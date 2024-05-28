from http import HTTPStatus

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.context import FSMContext

from .configurations import (
    FACE_WITH_MONOCLE,
    GRINNING_FACE,
    ExecutionLevel,
)
from .utils import (
    isfloat, what_already_introduced,
    get_learns_calorie, post_record_bzu,
    checking_for_full_input,
)
from .keyboard_set import (
    Keyboard_bzu, Keyboard_main_menu, keyboard_back
)

router = Router()

# Глобальные переменыедля для внесение Билка, Жира, Углерода.
BZU = {'БЕЛОК': None, 'ЖИР': None, 'УГЛЕВОД': None}
TEMP_ATTRIBUTE: str = None


@router.message(
    Command("menu_calori"),  # Команда для запуска
    StateFilter(None)
)
async def main_menu(
    message: types.Message,
    state: FSMContext
):
    """Меню работы с калориями и БЖУ."""
    await state.set_state(ExecutionLevel.menu_calori_and_bzu)
    await message.answer(
        'Что сделать:',
        reply_markup=Keyboard_main_menu
    )


@router.message(
    ExecutionLevel.menu_calori_and_bzu,
    F.text.lower() == 'назад'
)
async def return_main_menu(
    message: types.Message,
    state: FSMContext
):
    """Вернуться в главное меню."""
    await state.clear()
    await message.answer(
        text='Главное меню:',
        reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(
    ExecutionLevel.menu_calori_and_bzu,
    F.text.lower() == 'калории'
)
async def calculate_calorie_allowance(
    message: types.Message,
):
    """Расчитать нормы калории на текущего пользователя."""
    result = await get_learns_calorie(str(message.from_user.id))
    await message.answer(f'Норма колорий: {result["result"]}')


@router.message(
    ExecutionLevel.menu_calori_and_bzu,
    F.text.lower() == 'внести бжу'
)
async def with_bju(
    message: types.Message,
    state: FSMContext
):
    """Внести: Белки, Жиры, Углеводы."""
    await state.set_state(ExecutionLevel.bzu_calculation)
    text = 'Нужно внести:\nБелок, Жиры, Углеводы.'
    await message.answer(text, reply_markup=Keyboard_bzu)


@router.message(
    ExecutionLevel.menu_calori_and_bzu,
)
async def catching_garbage_main_menu(
    message: types.Message,
):
    """Отлавливаю  мусор в меню калории и внесением БЖУ."""
    await message.answer(text=FACE_WITH_MONOCLE)


@router.message(
    ExecutionLevel.bzu_calculation,
    F.text.lower() == 'назад'
)
async def return_calori_and_bzu_menu(
    message: types.Message,
    state: FSMContext
):
    """Вернуться в меню калорий и БЖУ."""
    await state.set_state(ExecutionLevel.menu_calori_and_bzu)
    await message.answer(
        text='Показатели БЖУ не сохранены.',
        reply_markup=Keyboard_main_menu
    )


@router.message(
    ExecutionLevel.bzu_calculation,
    F.text.in_(['Белок', 'Жир', 'Углевод'])
)
async def initializing_water_bzu(
    message: types.Message,
    state: FSMContext
):
    """Инцелизирую ввод БЖУ."""
    await state.set_state(ExecutionLevel.entering_bzu)
    global TEMP_ATTRIBUTE
    if TEMP_ATTRIBUTE is None:
        TEMP_ATTRIBUTE = (message.text).upper()
    await message.answer(f'Внесите {TEMP_ATTRIBUTE}:')


@router.message(
    ExecutionLevel.bzu_calculation,
)
async def catch_garbage_when_in_menu_water_bzu(
    message: types.Message,
):
    """Отлавливаю  мусор в меню выбора внесение БЖУ."""
    await message.answer(text=FACE_WITH_MONOCLE,)
    await message.answer(text='Упс, что-то пошло не так' +
                         '\nНажмите кнопку "назад"',
                         reply_markup=keyboard_back)


@router.message(
    ExecutionLevel.entering_bzu,
    F.text.lower() == 'назад'
)
async def return_menu_calorie_and_bzu(
    message: types.Message,
    state: FSMContext
):
    """Вернуться в меню калорий и БЖУ."""
    await state.set_state(ExecutionLevel.menu_calori_and_bzu)
    global BZU
    BZU = BZU.fromkeys(BZU, None)
    text = 'Показатели БЖУ не сохранены.'
    await message.answer(text, reply_markup=Keyboard_main_menu)


@router.message(
    ExecutionLevel.entering_bzu,
)
async def entering_protein(
    message: types.Message,
    state: FSMContext
):
    """Обработка ввода БЖУ."""
    global TEMP_ATTRIBUTE
    global BZU
    result: dict = {}
    entering = isfloat(message.text)
    if entering:
        text = await what_already_introduced(entering, TEMP_ATTRIBUTE, BZU)
        TEMP_ATTRIBUTE = None
        if await checking_for_full_input(BZU):
            text = 'Данные Сохранены !!! ' + GRINNING_FACE
            result['user_id'] = message.from_user.id
            calorie = await get_learns_calorie(result['user_id'])
            result['calories'] = float(calorie["result"])
            result['protein'] = BZU['БЕЛОК']
            result['fats'] = BZU['ЖИР']
            result['carbohydrates'] = BZU['УГЛЕВОД']
            if await post_record_bzu(result) != HTTPStatus.CREATED:
                text = 'Не записал данные !!!'
            BZU = BZU.fromkeys(BZU, None)
            await message.answer(text, reply_markup=Keyboard_main_menu)
            await state.set_state(ExecutionLevel.menu_calori_and_bzu)
        else:
            await message.answer(text, reply_markup=Keyboard_bzu)
            await state.set_state(ExecutionLevel.bzu_calculation)
    else:
        text = f'{FACE_WITH_MONOCLE} .Внесите {TEMP_ATTRIBUTE}:'
        await message.answer(text)
