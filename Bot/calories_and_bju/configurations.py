import emoji
from aiogram.filters.state import State, StatesGroup

# УРЛ запроста на получение о пользователе
URL_CALORIES: str = lambda x: f'http://127.0.0.1:8000/api/calories/{x}/'
URL_BZU = 'http://127.0.0.1:8000/api/nutrients/'

# emoji
FACE_WITH_MONOCLE = emoji.emojize(":face_with_monocle:")
GRINNING_FACE = emoji.emojize(':grinning_face:')


# Уровень выполнения запросов
class ExecutionLevel(StatesGroup):
    menu_calori_and_bzu = State()
    bzu_calculation = State()
    entering_bzu = State()
