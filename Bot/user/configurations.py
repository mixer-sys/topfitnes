USERS_INFO_URL = '/api/users_info/{chat}/'
USERS_INFO_GET_URL = '/api/users_info/'
USERS_URL = '/api/users/'

MEN = 'men'
WOMEN = 'women'
UNDEFINED = 'undefined'
SEX_CHOICES = {
    MEN: 'Мужской',
    WOMEN: 'Женский'
}

GAIN_MUSCLE_MASS = 'Gain muscle mass'
KEEPING_FIT = 'Keeping fit'
WEIGHT_LOSS = 'Weight Loss'
TARGET_CHOICES = {
    GAIN_MUSCLE_MASS: 'Набор мышечной массы',
    KEEPING_FIT: 'Поддержание формы',
    WEIGHT_LOSS: 'Сброс веса'
}

AGE = 'age'
WEIGHT = 'weight'
HEIGHT = 'height'
SEX = 'sex'

PARAMETERS = {
    AGE: 'возраст',
    WEIGHT: 'вес',
    HEIGHT: 'рост',
    SEX: 'пол'
}

ENTER_TEMPLATE = 'Введите {parameter}:'
OUTPUT_TEMPLATE = 'Вы ввели {parameter}: {text}'
ERROR_TEMPLATE = 'Ошибка: {message}'


HELP_MESSAGE = ('Бот для здорого питания'
                '\nПри нажатии на кнопку "Сон",'
                'будет зафиксировано время отдхоа к сну и время подъема'
                '\nКалории и бжу расчитают вашу норму на день'
                ' исходя из ваших показателей'
                '\nВ режиме "Тренировка" вам будут предоставлены'
                'тренировки различных типов'
                )
