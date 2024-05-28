from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestSleepAPI:

    url_down = '/api/sleep/down/'
    url_up = '/api/sleep/up/'
    data = {}
    data_new = {
        "time_down": "2024-04-18 10:55:43.313943",
        "time_up": "2024-04-18 11:20:43.313943"
    }

    def test_Sleep_not_authorized_user_post(
            self, api_client, user, userinfo
    ):
        # требует чтоб пользователь был авторизован
        # Проработать права нужно
        api_client.force_login(user)
        response = api_client.post(self.url_down)
        assert response.status_code == HTTPStatus.OK, (
            'POST-запрос проверяет внесёные данные зарегистрированым'
            f' пользователя по `{self.url_down}`, ответ со статусом 200.'
        )

    def test_Sleep_not_authorized_user_del_patch_get(
            self, api_client
    ):
        text = 'Метод {}- не реализован для неавторизованного пользователя,' \
               ' к энтпоинту `{}`, должен вернуться ответ со статусом 405.'
        response = api_client.get(self.url_down)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('GET', self.url_down)
        )
        response = api_client.get(self.url_up)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('GET', self.url_up)
        )
        response = api_client.delete(self.url_down)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('DELETE', self.url_down)
        )
        response = api_client.delete(self.url_up)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('DELETE', self.url_up)
        )
        response = api_client.patch(self.url_down, data=self.data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('PATCH', self.url_down)
        )
        response = api_client.patch(self.url_up, data=self.data)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            text.format('PATCH', self.url_up)
        )
