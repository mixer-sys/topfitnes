import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        id=1,
        username='TestUser',
        email='testuser@yamdb.fake',
        password='1234567',
        role='user',
        first_name='first_name_user',
        last_name='last_name_user',
    )


@pytest.fixture
def user2(django_user_model):
    return django_user_model.objects.create_user(
        id=2,
        username='TestUser2',
        email='testuser2@yamdb.fake',
        password='1234567',
        role='user2',
        first_name='fn_user2',
        last_name='ln_user2',
    )


@pytest.fixture
def token_user(user):
    token = AccessToken.for_user(user)
    return {
        'access': str(token),
    }


@pytest.fixture
def user_client(token_user):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_user["access"]}')
    return client


@pytest.fixture
def api_client():
    return APIClient()
