# API Currency Django

## Описание

Этот проект на Django предоставляет API-эндпоинт для получения актуального курса доллара к рублю с историей последних 10 запросов.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/TrokhinMaxim/api_currency_django.git
    cd api_currency_django
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Примените миграции:

    ```bash
    python manage.py migrate
    ```

## Использование

1. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

2. Перейдите по адресу [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/) для получения текущего курса доллара к рублю и истории последних 10 запросов.

## Ограничения запросов

Запросы к API ограничены одним запросом в 10 секунд.


