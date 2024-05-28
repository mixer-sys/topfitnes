from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestTrainingVideoAPI:

    url = '/api/video/c/{}/d/{}'
    category = 3
    difficulty = 'Професиональный'

    def test_training_video_not_authorized_user(
            self, client, category2, category3,
            trainingvideo1, trainingvideo2, trainingvideo3
    ):
        url = self.url.format(self.category, self.difficulty)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, (
            'GET-запрос проверяет доступность не зарегистрированым'
            f' пользователя к `{url}` возвращает ответ со статусом 200.'
        )
        url = self.url.format('Не коректное значение', self.difficulty)
        response = client.get(url)
        assert response.status_code == HTTPStatus.NOT_FOUND, (
            'GET-запрос проверяет не корректный ввод показателей'
            f'для эндпоинта `{url}`,не зарегистрированым пользователя'
            ' возвращает ответ со статусом 404.'
        )

    def test_training_video_not_authorized_user_post_del_patch(
            self, client, category2, category3,
            trainingvideo1, trainingvideo2, trainingvideo3
    ):
        url = self.url.format(self.category, self.difficulty)
        data = {
            "title": "t4",
            "description": "ОП4",
            "duration": 65.0,
            "file_path": "путь 4",
            "category": 2,
            "difficulty": "Сброс"
        }
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
