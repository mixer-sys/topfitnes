import pytest

from base.models import Category


@pytest.fixture
def category1():
    return Category.objects.create(name='Подержание',)


@pytest.fixture
def category2():
    return Category.objects.create(name='Сброс веса',)


@pytest.fixture
def category3():
    return Category.objects.create(name='Набор веса',)
