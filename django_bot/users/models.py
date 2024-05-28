from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxValueValidator, MinValueValidator
)
from django.db import models

from base.configurations import (
    ROLE_CHOICES, SEX_CHOICES, TARGET_CHOICES
)


class UserInfo(models.Model):
    chat = models.BigIntegerField(
        'Идентификатор чата в телеграмме',
        unique=True
    )
    age = models.SmallIntegerField(
        'Возраст',
        null=True,
        validators=[MaxValueValidator(120), MinValueValidator(3)]
    )
    weight = models.SmallIntegerField(
        'Вес',
        null=True,
        validators=[MaxValueValidator(200), MinValueValidator(25)]
    )
    height = models.SmallIntegerField(
        'Рост',
        null=True,
        validators=[MaxValueValidator(250), MinValueValidator(100)]
    )
    sex = models.CharField(
        'Пол',
        choices=SEX_CHOICES,
        default='Не определен',
        max_length=32,
    )
    target = models.CharField(
        'Цель пользователя',
        max_length=64,
        choices=TARGET_CHOICES,
        default='Поддержание формы'
    )

    user = models.OneToOneField(
        'User',
        verbose_name='Пользователи',
        on_delete=models.CASCADE,
        related_name='info',
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class User(AbstractUser):

    role = models.CharField(
        'Роль пользователя',
        max_length=13,
        choices=ROLE_CHOICES,
        default='user',
    )
    first_name = models.CharField('Имя', max_length=150, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True,
                                 null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
