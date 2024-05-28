import datetime

from aiogram import types

from sleep.configurations import BAD_SLEEP, GOOD_SLEEP, VERY_GOOD_SLEEP


async def take_user_info(callback: types.CallbackQuery, message: str):
    chat = callback.message.chat.id
    user_id = callback.from_user.id
    user_data = {
        'chat': chat,
        'user_id': user_id,
    }
    return user_data


def count_sleep(data_sleep, time_up):
    max_id = max(data_sleep, key=lambda x: x['id'])['id']
    filtered_data = list(filter(lambda x: x['id'] == max_id, data_sleep))
    last_date = filtered_data[0]['time_down']
    last_date = datetime.datetime.fromisoformat(last_date)
    formatted_date = last_date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    formatted_date = datetime.datetime.strptime(formatted_date,
                                                '%Y-%m-%d %H:%M:%S.%f')
    time_sleep = time_up - formatted_date
    hours, minutes, _ = str(time_sleep).split(":")
    return (hours, minutes, time_sleep)


def sleep_recomendations(hours):
    if hours < BAD_SLEEP:
        return 'Вы точно спали ?'
    if hours >= BAD_SLEEP and hours < GOOD_SLEEP:
        return ('Вы спали слишком мало' +
    '\nПосторайтесь в следующий раз лечь пораньше !')
    if hours >= GOOD_SLEEP and hours < VERY_GOOD_SLEEP:
        return 'Вы спали достаточно'
    if hours >= VERY_GOOD_SLEEP:
        return 'Вы спали очень много!'
