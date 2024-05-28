# README.md

Добро пожаловать в README.md для вашего проекта на Django REST Framework (DRF) и Aiogram. Этот файл поможет вам быстро начать работу с вашим проектом и предоставит всю необходимую информацию для его настройки и запуска.

## Проект

Проект представляет собой чат-бота, который взаимодействует с пользователями через мессенджер. Бот предоставляет различные функции, такие как отправка сообщений, обработка команд и выполнение действий.

## Настройка

Чтобы начать работу с проектом, выполните следующие шаги:

1. Установите необходимые зависимости:

pip install -r requirements.txt


2. Запустите сервер DRF:

python manage.py runserver


3. Запустите бота Aiogram:

python bot.py

## Быстрое развертывание:

```
git clone https://github.com/Studio-Yandex-Practicum/begin_with_yourself_bot_1.git

cd begin_with_yourself_bot_1/infra/
```
Измените .env.example и переименуйте в .env
```
docker compose -f docker-compose.production.yml up -d

docker compose exec django_bot python manage.py makemigrations

docker compose exec django_bot python manage.py migrate

docker compose -f docker-compose.production.yml down

docker compose -f docker-compose.production.yml up -d

```

## Использование

После запуска сервера и бота вы можете начать взаимодействие с ними. Для этого отправьте сообщение боту в мессенджере, где он был добавлен.

## Команды

Бот поддерживает следующие команды:

- /help - отображает список всех доступных команд.
- /start - возвращает приветственное сообщение.

## Разработка

Для разработки и тестирования бота используйте следующий подход:

1. Откройте терминал и перейдите в директорию проекта.
2. Запустите сервер DRF и бота Aiogram.
3. Используйте команды бота для тестирования функциональности.

## Поддержка

Если у вас возникли вопросы или проблемы при работе с проектом, пожалуйста, обратитесь к документации или свяжитесь с нашей командой поддержки.

## Благодарность

Большое спасибо за использование нашего проекта! Мы надеемся, что он будет полезен для ваших нужд.

## Разработчики
https://github.com/Groul117
https://github.com/lyudaplp
https://github.com/maybeYOLO
https://github.com/OsKaLis
https://github.com/mixer-sys
https://github.com/mixer-sys
