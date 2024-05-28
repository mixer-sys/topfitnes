from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


RANGE_APPROACHES = range(1, 7)
ADJUST_APPROACHES = 3
RANGE_REPETITIONS = range(5, 25)
ADJUST_REPETITIONS = 5

button_yes = KeyboardButton(text="Да")
button_no = KeyboardButton(text="Нет")
button_cancel = KeyboardButton(text='Отмена')
kb_yes_no = ReplyKeyboardMarkup(
            keyboard=[
                [button_yes, button_no]
            ],
            resize_keyboard=True,
        )


def kb_digits_builder(range, adjust):
    builder = ReplyKeyboardBuilder()
    for i in range:
        builder.add(KeyboardButton(text=str(i), callback_data=int(i)))
    builder.add(button_cancel)
    builder.adjust(adjust)
    return builder.as_markup(resize_keyboard=True)


kb_approaches = kb_digits_builder(RANGE_APPROACHES, ADJUST_APPROACHES)
kb_repetitions = kb_digits_builder(RANGE_REPETITIONS, ADJUST_REPETITIONS)
