from urllib.parse import urljoin

import aiohttp
import asyncio
import async_timeout
from aiohttp.client_exceptions import ClientConnectorError

from workoutsession.url import (
    WORKOUTSESSION_URL, WORKOUTSESSION_POST_URL
)
from local_settings import BACKEND_URL


WAIT = 5


async def patch_workoutsession(pk, data):
    async with aiohttp.ClientSession() as session:
        url = urljoin(
            BACKEND_URL,
            WORKOUTSESSION_URL.format(pk)
        )
        try:
            async with async_timeout.timeout(WAIT):
                async with session.patch(url, json=data) as response:
                    response_data = await response.json()
                    return response_data
        except asyncio.TimeoutError:
            return None
        except ClientConnectorError:
            return None


async def post_workoutsession(data):
    async with aiohttp.ClientSession() as session:
        url = urljoin(
            BACKEND_URL,
            WORKOUTSESSION_POST_URL
        )
        try:
            async with async_timeout.timeout(WAIT):
                async with session.post(url, json=data) as response:
                    response_data = await response.json()
                    return response_data
        except asyncio.TimeoutError:
            return None
        except ClientConnectorError:
            return None


async def delete_workoutsession(pk):
    async with aiohttp.ClientSession() as session:
        url = urljoin(
            BACKEND_URL,
            WORKOUTSESSION_URL.format(pk)
        )
        try:
            async with async_timeout.timeout(WAIT):
                async with session.delete(url) as response:
                    return await response.json()
        except asyncio.TimeoutError:
            return None
        except ClientConnectorError:
            return None
