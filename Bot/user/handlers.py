from aiogram import F, Router, types
from aiogram.filters.command import CommandStart
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from core import (
    start_logging
)
from user.keyboard import (
    menu_builder, parameters_builder,
    sex_builder,
    target_builder
)
from user.configurations import (
    AGE, ENTER_TEMPLATE,
    GAIN_MUSCLE_MASS, HEIGHT,
    KEEPING_FIT, MEN, OUTPUT_TEMPLATE,
    PARAMETERS, SEX, SEX_CHOICES,
    TARGET_CHOICES,
    WEIGHT, WEIGHT_LOSS, WOMEN,
    HELP_MESSAGE,
)
from user.utils import (
    get_user_info_or_create_new,
    patch_user_info
)

user_router = Router()
logger = start_logging()


@user_router.message(CommandStart())
async def cmd_start(message: types.Message):
    chat = message.chat.id
    await get_user_info_or_create_new(
        chat=chat,
        message=message
    )

    await message.answer(
        'Здравствуйте, какую цель вы преследуете?',
        reply_markup=target_builder.as_markup()
    )


async def choose_target(callback: types.CallbackQuery, message: str):
    await callback.message.answer(
        f'Ваша цель: {TARGET_CHOICES[message]}'
    )
    chat = callback.message.chat.id
    data = {
        'target': message
    }
    logger.debug(data)
    await patch_user_info(data=data, chat=chat, message=callback.message)

    await callback.message.answer(
        'Ваши параметры:',
        reply_markup=parameters_builder.as_markup()
    )


@user_router.callback_query(F.data == 'choose_gain_muscle_mass')
async def choose_gain_muscle_mass(callback: types.CallbackQuery):
    await choose_target(callback, GAIN_MUSCLE_MASS)


@user_router.callback_query(F.data == 'choose_keeping_fit')
async def choose_keeping_fit(callback: types.CallbackQuery):
    await choose_target(callback, KEEPING_FIT)


@user_router.callback_query(F.data == 'choose_weight_loss')
async def choose_weight_loss(callback: types.CallbackQuery):
    await choose_target(callback, WEIGHT_LOSS)


class Form(StatesGroup):
    age = State()
    weight = State()
    height = State()
    sex = State()


@user_router.callback_query(F.data == AGE)
async def age(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        ENTER_TEMPLATE.format(parameter=PARAMETERS[AGE])
    )
    await state.set_state(Form.age)


@user_router.callback_query(F.data == WEIGHT)
async def weight(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        ENTER_TEMPLATE.format(parameter=PARAMETERS[WEIGHT])
    )
    await state.set_state(Form.weight)


@user_router.callback_query(F.data == HEIGHT)
async def height(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer(
        ENTER_TEMPLATE.format(parameter=PARAMETERS[HEIGHT])
    )
    await state.set_state(Form.height)


@user_router.callback_query(F.data == SEX)
async def sex(callback_query: types.CallbackQuery, state: FSMContext):
    print('Я тут')
    await callback_query.message.answer(
        ENTER_TEMPLATE.format(parameter=PARAMETERS[SEX]),
        reply_markup=sex_builder.as_markup()
    )


async def choose_sex(callback: types.CallbackQuery, sex: str):
    parameter = SEX
    await callback.message.answer(
        OUTPUT_TEMPLATE.format(
            parameter=PARAMETERS[parameter],
            text=SEX_CHOICES[sex]
        )
    )
    chat = callback.message.chat.id
    data = {
        parameter: sex
    }
    logger.debug(data)
    await patch_user_info(data=data, chat=chat, message=callback.message)


@user_router.callback_query(F.data == MEN)
async def men(callback: types.CallbackQuery):
    await choose_sex(callback, MEN)


@user_router.callback_query(F.data == WOMEN)
async def women(callback: types.CallbackQuery):
    await choose_sex(callback, WOMEN)


async def process_parameters(message: types.Message, state: FSMContext):
    logger.debug(await state.get_state())
    parameter = None

    if AGE in await state.get_state():
        await state.update_data(age=message.text)
        parameter = AGE
    if HEIGHT in await state.get_state():
        await state.update_data(height=message.text)
        parameter = HEIGHT
    if WEIGHT in await state.get_state():
        await state.update_data(weight=message.text)
        parameter = WEIGHT
    if SEX in await state.get_state():
        await state.update_data(sex=message.text)
        parameter = SEX

    await message.answer(
        OUTPUT_TEMPLATE.format(
            parameter=PARAMETERS[parameter],
            text=message.text
        )
    )
    chat = message.chat.id
    data = {
        parameter: message.text
    }
    logger.debug(data)
    await patch_user_info(data=data, chat=chat, message=message)

    await state.clear()


@user_router.message(Form.age)
async def process_age(message: types.Message, state: FSMContext) -> None:
    await process_parameters(message=message, state=state)


@user_router.message(Form.weight)
async def process_weight(message: types.Message, state: FSMContext) -> None:
    await process_parameters(message=message, state=state)


@user_router.message(Form.height)
async def process_height(message: types.Message, state: FSMContext) -> None:
    await process_parameters(message=message, state=state)


@user_router.message(Form.sex)
async def process_sex(message: types.Message, state: FSMContext) -> None:
    await process_parameters(message=message, state=state)


@user_router.callback_query(F.data == 'menu')
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(
        'Меню:',
        reply_markup=menu_builder.as_markup()
    )


@user_router.message(Command('menu'))
async def menu_handler(message: types.Message):
    await message.answer(
        'Меню:',
        reply_markup=menu_builder.as_markup()
    )


@user_router.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer(HELP_MESSAGE)


@user_router.message(Command('change'))
async def change_handler(message: types.Message):
    await message.answer(
        'Меню:',
        reply_markup=target_builder.as_markup()
    )
