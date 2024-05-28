from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestUserAPI:

    url_reg = '/api/users/'
    url_token = '/api/auth/token/login/'
    url_logout = '/api/auth/token/logout/'

    def test_user_registration_and_token(
            self, api_client, user_client
    ):
        new_user = {
            "username": "user3",
            "password": "gh@hjhi765oi",
            "email": "user3@mail.ru"
        }
        response = api_client.post(self.url_reg, data=new_user)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.url_reg}` не найден. Проверьте '
            'настройки в *urls.py*.'
        )
        assert response.status_code == HTTPStatus.CREATED, (
            'POST-запрос регистация пользователя пользователя по '
            f'`{self.url_reg}`, возвращает ответ со статусом 201.'
        )

        user = {
            "username": "user3",
            "password": "gh@hjhi765oi"
        }

        response = api_client.post(self.url_token, data=user)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.url_token}` не найден. Проверьте '
            'настройки в *urls.py*.'
        )
        assert response.status_code == HTTPStatus.OK, (
            'POST-запрос получить токен для пользователя по '
            f'`{self.url_token}`, возвращает ответ со статусом 200.'
        )
