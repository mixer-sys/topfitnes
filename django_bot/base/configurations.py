from enum import Enum

SEC = 3600
BAD_SLEEP = 2
GOOD_SLEEP = 6
VERY_GOOD_SLEEP = 8

GAIN_MUSCLE_MASS = 'Gain muscle mass'
KEEPING_FIT = 'Keeping fit'
WEIGHT_LOSS = 'Weight Loss'
TARGET_CHOICES = (
    (GAIN_MUSCLE_MASS, 'Набор мышечной массы'),
    (KEEPING_FIT, 'Поддержание формы'),
    (WEIGHT_LOSS, 'Сброс веса'),
)

ADMINISTRATOR = 'administrator'
USER = 'user'
GUEST = 'guest'
BOT = 'bot'
ROLE_CHOICES = (
    (ADMINISTRATOR, 'Администратор'),
    (USER, 'Авторизованный пользователь'),
    (GUEST, 'Гость (неавторизованный пользователь)'),
    (BOT, 'Бот'),
)


MEN = 'men'
WOMEN = 'women'
UNDEFINED = 'undefined'
SEX_CHOICES = (
    (MEN, 'Мужской'),
    (WOMEN, 'Женский'),
    (UNDEFINED, 'Не определено')
)

"""Конфигурационые переменные для приложения [api]."""


# Максимум и Минемум КАЛОРИЙ в день.
MAXIMUM_CALORIES = 4000.0
MINIMUM_CALORIES = 1000.0
# Максимум и Минемум БЕЛКА в день.
MAXIMUM_PROTEIN = 1000.0
MINIMUM_PROTEIN = 0.0
# Максимум и Минемум ЖИРЫ в день.
MAXIMUM_FATS = 1000.0
MINIMUM_FATS = 0.0
# Максимум и Минемум УГЛЕВОДЫ в день.
MAXIMUM_CARBOHYDRATES = 1000.0
MINIMUM_CARBOHYDRATES = 0.0
# Минимальное значение для Идентификатор чата в телеграмме.
MINIMUM_CHAT_ID = 1
# Показатели для Мущины и Женщины
INDICATORS_MEN = [88.36, 13.4, 4.8, 5.7]
INDICATORS_WOMEN = [447.6, 9.2, 3.1, 4.3]
# Количество цыфр после запетой
OUTPUT_AFTER_COMMA = 3
# Процент для добавление при наборе веса
PERCENTAGE_WEIGHT_ADDITION = 20
# Процент для отнимание веса при худении
PERCENTAGE_WEIGHT_LOSS = 15
# Количество дней будет расчитываться количество тренеровок
RANGE_TRAINING_DAYS = 7
# Расщёт активность по количеству тренеровок
USER_ACTIVITY = {
    'Сидячий образ жизни': {
        'training': [0],
        'activity': 1.2
    },
    'Тренировки от 30мин 1-3 раза в неделю': {
        'training': [1, 2, 3],
        'activity': 1.375
    },
    'Тренировки 3-5 раз в неделю': {
        'training': [3, 5],
        'activity': 1.55
    },
    'Интенсивные тренировки 6-7 раз в неделю': {
        'training': [6, 7],
        'activity': 1.725
    },
    'Тренировки каждый день чаще чем раз в день': {
        'training': [x for x in range(8, 40, 1)],
        'activity': 1.9
    },
}


# Режин тренировки текучего пользователя
class TrainingMode(str, Enum):
    RESET = 'Сбросу'
    SUPPORT = 'Поддержки'
    WEIGHT_GAIN = 'Набору массы'


BEGINNER = 'beginner'
MIDDLE = 'middle'
PRO = 'pro'

DIFFICULTY_CHOICES = (
    (BEGINNER, 'Начинающий'),
    (MIDDLE, 'Средний'),
    (PRO, 'Продвинутый')
)
