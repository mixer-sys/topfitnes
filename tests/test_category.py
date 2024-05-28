from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestCategoryAPI:

    url = '/api/category/'

    def test_category_get(self, client, category1):
        response = client.get(self.url)
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.url}` не найден. Проверьте '
            'настройки в *urls.py*.'
        )
        assert response.status_code == HTTPStatus.OK, (
            'GET-запрос неавторизованного пользователя к '
            f'`{self.url}` возвращает ответ со статусом 200.'
        )
        assert response.json() == [{'pk': 1, 'name': 'Подержание'}], (
            'GET-запрос неавторизованного пользователя к '
            f'`{self.url}` проверки структуры ответа.'
        )

    def test_category_post_del_patch(self, client):

        data = {'name': 'Название категории'}
        text = '{}-запрос неавторизованного пользователя, на эндпоинт' \
               '`{}`, метод не разрешон ответ со статусом 405.'

        response = client.post(self.url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('POST', self.url)
        )
        response = client.delete(self.url)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('DELETE', self.url)
        )
        response = client.patch(self.url, data=data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('PATCH', self.url)
        )
