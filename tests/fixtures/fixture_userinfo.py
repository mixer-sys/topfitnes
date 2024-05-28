import pytest

from users.models import UserInfo


@pytest.fixture
def userinfo(user):
    return UserInfo.objects.create(
        id=1,
        chat=1000000001,
        age=18,
        weight=45,
        height=185,
        sex='муж',
        target='Поддержание',
        user=user,
    )


@pytest.fixture
def userinfo2(user2):
    return UserInfo.objects.create(
        id=2,
        chat=1000000005,
        age=18,
        weight=45,
        height=180,
        sex='жен',
        target='Поддержание',
        user=user2,
    )
