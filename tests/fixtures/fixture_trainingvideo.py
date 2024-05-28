import pytest

from base.models import TrainingVideo


@pytest.fixture
def trainingvideo1(category1):
    return TrainingVideo.objects.create(
        title='t1',
        description='Описание1',
        duration=60,
        file_path='путь к файлу f1.',
        category=category1,
        difficulty='Начальный',
    )


@pytest.fixture
def trainingvideo2(category2):
    return TrainingVideo.objects.create(
        title='t2',
        description='Описание2',
        duration=60,
        file_path='путь к файлу f2.',
        category=category2,
        difficulty='Средний',
    )


@pytest.fixture
def trainingvideo3(category3):
    return TrainingVideo.objects.create(
        title='t3',
        description='Описание3',
        duration=60,
        file_path='путь к файлу f3.',
        category=category3,
        difficulty='Професиональный',
    )
