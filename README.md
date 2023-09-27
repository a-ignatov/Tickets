# Tickets

Сервис для создания заявок на обслуживание офисной техники и ремонта.

![ticket](https://github.com/a-ignatov/Tickets/blob/3d824e8d174828d228b0c5ec8b7f44feb42e3d45/back/tickets/templates/Screenshot.png)

- фреймворк приложения: Django 4
- база данных: SQLite
- создание пользователей через админку Django (http://127.0.0.1:8000/admin/)
- пользователи могут создавать и редактировать основное содержимое тикетов

____
# Инструкция по установке
- Клонировать репозиторий в рабочую папку 
```
git clone git@github.com:a-ignatov/Tickets.git
```
- Установить виртуальное окружение
```
python3.8 -m venv venv
```
- Обновить PIP
```
python3 -m pip install --upgrade pip
```
- Установить зависимости
```
python3 -m pip install -r requirements.txt
```
- Перейти в папку с утилитой manage.py
```
cd back/tickets
```
- Выполнить миграции БД и создать суперпользователя
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- Запустить сервер
```
python3 manage.py runserver
```
