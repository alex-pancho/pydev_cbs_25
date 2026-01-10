# Лекція 1: Вступ до Django

## Що таке Django?

Django — це потужний Python web-фреймворк, який дозволяє швидко розробляти безпечні та масштабовані веб-додатки. Він слідує принципу "батарейки включені" (batteries included) — містить все необхідне для розробки, від ORM до адміністративного панелі.

### Основні характеристики Django:

- **MVT архітектура** (Model-View-Template): розділення кода на логічні компоненти
- **ORM** (Object-Relational Mapping): робота з БД через Python код
- **Адміністративна панель**: автоматично генерується з моделей
- **Вбудована система аутентифікації**: usuarios, групи, дозволи
- **Безпека**: CSRF захист, SQL-injection попередження
- **Масштабованість**: використовується Instagram, Pinterest, Spotify

## Цілі нашого проекту: Car Service API

Ми будемо розробляти **REST API для системи управління автосервісом** (`car_service_api_and_ui`).

Функціонал:
- Управління автомобілями (CRUD операції)
- Система користувачів (реєстрація, аутентифікація)
- Брендові та модельні довідники
- JWT токени для безпеки
- REST API з Swagger документацією
- Фронтенд інтерфейс

## Встановлення та перша конфігурація

### 1. Встановлення Django

```bash
# Створення віртуального середовища
python -m venv .venv

# Активація (на Linux/Mac)
source .venv/bin/activate

# Активація (на Windows)
.venv\Scripts\activate

# Встановлення Django
pip install django djangorestframework
```

### 2. Створення Django проекту

```bash
django-admin startproject autocheck_api .
```

Це створить структуру:
```
autocheck_api/
  ├── __init__.py
  ├── settings.py      # Конфігурація проекту
  ├── urls.py          # Маршрутизація
  ├── asgi.py          # Для async
  └── wsgi.py          # Для production
manage.py              # Утиліта управління
```

### 3. Створення Django додатків

```bash
# Основні додатки для проекту
python manage.py startapp cars      # Управління автомобілями
python manage.py startapp users     # Користувачі та аутентифікація
python manage.py startapp frontend  # Фронтенд сторінки
```

Кожний додаток має структуру:
```
cars/
  ├── migrations/      # Версіонування БД
  ├── __init__.py
  ├── admin.py        # Реєстрація в адмін-панелі
  ├── apps.py         # Конфіг додатку
  ├── models.py       # Моделі даних
  ├── tests.py        # Тести
  ├── urls.py         # Маршрути додатку
  └── views.py        # Логіка оброблення запитів
```

## Структура settings.py

Головний файл конфігурації `autocheck_api/settings.py`:

```python
import os
from pathlib import Path

# Базова папка проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ (не публікувати в git!)
SECRET_KEY = 'your-secret-key-here'

# Режим розробки
DEBUG = True

# Дозволені хости
ALLOWED_HOSTS = ['*']

# Встановлені додатки
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # REST Framework для API
    'rest_framework',
    'corsheaders',
    
    # Наші додатки
    'cars.apps.CarsConfig',
    'users.apps.UsersConfig',
    'frontend.apps.FrontendConfig',
]

# Middleware — обробники запитів
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ... інші middleware
]

# Конфігурація БД (за замовчуванням SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Тайм-зона та мова
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'uk-ua'
USE_I18N = True

# Static файли (CSS, JS, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Первий запуск

```bash
# Створити таблиці БД
python manage.py migrate

# Запустити сервер розробки
python manage.py runserver
```

По замовчуванню: http://127.0.0.1:8000/

## Архітектура Django додатку

Django слідує **MVT паттерну** (Model-View-Template):

```
User Request
     ↓
  URLs (маршрутизація)
     ↓
  Views (обробка логіки)
     ↓
  Models (робота з даними)
     ↓
Database (SQLite/PostgreSQL)
     ↓
  Templates (HTML)
     ↓
  Response (відповідь клієнту)
```

Для **REST API** замість Template використовуємо **Serializers**.

## Основні команди Django

```bash
# Створити нову миграцію
python manage.py makemigrations

# Застосувати миграції
python manage.py migrate

# Запустити тести
python manage.py test

# Створити суперкористувача для адміна
python manage.py createsuperuser

# Запустити shell (interactive Python)
python manage.py shell

# Збрати static файли
python manage.py collectstatic

# Очистити базу даних
python manage.py flush
```

## Що буде у проекті Car Service

До кінця 9 лекцій ми матимемо:

✅ **Лекція 1**: Проект створений, структура налаштована
✅ **Лекція 2**: URL маршрути та базові views
✅ **Лекція 3**: Frontend шаблони (якщо потрібні)
✅ **Лекція 4**: Форми для CRUD операцій
✅ **Лекція 5**: Моделі (Car, Brand, Model, User)
✅ **Лекція 6**: Робота з ORM, фільтрація, пошук
✅ **Лекція 7**: REST Framework, serializers, API viewsets
✅ **Лекція 8**: Аутентифікація, дозволи, CORS
✅ **Лекція 9**: Развертування на сервер

## Домашнє завдання

1. Встановіть Django та створіть проект `autocheck_api`
2. Створіть три додатки: `cars`, `users`, `frontend`
3. Виконайте `python manage.py migrate`
4. Запустіть сервер та перевірте http://127.0.0.1:8000/
5. Створіть суперкористувача та зайдіть в http://127.0.0.1:8000/admin/

## Контрольні питання

1. Чим відрізняється Django від Flask?
2. Що входить в структуру Django проекту?
3. Для чого потрібні migrations?
4. Як активувати віртуальне середовище на Windows?
5. Що таке INSTALLED_APPS в settings.py?

## Посилання

- [Django документація](https://docs.djangoproject.com/)
- [Django для початківців](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Наш проект на GitHub](https://github.com/alex-pancho/car_service_api_and_ui)
