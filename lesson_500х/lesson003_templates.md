# Лекція 3: Templates та Rendering

## Що таке Templates в Django?

Template — це HTML файл з вбудованою Django логікою для динамічного генерування контенту. Дозволяє відокремити дизайн від логіки програми.

**Важливо**: Для REST API обично не потрібні традиційні HTML templates, але вони корисні для:
- Фронтенд сторінок проекту
- Документації API (Swagger, ReDoc)
- Email повідомлень

## Структура Template системи

### 1. Налаштування шляху до templates в settings.py

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Глобальні templates
        ],
        'APP_DIRS': True,  # Шукати templates в додатках
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2. Структура папок проекту

```
car_service_api_and_ui/
├── templates/              # Глобальні templates
│   ├── base.html          # Base template
│   ├── navbar.html        # Навігація
│   └── swagger.html       # Swagger документація
├── cars/
│   └── templates/cars/    # Templates додатку cars
│       ├── car_list.html  # Список машин
│       └── car_detail.html
├── frontend/
│   └── templates/frontend/
│       ├── index.html     # Головна сторінка
│       └── cars.html      # Сторінка машин
└── users/
    └── templates/users/
        ├── signup.html
        └── login.html
```

## Синтаксис Django Templates

### 1. Змінні {{ }}

```html
<h1>{{ title }}</h1>
<p>Car: {{ car.brand }} {{ car.model }}</p>
<p>Year: {{ car.year }}</p>
```

Передача в view:

```python
from django.shortcuts import render
from .models import Car

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'cars/car_detail.html', {
        'title': 'Car Details',
        'car': car,
    })
```

### 2. Теги {% %}

#### Умовний оператор if

```html
{% if car.year > 2020 %}
    <span class="badge">Modern</span>
{% elif car.year > 2015 %}
    <span class="badge">Old</span>
{% else %}
    <span class="badge">Very Old</span>
{% endif %}
```

#### Цикл for

```html
<ul>
    {% for car in cars %}
        <li>
            {{ car.brand.name }} 
            {{ car.model.name }} 
            ({{ car.year }})
        </li>
    {% empty %}
        <li>No cars found</li>
    {% endfor %}
</ul>
```

#### URL посилання

```html
<!-- URL маршрутом -->
<a href="{% url 'cars:car_detail' car.id %}">
    View Details
</a>

<!-- За назвою -->
<a href="{% url 'admin:index' %}">Admin Panel</a>
```

#### Фільтри |

```html
<!-- Перетворення першої букви у верхню -->
<h1>{{ title|title }}</h1>

<!-- Перетворення у верхні букви -->
<p>Brand: {{ car.brand.name|upper }}</p>

<!-- Додання значення -->
<p>Price + tax: {{ car.price|add:100 }}</p>

<!-- Довжина списку -->
<p>Total cars: {{ cars|length }}</p>

<!-- Стандартне значення -->
<p>Owner: {{ car.owner|default:"Anonymous" }}</p>

<!-- Укорочення тексту -->
<p>{{ description|truncatewords:10 }}</p>

<!-- Форматування дати -->
<p>Created: {{ car.created_at|date:"d.m.Y H:i" }}</p>
```

### 3. Коментарі {# #}

```html
{# Це коментар, не буде видимо у HTML #}
{% comment %}
    Багаторядковий коментар
    Корисний для знімання блоків коду
{% endcomment %}
```

## Наслідування Templates (Template Inheritance)

### Base Template (templates/base.html)

```html
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>{% block title %}Car Service API{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; }
        nav { background: #333; color: white; padding: 1em; }
        nav a { color: white; margin-right: 2em; text-decoration: none; }
        nav a:hover { text-decoration: underline; }
        .container { max-width: 1200px; margin: 0 auto; padding: 2em; }
    </style>
</head>
<body>
    <nav>
        <h1>Car Service</h1>
        <a href="{% url 'frontend:index' %}">Home</a>
        <a href="{% url 'cars:car_list' %}">Cars</a>
        <a href="/swagger/">API Docs</a>
        {% if user.is_authenticated %}
            <a href="{% url 'users:logout' %}">Logout</a>
        {% else %}
            <a href="{% url 'users:signup' %}">Sign Up</a>
            <a href="{% url 'users:login' %}">Login</a>
        {% endif %}
    </nav>
    
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    
    <footer>
        <p>&copy; 2024 Car Service API</p>
    </footer>
</body>
</html>
```

### Child Template (frontend/templates/frontend/index.html)

```html
{% extends 'base.html' %}

{% block title %}Home - Car Service API{% endblock %}

{% block content %}
    <h2>Welcome to Car Service!</h2>
    <p>Manage your cars and maintenance records.</p>
    
    <h3>Quick Links</h3>
    <ul>
        <li><a href="{% url 'cars:car_list' %}">View All Cars</a></li>
        <li><a href="{% url 'cars:car_create' %}">Add New Car</a></li>
        <li><a href="/api/cars/">REST API</a></li>
    </ul>
{% endblock %}
```

