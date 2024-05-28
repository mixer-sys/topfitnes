import logging
import datetime
import requests
from urllib.parse import urljoin

from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup

from sleep import keyboards
from user.utils import (
    get_user_id,
)
from .utils import take_user_info, count_sleep, sleep_recomendations
from .configurations import SLEEP_DOWN_URL
from local_settings import BACKEND_URL

sleep_router = Router()
logger = logging.getLogger(__name__)


class Form(StatesGroup):
    sleep_down = State()


@sleep_router.callback_query(F.data == 'sleep')
async def sleep(callback: types.CallbackQuery):
    await callback.message.answer(
        'Вы ложитесь спать ?',
        reply_markup=keyboards.accept_sleep_down.as_markup()
    )


@sleep_router.callback_query(F.data == 'sleep_down')
async def sleep_down(callback: types.CallbackQuery, state: FSMContext):
    chat_data = await take_user_info(callback, 'post')
    chat = chat_data['chat']
    user_id = await get_user_id(chat, 'post')
    time_down = datetime.datetime.now()
    data = {
        'user': user_id,
        'time_down': time_down.strftime('%Y-%m-%d %H:%M:%S')
    }
    response = requests.post(
        urljoin(BACKEND_URL, SLEEP_DOWN_URL), json=data
    )
    if response.status_code == 201:
        print(time_down)
        await callback.message.answer(
            'Добрых снов\n' +
            f'Вы начали спать в: {str(time_down)[11:16]}' +
            '\nКак проснётесь нажмите на кнопку ниже',
            reply_markup=keyboards.accept_sleep_up.as_markup()
        )
    else:
        await callback.message.answer('Ошибка при записи сна')


@sleep_router.callback_query(F.data == 'sleep_up')
async def sleep_up(callback: types.CallbackQuery, state: FSMContext):
    chat_data = await take_user_info(callback, 'post')
    chat = chat_data['chat']
    user_id = await get_user_id(chat, 'post')
    time_up = datetime.datetime.now()

    data = {
        'user': user_id,
    }
    response = requests.get(
        urljoin(BACKEND_URL, SLEEP_DOWN_URL), json=data)
    data_sleep = response.json()
    sleep_count = count_sleep(data_sleep, time_up)
    recomendation = sleep_recomendations(int(sleep_count[0]))
    await callback.message.answer(
        'Доброе утро!\n' +
        f'Вы спали {int(sleep_count[0])} часов {int(sleep_count[1])} минут\n' +
        f'{recomendation}\n' +
        'Что бы вернуться в меню, нажмите на кнопку ниже',
        reply_markup=keyboards.return_menu.as_markup())


# @sleep_router.message(Form.sleep_down)
# async def process_sex(message: types.Message, state: FSMContext) -> None:
    # await sleep_process(message=message, state=state)"""
