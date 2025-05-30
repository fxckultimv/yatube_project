# Cоциальная сеть Yatube

#### Описание

Позволяет авторам создавать записи на различные темы, комментировать их и подписываться либо отписываться от разных авторов контента. Включает в себя администрирование, управление пользователями, работу с записями (создание, редактирование, удаление), объединение записей по сообществам,  модель отправки электронных сообщений пользователям, основные шаблоны для страниц сайта. Для хранения данных используется SQLite.

#### Технологии

-   Python 3.7
-   Django 2.2.16

#### Запуск проекта в dev-режиме

-   Склонируйте репозиторий с помощью:  
    `git clone <название репозитория>`
-   Установите и активируйте виртуальное окружение:  
    `python -m venv venv`  
    `source venv/Scripts/activate`
-   Установите зависимости из файла requirements.txt:  `pip install -r requirements.txt`
-   Выполните команду:  `python manage.py runserver`