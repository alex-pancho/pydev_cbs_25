# Лекція 8: Безпека у Django

## Вступ до Web безпеки

Web безпека — це критична частина розробки. Django має вбудовані захисти від більшості атак.

Основні загрози:
- **SQL Injection** — введення шкідливого SQL коду
- **XSS (Cross-Site Scripting)** — введення JavaScript коду
- **CSRF (Cross-Site Request Forgery)** — підроблені запити
- **Brute Force** — перебір пароля
- **Session Hijacking** — крадіжка сесії
- **Data Exposure** — витік даних

## 1. SQL Injection захист

### Проблема (НЕБЕЗПЕЧНО!)

```python
# НИКОГДА не робіть так!
brand_name = request.GET.get('brand')
query = f"SELECT * FROM cars_car WHERE brand = '{brand_name}'"
cars = Car.objects.raw(query)

# Атакуючий може передати: brand=' OR '1'='1
# Запит стане: SELECT * FROM cars_car WHERE brand = '' OR '1'='1'
# Результат: всі машини будуть повернені!
```

### Рішення (Django ORM)

```python
# БЕЗПЕЧНО - Django автоматично екранує дані
brand_name = request.GET.get('brand')
cars = Car.objects.filter(brand__name=brand_name)  # ✓ Безпечно

# Або з параметризованим raw SQL
cars = Car.objects.raw(
    'SELECT * FROM cars_car WHERE brand = %s',
    [brand_name]  # Параметр передається окремо
)
```

**Правило**: Завжди використовуйте ORM або параметризовані запити!

## 2. XSS (Cross-Site Scripting) захист

### Проблема

```html
<!-- НЕБЕЗПЕЧНО! -->
<p>{{ user_input }}</p>

<!-- Користувач введе: <script>alert('hacked')</script> -->
<!-- Скрипт виконається! -->
```

### Рішення

```html
<!-- БЕЗПЕЧНО - Django автоматично екранує -->
<p>{{ user_input }}</p>

<!-- Виведеться як текст: <script>alert('hacked')</script> -->
```

### Вручну позначити як безпечне (якщо потрібно HTML)

```html
<!-- Якщо ви впевнені в безпеці контенту -->
<p>{{ description|safe }}</p>

<!-- Або у Python -->
from django.utils.safestring import mark_safe
safe_html = mark_safe('<strong>Bold text</strong>')
```

**Правило**: Довіряйте Django фільтрам автоматичного екранування!

## 3. CSRF (Cross-Site Request Forgery) захист

### Проблема

```
Користувач залогінений на bank.com
Користувач відкриває вкладку на evil.com
evil.com відправляє запит на bank.com від імені користувача
bank.com виконує запит (видає гроші)
```

### Рішення в HTML

```html
<!-- Всі POST форми повинні включати CSRF токен -->
<form method="post">
    {% csrf_token %}  <!-- ❌ Забув - форма не працюватиме -->
    <!-- поля форми -->
</form>
```

### Рішення в API (JSON)

```javascript
// Отримати токен з cookies або input
const token = document.querySelector('[name=csrfmiddlewaretoken]').value;

fetch('/api/cars/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': token  // Передати у заголовку
    },
    body: JSON.stringify({...})
});
```

### CSRF для API (більш сучасно)

```python
# Якщо використовується JWT, CSRF може бути вимкнено для API

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# CSRF дозволяється для звичайних форм, але ігнорується для JWT
```

## 4. Аутентифікація та сесії

### Пароль хешування

```python
from django.contrib.auth.models import User

# НЕБЕЗПЕЧНО - ніколи не зберігайте пароль у plain text!
user = User.objects.create(username='john', password='mypassword')

# ПРАВИЛЬНО - використовуйте set_password
user = User.objects.create(username='john')
user.set_password('mypassword')
user.save()
```

### Password Validators (перевірка стійкості)

```python
# settings.py - налаштовані за замовчуванням
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Кастомна валідація паролю
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

password = 'newpassword123'
try:
    validate_password(password)
except ValidationError as e:
    print(e.messages)
```

### Rate limiting (захист від brute force)

```python
# Встановити django-ratelimit
pip install django-ratelimit

# Використання
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='POST')
def login_view(request):
    # Максимум 5 спроб на IP за хвилину
    pass
```

### Таймаут сесії

```python
# settings.py
SESSION_COOKIE_AGE = 3600  # 1 година
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True  # Тільки HTTPS
SESSION_COOKIE_HTTPONLY = True  # Недоступна для JavaScript
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
```

## 5. Дозволи та Авторизація

### Django Permissions

