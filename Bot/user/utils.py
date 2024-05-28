import aiohttp
from urllib.parse import urljoin
from http import HTTPStatus

from user.configurations import (
    ERROR_TEMPLATE,
    USERS_INFO_URL,
    USERS_INFO_GET_URL,
    USERS_URL
)
from local_settings import BACKEND_URL
from core import (
    get_random_password,
    start_logging
)


logger = start_logging()


async def check_errors(response, message):
    if ((response.status == HTTPStatus.OK)
       or (response.status == HTTPStatus.CREATED)):
        pass
    else:
        await message.answer(
            ERROR_TEMPLATE.format(
                message=await response.json()
            )
        )


async def get_user_info(chat: int, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            urljoin(BACKEND_URL, USERS_INFO_URL.format(chat=chat)
                    )
        ) as response:
            await check_errors(response=response, message=message)
            return response


async def get_user_id(chat: int, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            urljoin(BACKEND_URL, USERS_INFO_URL.format(chat=chat)
                    )
        ) as response:
            await check_errors(response=response, message=message)
            json = await response.json()
            return json.get('user').get('id')


async def post_user_info(data: dict, message):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            urljoin(BACKEND_URL, USERS_INFO_GET_URL),
            data=data
        ) as response:
            await check_errors(response=response, message=message)
            return response


async def patch_user_info(data: dict, chat: int, message):
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            urljoin(BACKEND_URL, USERS_INFO_URL.format(chat=chat)),
            data=data
        ) as response:
            await check_errors(response=response, message=message)
            return response


async def post_user(data: dict, message):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            urljoin(BACKEND_URL, USERS_URL),
            data=data
        ) as response:
            await check_errors(response=response, message=message)
            json = await response.json()
            return json.get('id')


async def get_user_info_or_create_new(chat: int, message):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            urljoin(BACKEND_URL, USERS_INFO_URL.format(chat=chat)
                    )
        ) as response:
            if response.status == HTTPStatus.NOT_FOUND:
                data = {
                    'username': message.chat.username,
                    'password': get_random_password(),
                    'first_name': message.chat.first_name or '',
                    'last_name': message.chat.last_name or ''
                }
                logger.debug(data)

                data = {
                    'user': await post_user(data=data, message=message),
                    'chat': chat
                }
                logger.debug(data)
                await post_user_info(data, message=message)
                return response
