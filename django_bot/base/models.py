from django.db import models
from users.models import User
from django_bot.settings import MEDIA_ROOT
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from .configurations import (
    MAXIMUM_CALORIES,
    MINIMUM_CALORIES,
    MAXIMUM_PROTEIN,
    MINIMUM_PROTEIN,
    MAXIMUM_FATS,
    MINIMUM_FATS,
    MAXIMUM_CARBOHYDRATES,
    MINIMUM_CARBOHYDRATES,
    MINIMUM_CHAT_ID,
    DIFFICULTY_CHOICES
)


class Sleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_down = models.DateTimeField(
        'Отход к сну',
        blank=True,
        null=True,
    )
    time_up = models.DateTimeField(
        'Подъем',
        blank=True,
        null=True,
    )
    time_sleep = models.TextField(
        'Время сна',
        blank=True,
        null=True
    )

    def __str__(self):
        return "Заснул в %s, проснулся в %s" % (self.time_down, self.time_up)


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=32
    )

    def __str__(self) -> str:
        return self.name


class TrainingVideo(models.Model):
    title = models.CharField(
        name='Название видео',
        max_length=100
    )
    description = models.TextField('Описание видео')
    duration = models.FloatField('Продолжительность видео в минутах')
    file_path = models.FileField('Путь к файлу с видео', upload_to=MEDIA_ROOT)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name='категория тренировки'
    )
    difficulty = models.CharField(
        'Сложность',
        choices=DIFFICULTY_CHOICES,
        default='Начинающий',
        max_length=32,
    )

    def __str__(self) -> str:
        return self.title


class WorkoutSession(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workoutsession',
        verbose_name='Тренировка пользователя'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время начала тренировки'
    )
    count_approaches = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Количество подходов'
    )
    count_repetitions = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Количество повторений'
    )

    title_exercise = models.TextField(
        'Название тренировки',
        blank=True,
        null=True
    )


class Nutrients(models.Model):
    "Модель Калории и БЖУ"
    NUTRIENTS_TEMPLATE = '{}: {} {} {} {}'
    chat = models.IntegerField(
        'Идентификатор чата в телеграмме',
        validators=[
            MinValueValidator(MINIMUM_CHAT_ID),
        ]
    )
    calories = models.FloatField(
        'Калории',
        validators=[
            MinValueValidator(MINIMUM_CALORIES),
            MaxValueValidator(MAXIMUM_CALORIES)
        ]
    )
    protein = models.FloatField(
        'Белок',
        validators=[
            MinValueValidator(MINIMUM_PROTEIN),
            MaxValueValidator(MAXIMUM_PROTEIN)
        ]
    )
    fats = models.FloatField(
        'Жир',
        validators=[
            MinValueValidator(MINIMUM_FATS),
            MaxValueValidator(MAXIMUM_FATS)
        ]
    )
    carbohydrates = models.FloatField(
        'Углевод',
        validators=[
            MinValueValidator(MINIMUM_CARBOHYDRATES),
            MaxValueValidator(MAXIMUM_CARBOHYDRATES)
        ]
    )
    date_record = models.DateTimeField(
        'Дата записи.',
        auto_now_add=True,
    )

    class Meta:
        ordering = ['chat']
        verbose_name = 'Питательные вещества продукта'
        verbose_name_plural = 'Питательные вещества'

    def __str__(self) -> str:
        return self.NUTRIENTS_TEMPLATE.format(
            self.chat,
            self.calories,
            self.protein,
            self.fats,
            self.carbohydrates,
        )
