from aiogram import types, F, Router, html
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)

from core import start_logging
from user.utils import (
    get_user_id
)
from workoutsession.states import WorkoutSessionForm
from workoutsession.data_fetcher import (
    post_workoutsession
)
from workoutsession import keyboards

logger = start_logging()

form_router = Router()


@form_router.callback_query(F.data == 'training')
async def training(callback: types.CallbackQuery):
    await callback.message.answer(
        'Тренировка'
    )
    await callback.message.answer(
        'Привет! Вы будуте сейчас заниматься?',
        reply_markup=keyboards.kb_yes_no
    )


@form_router.message(F.text == 'Отмена')
@form_router.message(F.text == 'Нет')
async def process_dindnt_do_workoutsession(message: Message,
                                           state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        'До скорой встречи!',
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(F.text == 'Да')
async def process_did_workoutsession(message: Message,
                                     state: FSMContext) -> None:
    await state.set_state(WorkoutSessionForm.count_approaches)

    await message.reply(
        'Отлично! Сколько подходов вы сдеалали?',
        reply_markup=keyboards.kb_approaches,
    )


@form_router.message(WorkoutSessionForm.count_approaches,
                     F.text.regexp(r'^(\d+)$').as_('digits'))
async def process_did_approaches(message: Message, state: FSMContext) -> None:
    await state.update_data(count_approaches=message.text)
    await state.set_state(WorkoutSessionForm.count_repetitions)
    await message.reply(
        'Супер! Сколько было повторений в каждом повторе?',
        reply_markup=keyboards.kb_repetitions,
    )


@form_router.message(WorkoutSessionForm.count_repetitions,
                     F.text.regexp(r'^(\d+)$').as_('digits'))
async def process_repetitions(message: Message, state: FSMContext) -> None:
    data = await state.update_data(count_repetitions=message.text)
    data = {key: int(value) if value.isdigit() else value
            for key, value in data.items()}
    await state.clear()

    chat = message.chat.id
    data['user_id'] = await get_user_id(chat, message)
    print(data)
    logger.debug(data)

    return_data = await post_workoutsession(data)
    if return_data is not None:
        approaches = return_data['count_approaches']
        repetitions = return_data['count_repetitions']
        text = (
            f'Великолепно! '
            f'Вы сделали {html.quote(str(approaches))} подходов '
            f'и по {html.quote(str(repetitions))} повторений '
            f'в каждом подходе.'
        )
    else:
        text = 'Well done! Could not save it'
    await message.reply(text=text, reply_markup=ReplyKeyboardRemove())
