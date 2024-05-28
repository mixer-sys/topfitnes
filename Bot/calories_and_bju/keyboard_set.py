from aiogram import types

"""Кнопки для меню (вынести к кнопкам)."""
main_menu_calories = [
    [
        types.KeyboardButton(text='Калории'),
        types.KeyboardButton(text='Внести БЖУ')
    ],
    [
        types.KeyboardButton(text='Назад'),
    ]
]

keyboard_back = types.ReplyKeyboardMarkup(
        keyboard=[main_menu_calories[1]],
        resize_keyboard=True,
    )

Keyboard_main_menu = types.ReplyKeyboardMarkup(
        keyboard=main_menu_calories,
        resize_keyboard=True,
    )


"""Кнопки для меню (вынести к кнопкам)."""
menu_bzu = [
    [
        types.KeyboardButton(text='Белок'),
        types.KeyboardButton(text='Жир'),
        types.KeyboardButton(text='Углевод')
    ],
    [
        types.KeyboardButton(text='Назад'),
    ]
]
Keyboard_bzu = types.ReplyKeyboardMarkup(
        keyboard=menu_bzu,
        resize_keyboard=True,
    )
