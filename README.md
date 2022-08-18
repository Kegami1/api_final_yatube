### Описание

API предоставляет доступ к сервису, который содержит посты, комментарии к ним, а так же позволяет пользователями подписываться друг на друга. Для авторизированных пользователей доступна возможность: создавать новые посты, комментировать чужие и свои публикации, подписываться на других пользователей.

### Технологии
Python 3.7

Django 2.2.16

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Kegami1/api_final_yatube.git
```
```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

Windows:
```
python -m venv venv
```
```
source venv/scripts/activate
```
Linux:
```
python3 -m venv env
```
```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```


Выполнить миграции:

Windows:
```
python manage.py migrate
```
Linux:
```
python3 manage.py migrate
```

Запустить проект:

Windows:
```
python manage.py runserver
```
Linux:
```
python3 manage.py runserver
```

### Примеры запросов

Запрос токена:
```
/auth/jwt/create/
```

Методом GET получить список всех постов и методом POST добавить свой пост:
```
/api/v1/posts/
```

