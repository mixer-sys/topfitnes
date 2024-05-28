import random
from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestCaloriesAPI:

    url = '/api/calories/{}/'

    untrained_user = {"result": "Пользователь не тренировался."}

    def pk(
            self,
            to_begin: int = 1000000010,
            before: int = 10000000000
    ):
        return random.randint(to_begin, before)

    def test_calories_get(
            self, client, user, userinfo, workout_userinfo,
            user2, userinfo2
    ):
        response = client.get(self.url.format(self.pk()))
        assert response.status_code == HTTPStatus.NOT_FOUND, (
            'GET-запрос не зарегистрированым пользователя к '
            f'`{self.url}` возвращает ответ со статусом 404.'
        )
        response = client.get(self.url.format(1000000005))
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос зарегистрированым пользователя к '
            f'`{self.url.format(1000000005)}` возвращает'
            'ответ со статусом 200.'
        )
        assert response.json() == self.untrained_user, (
            'Проверьте, что GET-запрос зарегистрированым пользователя к '
            f'`{self.url.format(1000000005)}` возвращает'
            'ответ пользователь не тренировался.'
        )
        response = client.get(self.url.format(1000000001))
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос зарегистрированым пользователя к '
            f'`{self.url.format(1000000001)}` возвращает'
            ' ответ со статусом 200.'
        )
        assert response.json() == {"result": "2030.545"}, (
            'Проверьте, что GET-запрос зарегистрированым пользователя к '
            f'`{self.url.format(1000000001)}` возвращает'
            ' ответ норме калорий расчитаный по формуле.'
        )

    def test_calories_post_del_patch(self, client):

        url = self.url.format(self.pk())
        data = {'result': 'Название категории'}
        text = 'Метод {}- не реализован для неавторизованного пользователя,' \
               ' к энтпоинту `{}`, должен вернуться ответ со статусом 405.'
        response = client.post(url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('POST', url)
        )
        response = client.delete(url)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('DELETE', url)
        )
        response = client.patch(url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('PATCH', url)
        )
