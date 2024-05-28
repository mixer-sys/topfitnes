from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

from sleep.configurations import SLEEP_DOWN_OR_NOT, SLEEP_DOWN, DONT_SLEEP


accept_sleep_down = InlineKeyboardBuilder()
accept_sleep_down.add(types.InlineKeyboardButton(
    text=SLEEP_DOWN_OR_NOT[SLEEP_DOWN],
    callback_data='sleep_down',
    row_width=1
    )
)
accept_sleep_down.add(types.InlineKeyboardButton(
    text=SLEEP_DOWN_OR_NOT[DONT_SLEEP],
    callback_data='menu',
    row_width=1
    )
)


accept_sleep_up = InlineKeyboardBuilder()
accept_sleep_up.add(types.InlineKeyboardButton(
    text='Проснуться',
    callback_data='sleep_up',
    row_width=1
    )
)

return_menu = InlineKeyboardBuilder()
return_menu.add(types.InlineKeyboardButton(
    text='Меню',
    callback_data='menu',
    )
)
