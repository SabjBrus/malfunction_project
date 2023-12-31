# Malfunction project

API для сервиса сбора и учёта ошибок и неисправностей
В разработке

## Технологии

- Python 3.11
- Django REST framework
- Docker
- Gunicorn
- PostgreSQL

## Запуск проекта

1. Склонировать репозиторий:

    ```bash
    git clone https://github.com/SabjBrus/malfunction_project.git
    ```

2. Установка и активация виртуального окружения

    ```bash
    python3 -m venv venv
    ```

    ```bash
    source venv/Scripts/activate
    ```

3. Установка зависимостей в виртуальном окружении

    ```bash
    pip install -r requirements.txt
    ```

4. Выполнение миграций

    ```bash
    python manage.py migrate
    ```

5. Запуск проекта

    ```bash
    python manage.py runserver
    ```

6. Создание суперпользователя

   ```bash
   python manage.py createsuperuser
   ```

## Эндпоинты

### Документация

<http://127.0.0.1:8000/api/v1/swagger>

### Создать пользователя

<http://127.0.0.1:8000/api/v1/auth/users/>

| Method | Request                                         | Response                                      |
|--------|-------------------------------------------------|-----------------------------------------------|
| POST   | email<br/>password<br/>first_name<br/>last_name | HTTP_201_CREATED or<br/> HTTP_400_BAD_REQUEST |

### Создать и удалить токен

<http://127.0.0.1:8000/api/v1/auth/token/login/>

| Method | Request            | Response     |
|--------|--------------------|--------------|
| POST   | email<br/>password | HTTP_200_OK  |

<http://127.0.0.1:8000/api/v1/auth/token/logout/>

| Method | Request | Response     |
|--------|---------|--------------|
| POST   | -       | HTTP_200_OK  |

### Действия пользователя

<http://127.0.0.1:8000/api/v1/auth/users/me/>

| Method | Request              | Response                                         |
|--------|----------------------|--------------------------------------------------|
| GET    | -                    | HTTP_200_OK                                      |
| PUT    | User.REQUIRED_FIELDS | HTTP_200_OK or<br/> HTTP_400_BAD_REQUEST         |
| PATCH  | User.REQUIRED_FIELDS | HTTP_200_OK or<br/> HTTP_400_BAD_REQUEST         |
| DELETE | current_password     | HTTP_204_NO_CONTENT or<br/> HTTP_400_BAD_REQUEST |

### Список пользователей

<http://127.0.0.1:8000/api/v1/users/>

| Method | Request | Response    |
|--------|---------|-------------|
| GET    | -       | HTTP_200_OK |

### Админка

<http://127.0.0.1:8000/admin/>

### Автор

Жуков Борис
