from typing import Union

import aiohttp

from .configurations import URL_CALORIES, URL_BZU


def isfloat(
    meaning: str
) -> Union[float, None]:
    """Проверка на число."""
    try:
        value = float(meaning)
    except (TypeError, ValueError):
        return None
    else:
        return value


async def what_already_introduced(
    meaning: float,
    indicator: str,
    bzu: dict,
) -> str:
    """Выводит список что уже пользователь вёл."""
    bzu[indicator] = meaning
    text = 'Что уже введено: \n'
    for key, value in bzu.items():
        text += f"{key}: {str(value)} \n"
    return text


async def get_learns_calorie(meaning: str):
    """Отправка запроста о пользователе."""
    async with aiohttp.ClientSession() as session:
        async with session.post(URL_CALORIES(meaning)) as response:
            return await response.json()


async def post_record_bzu(bzu: dict) -> int:
    """Отправка на запись данных БЖУ на API."""
    async with aiohttp.ClientSession() as session:
        async with session.post(URL_BZU, data=bzu) as response:
            return response.status


async def checking_for_full_input(bzu: dict) -> bool:
    """Проверка что внесены все данные."""
    for value in bzu.values():
        if not value:
            return False
    return True