### Car List Template (cars/templates/cars/car_list.html)

```html
{% extends 'base.html' %}

{% block title %}Cars - Car Service API{% endblock %}

{% block content %}
    <h2>Cars</h2>
    
    <a href="{% url 'cars:car_create' %}" class="btn">Add New Car</a>
    
    <table border="1" style="width: 100%; margin-top: 2em;">
        <thead>
            <tr>
                <th>Brand</th>
                <th>Model</th>
                <th>Year</th>
                <th>Owner</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for car in cars %}
                <tr>
                    <td>{{ car.brand.name }}</td>
                    <td>{{ car.model.name }}</td>
                    <td>{{ car.year }}</td>
                    <td>{{ car.owner.username }}</td>
                    <td>
                        <a href="{% url 'cars:car_detail' car.id %}">View</a>
                        <a href="{% url 'cars:car_update' car.id %}">Edit</a>
                        <a href="{% url 'cars:car_delete' car.id %}">Delete</a>
                    </td>
                </tr>
            {% empty %}
                <tr>
                    <td colspan="5" align="center">No cars found</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```

### Car Detail Template (cars/templates/cars/car_detail.html)

```html
{% extends 'base.html' %}

{% block title %}{{ car.brand }} {{ car.model }} - Car Service API{% endblock %}

{% block content %}
    <h2>{{ car.brand.name }} {{ car.model.name }}</h2>
    
    <div class="car-details">
        <p><strong>Year:</strong> {{ car.year }}</p>
        <p><strong>Owner:</strong> {{ car.owner.username }}</p>
        {% if car.description %}
            <p><strong>Description:</strong> {{ car.description }}</p>
        {% endif %}
        <p><strong>Created:</strong> {{ car.created_at|date:"d.m.Y" }}</p>
    </div>
    
    <div class="actions" style="margin-top: 2em;">
        <a href="{% url 'cars:car_update' car.id %}" class="btn">Edit</a>
        <a href="{% url 'cars:car_delete' car.id %}" class="btn btn-danger">Delete</a>
        <a href="{% url 'cars:car_list' %}" class="btn">Back</a>
    </div>
{% endblock %}
```

## Template Tags для авторизації

```html
<!-- Перевірка авторизації -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <p>Email: {{ user.email }}</p>
{% else %}
    <p><a href="{% url 'users:login' %}">Please log in</a></p>
{% endif %}

<!-- Перевірка наявності дозволу -->
{% if user.has_perm 'cars.change_car' %}
    <a href="{% url 'cars:car_update' car.id %}">Edit</a>
{% endif %}

<!-- Перевірка групи користувача -->
{% if user.groups.all|length > 0 %}
    <p>Groups: {{ user.groups.all|join:", " }}</p>
{% endif %}
```

## Статичні файли (CSS, JS, Images)

### 1. Налаштування в settings.py

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### 2. Структура папок

```
project/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── img/
│       └── logo.png
└── templates/
    └── base.html
```

### 3. Використання в templates

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'img/logo.png' %}" alt="Logo">
    <script src="{% static 'js/app.js' %}"></script>
</body>
</html>
```

## Views з Templates (Function-Based)

```python
from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {
        'cars': cars,
    })

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {
        'car': car,
    })
```

## Generic Views для Templates

Django надає готові generic views для шаблонних операцій:

```python
from django.views.generic import ListView, DetailView
from .models import Car

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 20

class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'
```

## Context Processors

Додають дані до всіх templates:

```python
# cars/context_processors.py
from .models import Brand

def brands(request):
    return {
        'all_brands': Brand.objects.all()
    }
```

Реєстрація в settings.py:

```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ...
                'cars.context_processors.brands',
            ],
        },
    },
]
```

Використання в template:

```html
<select>
    {% for brand in all_brands %}
        <option>{{ brand.name }}</option>
    {% endfor %}
</select>
```

## Middleware для Templates

Додає глобальні змінні до всіх views:

```python
# core/middleware.py
class AppInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        request.app_name = 'Car Service API'
        request.version = '1.0.0'
        response = self.get_response(request)
        return response
```

Реєстрація в settings.py:

```python
MIDDLEWARE = [
    # ...
    'core.middleware.AppInfoMiddleware',
]
```

## Домашнє завдання

1. Створіть `templates/base.html` з навігацією
2. Створіть `frontend/templates/frontend/index.html` (homepage)
3. Створіть `cars/templates/cars/car_list.html` та `car_detail.html`
4. Реалізуйте функції views для render templates
5. Налаштуйте статичні файли (CSS)
6. Протестуйте за http://127.0.0.1:8000/

## Контрольні питання

1. Як передати дані з view в template?
2. Як використовувати цикл у template?
3. Що таке template inheritance?
4. Як посилатися на URL в template?
5. Як працюють static файли в Django?

## Посилання

- [Django Template Language](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Built-in Template Tags](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
- [Static Files Management](https://docs.djangoproject.com/en/stable/howto/static-files/)
