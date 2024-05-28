import random
from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestWorkoutSessionAPI:

    url = '/api/workout_session/{}/'
    data_new = {
            "id": 1,
            "count_approaches": 6,
            "count_repetitions": 4
        }

    def pk(self):
        return random.randint(1, 10)

    def test_workout_session_not_authorized_user(self, client):
        url = self.url.format(self.pk())
        response = client.get(url)
        text = '{}-запрос проверяет доступность не зарегистрированым' \
               ' пользователя к `{}` возвращает ответ со статусом 403.'
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            text.format('GET', url)
        )
        response = client.post(url, data=self.data_new)
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            text.format('POST', url)
        )
        response = client.delete(url)
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            text.format('DELETE', url)
        )
        response = client.patch(url, data=self.data_new)
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            text.format('PATCH', url)
        )

    def test_workout_session_authorized_user_patch(
            self, api_client, workout_userinfo, user
    ):
        url = self.url.format('1')
        api_client.force_login(user)
        response = api_client.patch(url, data=self.data_new, format='json')
        assert response.status_code == HTTPStatus.OK, (
            'PATCH-запрос проверяет внесёные данные зарегистрированым'
            f' пользователя по `{url}` возвращает ответ со статусом 200.'
        )

    def test_workout_session_authorized_user_post_del_get(
            self, client, workout_userinfo, user
    ):
        url = self.url.format('1')
        client.force_login(user)
        text = '{}-запрос запрещён зарегистрированым' \
               ' пользователя по `{}` возвращает ответ со статусом 405.'
        response = client.post(url, data=self.data_new)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('POST', url)
        )

        response = client.delete(url, data=self.data_new)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('DELETE', url)
        )
        response = client.get(url)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('GET', url)
        )
