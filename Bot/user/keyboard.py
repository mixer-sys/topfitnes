
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

from user.configurations import (
    GAIN_MUSCLE_MASS,
    KEEPING_FIT,
    MEN,
    PARAMETERS,
    SEX_CHOICES,
    TARGET_CHOICES,
    WEIGHT_LOSS,
    WOMEN
)

sex_builder = InlineKeyboardBuilder()
sex_builder.add(types.InlineKeyboardButton(
    text=SEX_CHOICES[MEN],
    callback_data=MEN
))
sex_builder.add(types.InlineKeyboardButton(
    text=SEX_CHOICES[WOMEN],
    callback_data=WOMEN
))

target_builder = InlineKeyboardBuilder()
target_builder.add(
    types.InlineKeyboardButton(
        text=TARGET_CHOICES[GAIN_MUSCLE_MASS],
        callback_data='choose_gain_muscle_mass',
        row_width=5
    )
)
target_builder.add(types.InlineKeyboardButton(
    text=TARGET_CHOICES[KEEPING_FIT],
    callback_data='choose_keeping_fit',
    row_width=1)
)
target_builder.add(types.InlineKeyboardButton(
    text=TARGET_CHOICES[WEIGHT_LOSS],
    callback_data='choose_weight_loss',
    row_width=1)
)


menu_builder = InlineKeyboardBuilder()
menu_builder.add(types.InlineKeyboardButton(
    text='Сон',
    callback_data='sleep')
)
menu_builder.add(types.InlineKeyboardButton(
    text='Каллории и БЖУ',
    callback_data='callories_cpf')
)
menu_builder.add(types.InlineKeyboardButton(
    text='Тренировка',
    callback_data='training')
)


parameters_builder = InlineKeyboardBuilder()
for parameter, value in PARAMETERS.items():
    parameters_builder.add(types.InlineKeyboardButton(
        text=value.capitalize(),
        callback_data=parameter)
    )
parameters_builder.add(types.InlineKeyboardButton(
    text='Меню',
    callback_data='menu')
)
