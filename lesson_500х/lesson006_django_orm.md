# Лекція 6: Django ORM (Object-Relational Mapping)

## Що таке ORM?

ORM — це прошарок, що дозволяє працювати з базою даних через Python об'єкти замість SQL запитів.

**Переваги:**
- Безпека (SQL Injection захист)
- Простота (Python замість SQL)
- Переносимість (SQLite → PostgreSQL без змін коду)
- Читабельність

## QuerySet - основний інструмент

QuerySet — це об'єкт, що представляє набір записів з БД. Він **ліниво виконується** (лише при необхідності).

```python
# Це не виконує запит до БД!
cars = Car.objects.filter(brand__name='Toyota')

# Запит виконується тільки тут:
for car in cars:  # Ітерація
    print(car)

car = cars[0]  # Індексування
count = cars.count()  # Підрахунок
```

## Основні QuerySet операції

### 1. Фільтрація - filter()

```python
from .models import Car

# Точна відповідність
toyota_cars = Car.objects.filter(brand__name='Toyota')

# Кілька умов (AND)
new_toyotas = Car.objects.filter(
    brand__name='Toyota',
    year__gte=2020
)

# Зворотна фільтрація
not_toyota = Car.objects.exclude(brand__name='Toyota')

# Комбінація фільтрів
cars = Car.objects.filter(
    brand__name='Toyota'
).exclude(
    year__lt=2015
)
```

### 2. Пошук - get()

```python
# Отримати один запис
car = Car.objects.get(id=1)

# З винятком, якщо не знайдено
try:
    car = Car.objects.get(license_plate='ABC123')
except Car.DoesNotExist:
    print("Car not found")

# Безпечне отримання (повертає None)
car = Car.objects.filter(id=999).first()
```

### 3. Сортування - order_by()

```python
# За датою (від новіших)
recent = Car.objects.order_by('-created_at')

# За кількома полями
by_brand_year = Car.objects.order_by('brand__name', '-year')

# Випадковий порядок
import random
random_car = Car.objects.all().order_by('?').first()

# Видалення сортування
cars = Car.objects.order_by('-created_at').order_by()
```

### 4. Обмеження - slice та limit

```python
# Перші 5 записів
top_5 = Car.objects.all()[:5]

# З 5 по 10 (пагінація)
middle = Car.objects.all()[5:10]

# Без обмеження
cars = Car.objects.all()[:None]

# Останній запис
last = Car.objects.all()[:1]  # QuerySet
last = Car.objects.all().last()  # Об'єкт
```

### 5. Підрахунок - count()

```python
total = Car.objects.count()
toyota_count = Car.objects.filter(brand__name='Toyota').count()

# exists() - більш ефективний для перевірки
has_cars = Car.objects.filter(brand__name='Toyota').exists()
```

## Поля з зв'язками - related lookups

Django ORM дозволяє переходити через зв'язки за допомогою `__`:

### 1. ForeignKey

```python
# Машини марки Toyota
toyota_cars = Car.objects.filter(brand__name='Toyota')

# Машини користувача з id=5
user_cars = Car.objects.filter(owner__id=5)
user_cars = Car.objects.filter(owner__username='john')

# Машини користувачів із email, що містить 'gmail'
gmail_users = Car.objects.filter(owner__email__icontains='gmail.com')
```

### 2. Зворотний пошук (Reverse Relations)

```python
# Марка з усіма її машинами
brand = Brand.objects.get(name='Toyota')
brand.car_set.all()  # Обидва способи працюють
# або (так як у Brand вказано related_name='cars')
brand.cars.all()

# Фільтрація через зворотний зв'язок
brands_with_cars = Brand.objects.filter(cars__owner__username='john')
```

## Lookup операції (умови пошуку)

