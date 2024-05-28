from urllib.parse import urljoin
import aiohttp

from local_settings import BACKEND_URL
from user.configurations import USERS_INFO_URL


async def get_user_info(chat: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            urljoin(BACKEND_URL, USERS_INFO_URL.format(chat=chat)
                    )
        ) as response:
            return response


def norma(data):
    if data['sex'] == 'men':
        return (88.36 + (13.4 * data['weight'])
                + (4.8 * data['height']) - (5.7 * data['age']))
    else:
        return (447.59 + (9.24 * data['weight'])
                + (3.67 * data['height']) - (6.75 * data['age']))
