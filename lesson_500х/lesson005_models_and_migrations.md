# Лекція 5: Models та Migrations

## Що таке Models в Django?

Model — це Python клас, що описує структуру таблиці в базі даних. Один Model = одна таблиця в БД.

Django автоматично генерує SQL запити, коли ви працюєте з models через Python код.

## Структура проекту Car Service

Для системи управління автосервісом потрібні моделі:

1. **Brand** (Марка автомобіля)
2. **Model** (Модель автомобіля)
3. **Car** (Автомобіль користувача)
4. **User** (Розширення Django User)

## Базові Models для Car Service

### 1. Марка і модель авто (cars/models.py)

```python
from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    """Марка автомобіля (Toyota, BMW, Mercedes)"""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Car brand name"
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Model(models.Model):
    """Модель автомобіля (Camry, 3 Series, C-Class)"""
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='models'
    )
    year_from = models.IntegerField(help_text="Production year from")
    year_to = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"
        unique_together = ['name', 'brand']
    
    def __str__(self):
        return f"{self.brand.name} {self.name}"
```

### 2. Машина користувача (cars/models.py)

```python
class Car(models.Model):
    """Автомобіль користувача"""
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    year = models.IntegerField(
        help_text="Year of manufacture"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    description = models.TextField(blank=True)
    license_plate = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    vin = models.CharField(
        max_length=17,
        unique=True,
        null=True,
        blank=True,
        help_text="Vehicle Identification Number"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['owner', '-created_at']),
            models.Index(fields=['license_plate']),
        ]
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.owner}"
    
    def get_age(self):
        """Вік машини"""
        from datetime import datetime
        return datetime.now().year - self.year
```

## Типи полів в Django

```python
# Текстові поля
CharField(max_length=100)           # Один рядок тексту
TextField()                          # Багаторядковий текст
SlugField(max_length=100)           # URL-дружний текст

# Числа
IntegerField()                       # Ціле число
FloatField()                         # Дробове число
DecimalField(max_digits=10, decimal_places=2)  # Точні дроби

# Логічні значення
BooleanField(default=True)
NullBooleanField()                  # Может бути null

# Дата та час
DateField(auto_now_add=True)        # Дата (створення)
TimeField()                          # Час
DateTimeField(auto_now=True)        # Дата і час (оновлення)

# Файли
FileField(upload_to='files/')
ImageField(upload_to='images/')

# Зв'язки
ForeignKey(OtherModel, on_delete=models.CASCADE)  # Один до багатьох
OneToOneField(OtherModel, on_delete=models.CASCADE)  # Один до одного
ManyToManyField(OtherModel)         # Багато до багатьох

# Спеціальні
EmailField()
URLField()
UUIDField()
JSONField()
```

## Параметри полів

```python
# Основні параметри
name = models.CharField(
    max_length=100,                 # Максимальна довжина
    help_text="User's full name",   # Підказка
    verbose_name="Full Name",       # Люди-зрозумла назва
    db_column='user_full_name',     # Назва колонки в БД
)

# Значення за замовчуванням
status = models.CharField(
    max_length=20,
    default='active',                # Статичне значення
    # або функція
    default=timezone.now,
)

# Унікальність та null
email = models.EmailField(
    unique=True,                    # Унікальне значення
    null=True,                      # Дозволяє NULL в БД
    blank=True,                     # Дозволяє пусто у формах
)

# Обов'язкові (за замовчуванням)
name = models.CharField(max_length=100)  # null=False, blank=False
```

##関係を持つフィールド (Відношення)

### ForeignKey (Один до багатьох)

```python
class Comment(models.Model):
    text = models.TextField()
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,      # Видалити коменти, якщо машина видалена
        related_name='comments'        # Зворотне посилання: car.comments.all()
    )

# Використання
car = Car.objects.first()
car.comments.all()  # Всі коментарі машини
```

### OneToOneField (Один до одного)

```python
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(max_length=20)

# Використання
user.profile.phone
```

### ManyToManyField (Багато до багатьох)

```python
class Service(models.Model):
    name = models.CharField(max_length=100)

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

# Використання
maintenance = Maintenance.objects.first()
maintenance.services.all()  # Всі сервіси для обслуговування
```

## Meta опції

```python
class Car(models.Model):
    # ...
    
    class Meta:
        # Людська назва (одниця)
        verbose_name = "Car"
        
        # Людська назва (множина)
        verbose_name_plural = "Cars"
        
        # Порядок за замовчуванням
        ordering = ['-created_at']  # Від новіших до старіших
        
        # Унікальність кількох полів разом
        unique_together = ['owner', 'license_plate']
        
        # Індекси для швидкого пошуку
        indexes = [
            models.Index(fields=['owner', '-created_at']),
        ]
        
        # Дозволи за замовчуванням
        permissions = [
            ('can_view_report', 'Can view car report'),
        ]
        
        # Абстрактна модель (не створює таблицю)
        abstract = True
```