```python
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# У models.py - кастомні дозволи
class Car(models.Model):
    # ...
    class Meta:
        permissions = [
            ('can_view_stats', 'Can view car statistics'),
            ('can_export_data', 'Can export car data'),
        ]

# Перевірка прав у view
@permission_required('cars.change_car')
def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    # ...

# У class-based view
from django.contrib.auth.mixins import PermissionRequiredMixin

class CarUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'cars.change_car'
```

### Об'єктні дозволи (на рівні об'єкта)

```python
# Встановити django-guardian
pip install django-guardian

from guardian.shortcuts import assign_perm, remove_perm, get_perms

# Дати дозвіл користувачу на конкретну машину
car = Car.objects.first()
user = User.objects.get(username='john')
assign_perm('cars.change_car', user, car)

# Видалити дозвіл
remove_perm('cars.change_car', user, car)

# Перевірити дозвіл
user.has_perm('cars.change_car', car)

# Отримати всі дозволи користувача на об'єкт
get_perms(user, car)
```

### Керування групами

```python
from django.contrib.auth.models import Group, Permission

# Створити групу
mechanics_group, created = Group.objects.get_or_create(name='Mechanics')

# Додати дозволи групі
change_car = Permission.objects.get(codename='change_car')
mechanics_group.permissions.add(change_car)

# Додати користувача до групи
user.groups.add(mechanics_group)

# Перевірити принадлежність до групи
if user.groups.filter(name='Mechanics').exists():
    print("User is a mechanic")
```

## 6. Environment Variables

### Приховування конфіденційних даних

```bash
# Встановити python-decouple
pip install python-decouple
```

```python
# settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
```

```env
# .env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DB_NAME=car_service
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

```python
# .gitignore
.env
*.pyc
__pycache__/
.venv/
db.sqlite3
```

## 7. CORS та приватність

### CORS налаштування

```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Development
    'http://localhost:5173',  # Vite
    'https://yourdomain.com',  # Production
]

# Або дозволити конкретні методи
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
```

### Headers безпеки

```python
# settings.py
SECURE_SSL_REDIRECT = True  # Перенаправити на HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 рік
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

X_FRAME_OPTIONS = 'DENY'  # Запобігти clickjacking
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
    'script-src': ("'self'", "'unsafe-inline'"),
    'style-src': ("'self'", "'unsafe-inline'"),
}
```

## 8. Логування та Аудит

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/debug.log',
        },
        'security': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/security.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'WARNING',
        },
    },
}

# Використання у коді
import logging
logger = logging.getLogger('django.security')

def login_view(request):
    logger.info(f"Login attempt from {request.META.get('REMOTE_ADDR')}")
```

## 9. API безпека

### Throttling (обмеження запитів)

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',  # Для анонімних користувачів
        'user': '1000/hour'  # Для авторизованих
    }
}

# Кастомне throttling
from rest_framework.throttling import BaseThrottle

class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return True  # Логіка throttling
```

### Input Validation

```python
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year']
    
    def validate_year(self, value):
        # Валідація діапазону
        if not (1900 <= value <= 2024):
            raise serializers.ValidationError(
                "Year must be between 1900 and 2024"
            )
        return value
    
    def validate_license_plate(self, value):
        # Валідація формату
        if value and not value.isalnum():
            raise serializers.ValidationError(
                "License plate can only contain letters and numbers"
            )
        return value.upper()
```

## 10. Чек-лист для production

```python
# settings.py для production

# Основне
DEBUG = False
SECRET_KEY = config('SECRET_KEY')  # Змінити!
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Headers
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_SECURITY_POLICY = {...}

# Дозволи
SECURE_HSTS_SECONDS = 31536000

# API
CORS_ALLOWED_ORIGINS = ['https://yourdomain.com']

# Authentication
AUTH_PASSWORD_VALIDATORS = [...]
SESSION_COOKIE_AGE = 3600

# Логування
LOGGING = {...}
```

## Домашнє завдання

1. Налаштуйте `.env` файл з конфіденційними даними
2. Додайте CSRF захист до всіх форм
3. Реалізуйте rate limiting для API
4. Налаштуйте дозволи користувачів
5. Створіть Audit logs для важливих операцій

## Контрольні питання

1. Як Django захищає від SQL Injection?
2. Що таке CSRF та як його запобігти?
3. Як правильно зберігати паролі?
4. Що таке XSS і як його запобігти?
5. Як налаштувати дозволи користувачів?

## Посилання

- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)
- [Security in Django](https://docs.djangoproject.com/en/stable/ref/middleware/csrf/)
- [Authentication](https://docs.djangoproject.com/en/stable/topics/auth/)
- [Permissions and Authorization](https://docs.djangoproject.com/en/stable/topics/auth/default/)