```python
from .models import Car
from datetime import datetime, timedelta

# Точна відповідність
Car.objects.filter(year=2024)
Car.objects.filter(year__exact=2024)  # те саме

# Неточна (case-insensitive)
Car.objects.filter(brand__name__iexact='toyota')

# Більше / Менше
Car.objects.filter(year__gt=2020)     # >
Car.objects.filter(year__gte=2020)    # >=
Car.objects.filter(year__lt=2020)     # <
Car.objects.filter(year__lte=2020)    # <=

# Містить (case-sensitive)
Car.objects.filter(description__contains='diesel')

# Містить (case-insensitive)
Car.objects.filter(description__icontains='diesel')

# У списку
Car.objects.filter(year__in=[2020, 2021, 2022])

# Стартує з
Car.objects.filter(license_plate__startswith='AA')
Car.objects.filter(license_plate__istartswith='aa')  # case-insensitive

# Закінчується на
Car.objects.filter(vin__endswith='XYZ')

# Дата (найчастіше)
today = datetime.now().date()
yesterday = today - timedelta(days=1)

Car.objects.filter(created_at__date=today)
Car.objects.filter(created_at__year=2024)
Car.objects.filter(created_at__month=1)
Car.objects.filter(created_at__day=15)
Car.objects.filter(created_at__range=[yesterday, today])

# Null перевірка
Car.objects.filter(description__isnull=True)
Car.objects.exclude(description__isnull=True)
```

## Values і Aggregation

### Values - отримати словники замість об'єктів

```python
# Отримати тільки id та year
cars_data = Car.objects.values('id', 'year', 'brand__name')
# [{'id': 1, 'year': 2024, 'brand__name': 'Toyota'}, ...]

# Distinct - унікальні значення
brands = Car.objects.values('brand__name').distinct()

# Values з анотацією
from django.db.models import Count
cars_with_count = Car.objects.values('owner').annotate(
    car_count=Count('id')
)
# [{'owner': 1, 'car_count': 3}, {'owner': 2, 'car_count': 1}]
```

### Aggregation - обчислення

```python
from django.db.models import Count, Sum, Avg, Max, Min

# Count - підрахунок
total = Car.objects.aggregate(Count('id'))['id__count']

# Average - середнє
avg_year = Car.objects.aggregate(Avg('year'))['year__avg']

# Max / Min
newest = Car.objects.aggregate(Max('year'))['year__max']
oldest = Car.objects.aggregate(Min('year'))['year__min']

# Кілька разом
stats = Car.objects.aggregate(
    total_cars=Count('id'),
    avg_year=Avg('year'),
    newest=Max('year')
)
# {'total_cars': 50, 'avg_year': 2015.5, 'newest': 2024}
```

### Group By

```python
from django.db.models import Count

# Кількість машин на користувача
user_cars = Car.objects.values('owner__username').annotate(
    count=Count('id')
).order_by('-count')

# [{'owner__username': 'john', 'count': 5}, 
#  {'owner__username': 'jane', 'count': 3}]

# Середній рік по марках
brand_stats = Car.objects.values('brand__name').annotate(
    avg_year=Avg('year'),
    total=Count('id')
).order_by('-total')
```

## Distinct

```python
# Унікальні марки
brands = Car.objects.values_list('brand__name', flat=True).distinct()

# Унікальні записи з певних полів
unique_owners = Car.objects.values('owner').distinct()
```

## Select Related та Prefetch Related

Ці методи вирішують проблему N+1 запитів:

### Select Related (для ForeignKey)

```python
# БЕЗ select_related - 51 запит до БД!
cars = Car.objects.all()
for car in cars:
    print(car.brand.name)  # Запит для кожної машини

# З select_related - 1 запит
cars = Car.objects.select_related('brand', 'owner').all()
for car in cars:
    print(car.brand.name)  # БЕЗ запиту
```

### Prefetch Related (для ManyToMany та зворотних зв'язків)

```python
from django.db.models import Prefetch

# БЕЗ prefetch_related - 26 запитів
brands = Brand.objects.all()
for brand in brands:
    cars = brand.cars.all()  # Запит для кожної марки

# З prefetch_related - 2 запити
brands = Brand.objects.prefetch_related('cars').all()
for brand in brands:
    cars = brand.cars.all()  # БЕЗ запиту
```

