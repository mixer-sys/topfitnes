import requests

from aiogram import types, F
from aiogram import Router

from sleep.utils import take_user_info
from .utils import norma
from local_settings import BACKEND_URL
from user.configurations import USERS_INFO_GET_URL
bju_router = Router()


@bju_router.callback_query(F.data == 'callories_cpf')
async def sleep(callback: types.CallbackQuery):
    chat_data = await take_user_info(callback, 'post')
    chat = chat_data['chat']
    # user_id = await get_user_id(chat, 'post')
    response_data = requests.get(BACKEND_URL + USERS_INFO_GET_URL + str(chat))
    response_data = response_data.json()  # parse the JSON response
    data = {
        'age': response_data['age'],
        'sex': response_data['sex'],
        'height': response_data['height'],
        'weight': response_data['weight'],
        'target': response_data['target']
    }
    norma_bju = round(norma(data), 4)
    await callback.message.answer(
        f'Ваша норма Калорий в день {norma_bju}',
    )
