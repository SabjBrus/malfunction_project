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
