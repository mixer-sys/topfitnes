import pytest

from base.models import WorkoutSession


@pytest.fixture
def workout_userinfo(user):
    return WorkoutSession.objects.create(
        id=1,
        date='2024-04-13 10:16:43.313943',
        count_approaches=10,
        count_repetitions=10,
        user_id=user,
    )