## Migrations

Migration — це набір змін, які застосовуються до структури БД.

### 1. Створення migration

```bash
# Створить файли міграцій на основі змін у моделях
python manage.py makemigrations
```

Це створить файл як `migrations/0001_initial.py`:

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    
    dependencies = []
    
    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

### 2. Застосування migrations

```bash
# Застосувати всі неза-застосовані міграції
python manage.py migrate

# Застосувати конкретної додатку
python manage.py migrate cars

# Застосувати до конкретної номер міграції
python manage.py migrate cars 0003
```

### 3. Перегляд стану migrations

```bash
# Показати список всіх міграцій та їхній стан
python manage.py showmigrations

# Вивід:
# cars
#  [X] 0001_initial
#  [X] 0002_car_license_plate
#  [ ] 0003_auto_20240115_1234  # Ще не застосована
```

### 4. Скасування міграції

```bash
# Повернутися на крок назад
python manage.py migrate cars 0001
```

### 5. SQL запит міграції

```bash
# Показати SQL, який буде виконаний
python manage.py sqlmigrate cars 0001
```

## Моделі в адмін-панелі

### Реєстрація (cars/admin.py)

```python
from django.contrib import admin
from .models import Brand, Model, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'year_from', 'year_to']
    list_filter = ['brand', 'year_from']
    search_fields = ['name', 'brand__name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ['name', 'brand']
        }),
        ('Years', {
            'fields': ['year_from', 'year_to']
        }),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'license_plate', 'is_active', 'created_at']
    list_filter = ['brand', 'is_active', 'created_at']
    search_fields = ['license_plate', 'vin', 'owner__username']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Vehicle Information', {
            'fields': ['brand', 'model', 'year']
        }),
        ('Owner', {
            'fields': ['owner']
        }),
        ('Details', {
            'fields': ['license_plate', 'vin', 'description']
        }),
        ('Status', {
            'fields': ['is_active', 'created_at', 'updated_at']
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Редагування існуючого об'єкта
            return self.readonly_fields + ['brand', 'model']
        return self.readonly_fields
```

## Queryset методи

```python
from .models import Car, Brand

# Отримання всіх об'єктів
all_cars = Car.objects.all()

# Фільтрація
toyota_cars = Car.objects.filter(brand__name='Toyota')
recent_cars = Car.objects.filter(created_at__gte='2024-01-01')

# Виключення
not_toyota = Car.objects.exclude(brand__name='Toyota')

# Перший об'єкт
first_car = Car.objects.first()

# Останній об'єкт
last_car = Car.objects.last()

# Отримання за ID
car = Car.objects.get(id=1)  # Викидає DoesNotExist, якщо не знайдено

# Перевірка існування
exists = Car.objects.filter(id=1).exists()

# Кількість
count = Car.objects.count()

# Сортування
by_year = Car.objects.order_by('-year')

# Pagination
page_1 = Car.objects.all()[:10]   # Перші 10
page_2 = Car.objects.all()[10:20]  # З 10 по 20

# Select related (для ForeignKey) - запобіганню N+1
cars = Car.objects.select_related('brand', 'owner').all()

# Prefetch related (для ManyToMany)
from django.db.models import Prefetch
cars = Car.objects.prefetch_related('comments').all()

# Values (отримати словники замість об'єктів)
data = Car.objects.values('id', 'year', 'brand__name')
# [{'id': 1, 'year': 2024, 'brand__name': 'Toyota'}, ...]

# Aggregation
from django.db.models import Count, Avg, Max
brand_count = Brand.objects.all().count()
avg_year = Car.objects.aggregate(Avg('year'))['year__avg']
```

## Домашнє завдання

1. Створіть моделі `Brand`, `Model`, `Car` в `cars/models.py`
2. Виконайте `makemigrations` та `migrate`
3. Зареєструйте моделі в адмін-панелі
4. Додайте дані через адмін-панель
5. Перевірте queryset методи через Django shell:
   ```bash
   python manage.py shell
   ```

## Контрольні питання

1. Яка різниця між CharField та TextField?
2. Як створити зв'язок один-до-багатьох?
3. Для чого потрібні migrations?
4. Як скасувати міграцію?
5. Що означає `on_delete=models.CASCADE`?

## Посилання

- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Field Types](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Admin Interface](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
