import aiohttp
from http import HTTPStatus
import async_timeout
import asyncio
from aiohttp.client_exceptions import ClientConnectorError
from urllib.parse import urljoin


from .configurations import (SLEEP_DOWN_URL, SLEEP_UP_URL, ERROR_TEMPLATE)
from local_settings import BACKEND_URL
WAIT = 5


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


async def post_sleep(data):
    async with aiohttp.ClientSession() as session:
        url = urljoin(BACKEND_URL, SLEEP_DOWN_URL)

        try:
            async with async_timeout.timeout(WAIT):
                async with session.post(url, json=data) as response:
                    response_data = await response.json()
                    return response_data
        except asyncio.TimeoutError:
            return None
        except ClientConnectorError:
            return None


async def sleep_up(data: dict, chat: int, message):
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            urljoin(BACKEND_URL, SLEEP_UP_URL.format(chat=chat)),
            data=data
        ) as response:
            await check_errors(response=response, message=message)
            return response