## Batch операції

### Масове створення

```python
# Неефективно - багато запитів
for car in cars_data:
    Car.objects.create(**car)

# Ефективно - один запит
Car.objects.bulk_create([
    Car(brand_id=1, model_id=1, year=2024),
    Car(brand_id=2, model_id=3, year=2023),
    Car(brand_id=1, model_id=2, year=2022),
])
```

### Масове оновлення

```python
# Оновити всі машини Toyota
Car.objects.filter(brand__name='Toyota').update(is_active=False)

# Масовое оновлення з умовою
from django.db.models import Case, When, F, Value

Car.objects.all().update(
    is_active=Case(
        When(year__lt=2010, then=Value(False)),
        default=Value(True)
    )
)
```

### Масове видалення

```python
# Видалити старі машини
Car.objects.filter(year__lt=2000).delete()

# Видалити всі машини користувача
Car.objects.filter(owner__username='john').delete()
```

## F expressions (обчислення у БД)

```python
from django.db.models import F, ExpressionWrapper, FloatField

# Збільшити вік машини на 1
Car.objects.all().update(year=F('year') - 1)

# Порівняння полів
old_cars = Car.objects.filter(
    year__lt=2020
)

# Обчислення у фільтрі
recent_cars = Car.objects.annotate(
    age=F('year') - 2024
).filter(age__lt=-10)
```

## Raw SQL (коли ORM недостатньо)

```python
# Raw запит
cars = Car.objects.raw(
    'SELECT * FROM cars_car WHERE year > %s',
    [2020]
)

# Raw SQL без ORM моделі
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute('SELECT COUNT(*) FROM cars_car')
    row = cursor.fetchone()
    print(f"Total cars: {row[0]}")
```

## Практичні приклади для Car Service

### 1. Пошук машин

```python
def search_cars(request):
    brand = request.GET.get('brand')
    year_from = request.GET.get('year_from')
    year_to = request.GET.get('year_to')
    
    cars = Car.objects.select_related('brand', 'owner')
    
    if brand:
        cars = cars.filter(brand__name__icontains=brand)
    
    if year_from:
        cars = cars.filter(year__gte=year_from)
    
    if year_to:
        cars = cars.filter(year__lte=year_to)
    
    return cars.order_by('-created_at')
```

### 2. Рейтинг користувачів

```python
from django.db.models import Count

# Топ користувачів за кількістю машин
top_users = Car.objects.values('owner__username', 'owner__email').annotate(
    car_count=Count('id')
).order_by('-car_count')[:10]
```

### 3. Статистика по маркам

```python
from django.db.models import Count, Avg

# Статистика по кожній марці
brand_stats = Car.objects.values('brand__name').annotate(
    total_cars=Count('id'),
    avg_year=Avg('year'),
    newest=Max('year'),
    oldest=Min('year')
).order_by('-total_cars')
```

### 4. Видалення неактивних записів

```python
from datetime import timedelta
from django.utils import timezone

# Видалити машини, які не оновлювались більше року
one_year_ago = timezone.now() - timedelta(days=365)
Car.objects.filter(
    updated_at__lt=one_year_ago,
    is_active=False
).delete()
```

## Домашнє завдання

1. Використайте Django shell для практики:
   ```bash
   python manage.py shell
   ```

2. Виконайте запити:
   - Отримайте всі машини марки Toyota
   - Знайдіть машини року 2024
   - Порахуйте кількість машин на користувача
   - Знайдіть найстарішу машину
   - Отримайте середній рік випуску

3. Оптимізуйте запити для views используючи select_related

## Контрольні питання

1. Що таке QuerySet?
2. Яка різниця між filter() та get()?
3. Чому потрібні select_related та prefetch_related?
4. Як використовувати lookup операції?
5. Коли використовувати raw SQL?

## Посилання

- [QuerySet API Reference](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Field lookups](https://docs.djangoproject.com/en/stable/ref/models/querysets/#field-lookups)
- [Database access optimization](https://docs.djangoproject.com/en/stable/topics/db/optimization/)
