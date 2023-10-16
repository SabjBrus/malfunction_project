# Malfunction project

Cервис сбора и учёта ошибок и неисправностей  
В разработке  

## Эндпоинты

### Создать пользователя

<http://127.0.0.1:8000/api/auth/users/>

| Method | Request                                         | Response                                      |
|--------|-------------------------------------------------|-----------------------------------------------|
| POST   | email<br/>password<br/>first_name<br/>last_name | HTTP_201_CREATED or<br/> HTTP_400_BAD_REQUEST |

### Создать и удалить токен

<http://127.0.0.1:8000/api/auth/token/login/>

| Method | Request            | Response     |
|--------|--------------------|--------------|
| POST   | email<br/>password | HTTP_200_OK  |

<http://127.0.0.1:8000/api/auth/token/logout/>

| Method | Request | Response     |
|--------|---------|--------------|
| POST   | -       | HTTP_200_OK  |

### Действия пользователя

<http://127.0.0.1:8000/api/auth/users/me/>

| Method | Request              | Response                                         |
|--------|----------------------|--------------------------------------------------|
| GET    | -                    | HTTP_200_OK                                      |
| PUT    | User.REQUIRED_FIELDS | HTTP_200_OK or<br/> HTTP_400_BAD_REQUEST         |
| PATCH  | User.REQUIRED_FIELDS | HTTP_200_OK or<br/> HTTP_400_BAD_REQUEST         |
| DELETE | current_password     | HTTP_204_NO_CONTENT or<br/> HTTP_400_BAD_REQUEST |

### Список пользователей

<http://127.0.0.1:8000/api/users/>

| Method | Request | Response    |
|--------|---------|-------------|
| GET    | -       | HTTP_200_OK |
