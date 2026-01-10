# Лекція 10: Підсумковий урок - Розбір, доопрацювання та деплой проекту

## Вступ

На цьому уроці ми об'єднаємо всі знання з попередніх 9 лекцій, щоб завершити реальний проект. Ми буде працювати на проекті **car_service_api_and_ui** та реалізуємо новий функціонал: **управління роботами/обслуговуванням машини** з полями вартості та оплати.

Цей урок максимально наближений до реальної розробки: від написання коду до PR і production deployment.

## 1. Аналіз поточної структури проекту

### Типова структура car_service_api_and_ui

```
car_service_api_and_ui/
├── autocheck_api/              # Головний Django проект
│   ├── settings.py             # Конфігурація
│   ├── urls.py                 # Головна маршрутизація
│   ├── wsgi.py
│   └── asgi.py
│
├── cars/                        # Django додаток для машин
│   ├── migrations/
│   ├── models.py               # Car, Brand, Model
│   ├── serializers.py          # CarSerializer, BrandSerializer
│   ├── views.py                # CarViewSet
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/cars/
│
├── users/                       # Django додаток для користувачів
│   ├── models.py               # Розширення User
│   ├── serializers.py
│   ├── views.py                # SignupView, SigninView
│   ├── auth_urls.py
│   └── templates/users/
│
├── services/                    # Новий додаток - РОБОТИ/ОБСЛУГОВУВАННЯ
│   ├── models.py               # Work, Service (ЛІ СТВОРИМО)
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── templates/services/
│
├── frontend/                    # UI сторінки
│   ├── views.py
│   ├── urls.py
│   └── templates/frontend/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Основні сутності домену

Поточні моделі:
- **Car** — машина користувача
- **Brand** — марка авто (Toyota, BMW, тощо)
- **Model** — модель авто (Camry, 3 Series)
- **User** — користувач системи

Нові моделі, які створимо:
- **Service** — тип обслуговування (заміна масла, шини, тощо)
- **Work** — виконана робота на машині з вартістю та статусом оплати

## 2. Бізнес-вимоги та постановка задачі

### Що нам потрібно реалізувати

Автосервіс потребує відстеження роботи, виконаної на машині:

1. **Створювати записи про роботу** — які роботи виконувались на машині
2. **Вартість роботи** — скільки вона коштує
3. **Статус оплати** — оплачено або ні
4. **Переглядати неоплачені роботи** — щоб знати заборгованість клієнта

### API вимоги

```
GET    /api/services/                 - список типів обслуговування
GET    /api/works/                    - список робіт
POST   /api/works/                    - створити роботу
GET    /api/works/{id}/               - деталі роботи
PATCH  /api/works/{id}/               - оновити роботу (вартість, статус оплати)
DELETE /api/works/{id}/               - видалити роботу

GET    /api/works/?is_paid=false      - фільтр: тільки неоплачені роботи
GET    /api/works/?car={car_id}       - фільтр: роботи для конкретної машини
```

### UI вимоги

- Форма для створення роботи (добір машини, тип роботи, вартість, checkbox оплати)
- Таблиця робіт з можливістю редагування статусу оплати
- Фільтр для перегляду неоплачених робіт
- Виведення загальної вартості робіт для машини

## 3. Креація нового додатку

### Крок 1: Створити додаток services

```bash
python manage.py startapp services
```

### Крок 2: Реєструємо в settings.py

```python
# autocheck_api/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
    
    'cars.apps.CarsConfig',
    'users.apps.UsersConfig',
    'frontend.apps.FrontendConfig',
    'services.apps.ServicesConfig',  # ← НОВИЙ ДОДАТОК
]
```

## 4. Моделювання: створення Work та Service

### services/models.py

```python
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from cars.models import Car

class Service(models.Model):
    """Тип обслуговування (заміна масла, шини, тощо)"""
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Назва типу обслуговування"
    )
    description = models.TextField(
        blank=True,
        help_text="Детальний опис"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        null=True,
        blank=True,
        help_text="Орієнтовна вартість"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Work(models.Model):
    """Виконана робота на машині"""
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='works',
        help_text="Машина, на якій виконана робота"
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='works',
        help_text="Тип обслуговування"
    )
    description = models.TextField(
        help_text="Деталі виконаної роботи"
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text="Вартість роботи"
    )
    is_paid = models.BooleanField(
        default=False,
        help_text="Чи оплачена робота"
    )
    paid_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Дата оплати"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['car', '-created_at']),
            models.Index(fields=['is_paid']),
        ]
        permissions = [
            ('can_mark_paid', 'Can mark work as paid'),
        ]
    
    def __str__(self):
        return f"{self.car} - {self.service or self.description} ({self.cost})"
    
    def mark_as_paid(self):
        """Позначити роботу як оплачену"""
        from django.utils import timezone
        self.is_paid = True
        self.paid_at = timezone.now()
        self.save()


class Invoice(models.Model):
    """Рахунок для клієнта (опціонально - для складних потреб)"""
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='invoices'
    )
    works = models.ManyToManyField(Work)
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Загальна вартість"
    )
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    
    def __str__(self):
        return f"Invoice {self.id} - {self.car}"
```

### Ключові моменти моделей:

- **DecimalField** — правильний вибір для грошей (точність вищої за Float)
- **MinValueValidator** — валідація на уровні БД (вартість > 0)
- **ForeignKey** з `related_name` — зручні зворотні посилання
- **Meta.permissions** — нові дозволи
- **mark_as_paid()** — бізнес-логіка при оплаті

## 5. Міграції та застосування до БД

### Крок 1: Створити міграції

```bash
python manage.py makemigrations services
```

Це створить файл `services/migrations/0001_initial.py`:

```python
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
from decimal import Decimal

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('cars', '0001_initial'),  # Залежність від cars
    ]
    
    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(Decimal('0.01'))])),
                ('is_paid', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='cars.car')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='services.service')),
            ],
        ),
    ]
```

### Крок 2: Застосувати міграції

```bash
python manage.py migrate
```

**Важливо**: це створить таблиці в БД. На production це **КРИТИЧНО** — забування migrate призводить до помилок!

### Крок 3: Перевірити міграції

```bash
python manage.py showmigrations services
# services
#  [X] 0001_initial
```

## 6. Серіалізатори для REST API

### services/serializers.py

```python
from rest_framework import serializers
from .models import Service, Work, Invoice
from cars.serializers import CarSerializer

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id', 'name', 'description', 'price', 
            'is_active', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class WorkSerializer(serializers.ModelSerializer):
    # Для читання (вложена інформація про машину та сервіс)
    car_detail = CarSerializer(source='car', read_only=True)
    service_name = serializers.CharField(
        source='service.name',
        read_only=True
    )
    
    # Для запису (приймаємо тільки ID)
    car_id = serializers.IntegerField(write_only=True)
    service_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Work
        fields = [
            'id', 'car', 'car_id', 'car_detail',
            'service', 'service_id', 'service_name',
            'description', 'cost', 'is_paid', 'paid_at',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'paid_at', 'created_at', 'updated_at']
    
    def validate_cost(self, value):
        """Валідація вартості"""
        if value <= 0:
            raise serializers.ValidationError(
                "Вартість повинна бути більше за 0"
            )
        return value
    
    def validate(self, data):
        """Перевірка логіки"""
        # Перевіріть що машина існує
        car_id = data.get('car_id')
        from cars.models import Car
        try:
            Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            raise serializers.ValidationError(
                {'car_id': 'Машина не знайдена'}
            )
        return data
    
    def create(self, validated_data):
        """Створення Work з ID замість об'єкту"""
        car_id = validated_data.pop('car_id')
        service_id = validated_data.pop('service_id', None)
        
        from cars.models import Car
        car = Car.objects.get(id=car_id)
        
        work = Work.objects.create(car=car, **validated_data)
        
        if service_id:
            work.service_id = service_id
            work.save()
        
        return work


class WorkListSerializer(serializers.ModelSerializer):
    """Спрощений серіалізер для списків"""
    car_brand = serializers.CharField(
        source='car.brand.name',
        read_only=True
    )
    car_model = serializers.CharField(
        source='car.model.name',
        read_only=True
    )
    
    class Meta:
        model = Work
        fields = [
            'id', 'car', 'car_brand', 'car_model',
            'description', 'cost', 'is_paid', 'created_at'
        ]


class InvoiceSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)
    work_ids = serializers.PrimaryKeyRelatedField(
        queryset=Work.objects.all(),
        many=True,
        write_only=True
    )
    
    class Meta:
        model = Invoice
        fields = [
            'id', 'car', 'works', 'work_ids',
            'total_cost', 'is_paid', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
```

## 7. Views / ViewSets для REST API

### services/views.py

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Service, Work, Invoice
from .serializers import (
    ServiceSerializer, WorkSerializer, WorkListSerializer,
    InvoiceSerializer
)
from cars.permissions import IsOwnerOrReadOnly


class ServiceViewSet(viewsets.ModelViewSet):
    """API для типів обслуговування"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering = ['name']


class WorkViewSet(viewsets.ModelViewSet):
    """API для робіт"""
    queryset = Work.objects.select_related('car', 'service')
    permission_classes = [IsAuthenticated]
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ['car', 'is_paid']
    search_fields = ['description', 'car__brand__name', 'service__name']
    ordering_fields = ['created_at', 'cost']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Використовувати спрощений серіалізер для списків"""
        if self.action == 'list':
            return WorkListSerializer
        return WorkSerializer
    
    def get_queryset(self):
        """Фільтрувати за власником машини"""
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(car__owner=user)
    
    def perform_create(self, serializer):
        """Убедитися що машина належить користувачу"""
        car_id = self.request.data.get('car_id')
        from cars.models import Car
        car = Car.objects.get(id=car_id)
        
        if car.owner != self.request.user and not self.request.user.is_staff:
            return Response(
                {'error': 'You can only create work for your cars'},
                status=status.HTTP_403_FORBIDDEN
            )
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def mark_paid(self, request, pk=None):
        """POST /api/works/{id}/mark_paid/ - Позначити оплачену"""
        work = self.get_object()
        
        # Перевірка прав
        if work.car.owner != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        work.mark_as_paid()
        
        return Response({
            'message': 'Work marked as paid',
            'work': WorkSerializer(work).data
        })
    
    @action(detail=False, methods=['get'])
    def unpaid(self, request):
        """GET /api/works/unpaid/ - Тільки неоплачені роботи"""
        unpaid_works = self.get_queryset().filter(is_paid=False)
        
        serializer = self.get_serializer(unpaid_works, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """GET /api/works/statistics/ - Статистика робіт"""
        from django.db.models import Sum, Count, Avg
        
        stats = self.get_queryset().aggregate(
            total_works=Count('id'),
            total_cost=Sum('cost'),
            paid_cost=Sum('cost', filter=Q(is_paid=True)),
            unpaid_cost=Sum('cost', filter=Q(is_paid=False)),
            average_cost=Avg('cost')
        )
        
        return Response(stats)


class InvoiceViewSet(viewsets.ModelViewSet):
    """API для рахунків"""
    queryset = Invoice.objects.select_related('car')
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = ['car', 'is_paid']
    ordering = ['-created_at']
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(car__owner=user)
```

## 8. URL маршрутизація

### services/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'works', views.WorkViewSet, basename='work')
router.register(r'invoices', views.InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls)),
]
```

### Додавання у головні urls (autocheck_api/urls.py)

```python
urlpatterns = [
    # ...
    path('api/', include('services.urls')),
    # ...
]
```

## 9. Django Forms для UI (якщо потрібен HTML фронтенд)

### services/forms.py

```python
from django import forms
from .models import Work, Service
from cars.models import Car

class WorkForm(forms.ModelForm):
    car = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Select car'
        })
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(is_active=True),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Work description'
        })
    )
    cost = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'type': 'number',
            'step': '0.01',
            'min': '0.01',
            'placeholder': '0.00'
        })
    )
    is_paid = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
    
    class Meta:
        model = Work
        fields = ['car', 'service', 'description', 'cost', 'is_paid']
```

## 10. Адмін-панель

### services/admin.py

```python
from django.contrib import admin
from .models import Service, Work, Invoice

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ['name', 'description']
        }),
        ('Price', {
            'fields': ['price']
        }),
        ('Status', {
            'fields': ['is_active']
        }),
    )

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'car', 'cost', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at', 'service']
    search_fields = ['description', 'car__brand__name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Машина', {
            'fields': ['car']
        }),
        ('Робота', {
            'fields': ['service', 'description']
        }),
        ('Вартість', {
            'fields': ['cost']
        }),
        ('Оплата', {
            'fields': ['is_paid', 'paid_at']
        }),
        ('Timestamps', {
            'fields': ['created_at', 'updated_at']
        }),
    )
    
    actions = ['mark_as_paid']
    
    def mark_as_paid(self, request, queryset):
        """Дія адміна для позначення оплачених робіт"""
        count = 0
        for work in queryset:
            if not work.is_paid:
                work.mark_as_paid()
                count += 1
        self.message_user(request, f'{count} работ позначено як оплачено')
    
    mark_as_paid.short_description = "Mark selected works as paid"

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'total_cost', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    search_fields = ['car__brand__name']
    filter_horizontal = ['works']
```

## 11. Написання тестів

### services/tests.py

```python
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from cars.models import Car, Brand, Model
from .models import Service, Work

class WorkModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'pass')
        self.brand = Brand.objects.create(name='Toyota')
        self.model = Model.objects.create(name='Camry', brand=self.brand)
        self.car = Car.objects.create(
            brand=self.brand,
            model=self.model,
            year=2024,
            owner=self.user
        )
        self.service = Service.objects.create(name='Oil Change', price=500)
    
    def test_create_work(self):
        work = Work.objects.create(
            car=self.car,
            service=self.service,
            description='Regular maintenance',
            cost=500
        )
        self.assertEqual(work.cost, 500)
        self.assertFalse(work.is_paid)
    
    def test_mark_as_paid(self):
        work = Work.objects.create(
            car=self.car,
            description='Repair',
            cost=1200
        )
        work.mark_as_paid()
        self.assertTrue(work.is_paid)
        self.assertIsNotNone(work.paid_at)
    
    def test_cost_validation(self):
        with self.assertRaises(Exception):
            Work.objects.create(
                car=self.car,
                description='Bad work',
                cost=-100  # Негативна вартість
            )


class WorkAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'pass')
        self.brand = Brand.objects.create(name='BMW')
        self.model = Model.objects.create(name='X5', brand=self.brand)
        self.car = Car.objects.create(
            brand=self.brand,
            model=self.model,
            year=2024,
            owner=self.user
        )
        self.service = Service.objects.create(name='Tire Replacement', price=2000)
        self.client.force_authenticate(user=self.user)
    
    def test_create_work_api(self):
        data = {
            'car_id': self.car.id,
            'service_id': self.service.id,
            'description': 'Replace all tires',
            'cost': '2000.00'
        }
        response = self.client.post('/api/works/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_works(self):
        Work.objects.create(
            car=self.car,
            description='Service',
            cost=1500
        )
        response = self.client.get('/api/works/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_filter_unpaid_works(self):
        Work.objects.create(car=self.car, description='Work 1', cost=500)
        work2 = Work.objects.create(car=self.car, description='Work 2', cost=300)
        work2.mark_as_paid()
        
        response = self.client.get('/api/works/?is_paid=false')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_mark_paid_action(self):
        work = Work.objects.create(
            car=self.car,
            description='Maintenance',
            cost=1000
        )
        response = self.client.post(f'/api/works/{work.id}/mark_paid/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        work.refresh_from_db()
        self.assertTrue(work.is_paid)
```

Запуск тестів:

```bash
# Всі тести
python manage.py test

# Тільки тести services
python manage.py test services

# З покриттям
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 12. Робочий процес Git та Pull Request

### Крок 1: Створити feature-гілку

```bash
# Завантажити основну гілку
git fetch origin
git pull origin main

# Створити feature-гілку
git checkout -b feature/services-work-management
```

### Крок 2: Розробка та коміти

```bash
# Коміт за логічними частинами
git add services/models.py
git commit -m "Add Service and Work models with cost and payment tracking"

git add services/serializers.py
git commit -m "Add serializers for Work, Service and Invoice"

git add services/views.py services/urls.py
git commit -m "Add API views and routing for work management"

git add services/admin.py
git commit -m "Register models in Django admin"

git add services/tests.py
git commit -m "Add comprehensive tests for Work model and API"

# Перегляд історії
git log --oneline -5
```

### Крок 3: Push у GitHub

```bash
git push origin feature/services-work-management
```

### Крок 4: Створення Pull Request

На GitHub:
1. Перейти на сторінку репозиторію
2. Натиснути "Compare & pull request"
3. Заповнити шаблон PR:

**Заголовок PR:**
```
Add work management system with cost and payment tracking
```

**Опис PR:**
```markdown
## What does this PR do?

Implements a complete work/service management system for cars:

- **New models**: Service (service types) and Work (performed work)
- **Features**:
  - Track work performed on cars with cost
  - Mark work as paid/unpaid
  - Filter unpaid works
  - Generate invoices
  - Admin interface for managing works

## What changed?

- Added `services` Django app
- Created Service and Work models with DecimalField for cost
- Added comprehensive DRF serializers and ViewSets
- Implemented API endpoints:
  - GET/POST /api/works/
  - PATCH /api/works/{id}/
  - POST /api/works/{id}/mark_paid/
  - GET /api/works/unpaid/
  - GET /api/works/statistics/
- Added Django admin interface
- Added 10+ tests covering models and API

## Testing

- All tests passing: `python manage.py test services`
- Tested API endpoints with Postman
- Verified admin interface

## Checklist

- [x] Models created and migrated
- [x] Serializers updated
- [x] Views implemented
- [x] URLs configured
- [x] Tests added
- [x] No hardcoded secrets
- [x] DEBUG = False in production
```

## 13. Код-ревью (Code Review) процес

### Як розглядає code reviewer:

Чек-лист для reviewer:

```
□ Логіка коду:
  ✓ Валідація даних (DecimalField, MinValueValidator)
  ✓ Перевірка прав доступу
  ✓ Обробка помилок
  
□ Інтеграція:
  ✓ Міграції коректні
  ✓ Serializers включають всі нові поля
  ✓ Не порушена зворотна сумісність
  
□ Тестування:
  ✓ Є unit тести
  ✓ Є integration тести
  ✓ Покриття > 80%
  
□ Безпека:
  ✓ Немає SQL injection
  ✓ Дозволи перевірені
  ✓ Немає SECRET_KEY у коді
  
□ Документація:
  ✓ Docstrings в функціях
  ✓ Models документовані
```

## 14. Підготовка до production deployment

### Крок 1: Оновлення requirements.txt

```bash
pip freeze > requirements.txt
```

### Крок 2: Production checklist

```python
# settings.py для production

DEBUG = config('DEBUG', default=False, cast=bool)

# HTTPS
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# Static файли
STATIC_ROOT = '/var/www/car_service/staticfiles'

# БД на PostgreSQL
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
```

### Крок 3: Локальне тестування з production налаштуванням

```bash
# .env для локального production тестування
DEBUG=False
SECRET_KEY=test-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Запуск перевірок
python manage.py check --deploy

# Збирання static файлів
python manage.py collectstatic --noinput

# Запуск тестів
python manage.py test

# Запуск сервера локально
gunicorn autocheck_api.wsgi:application --bind 0.0.0.0:8000
```

## 15. Розгортання на production

### Крок 1: Merge PR до main

```bash
# На GitHub: натиснути "Merge pull request"
# Або через Git CLI:
git checkout main
git pull origin main
git pull origin feature/services-work-management
git push origin main
```

### Крок 2: SSH на сервер і оновлення

```bash
ssh user@your-server.com

cd /var/www/car_service

# Завантажити оновлення
git pull origin main

# Активувати venv
source venv/bin/activate

# Встановити нові залежності
pip install -r requirements.txt

# Зробити міграції
python manage.py migrate

# Зібрати static файли
python manage.py collectstatic --noinput

# Перезапустити Gunicorn
sudo systemctl restart gunicorn

# Перезавантажити Nginx
sudo systemctl reload nginx

# Перевірити статус
sudo systemctl status gunicorn
```

### Крок 3: Перевірка логів

```bash
# Логи Gunicorn
sudo journalctl -u gunicorn -f

# Логи Nginx
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log

# Django логи
tail -f /var/log/django/debug.log
```

## 16. Тестування після deployment

### API Тестування

```bash
# Тест створення роботи
curl -X POST http://yourdomain.com/api/works/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "car_id": 1,
    "service_id": 1,
    "description": "Oil change and filter replacement",
    "cost": "1500.00",
    "is_paid": false
  }'

# Тест отримання списку
curl http://yourdomain.com/api/works/ \
  -H "Authorization: Bearer YOUR_TOKEN"

# Тест фільтрації неоплачених
curl "http://yourdomain.com/api/works/?is_paid=false" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Тест позначення як оплачена
curl -X POST http://yourdomain.com/api/works/1/mark_paid/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### UI Тестування

- Заходимо на сайт
- Переходимо на сторінку машины
- Створюємо нову роботу
- Вводимо вартість та статус оплати
- Зберігаємо
- Перевіряємо, що дані відображаються
- Редагуємо роботу
- Позначаємо як оплачену

### Перевірка БД

```bash
# На серверу в PostgreSQL консолі
sudo -u postgres psql car_service_db

# Перевірити дані
SELECT * FROM services_work LIMIT 5;
SELECT COUNT(*) as unpaid_count FROM services_work WHERE is_paid = false;
```

## 17. Моніторинг та обслуговування

### Моніторинг помилок

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
        },
    },
}
```

### Резервні копії

```bash
# Резервна копія БД
sudo -u postgres pg_dump car_service_db > /backups/car_service_$(date +%Y%m%d).sql

# Cron для автоматичного резервного копіювання
# 0 2 * * * /usr/bin/pg_dump -U car_user car_service_db > /backups/car_service_$(date +\%Y\%m\%d).sql
```

## 18. Типові помилки, яких слід уникати

### ❌ Критичні помилки

1. **Забули migrate на сервері**
   - Сервер падає з ошибкой: "no such table"
   - Рішення: `python manage.py migrate`

2. **Забули collectstatic**
   - CSS/JS не завантажуються
   - Рішення: `python manage.py collectstatic --noinput`

3. **Hardcoded SECRET_KEY у коді**
   - Будь-хто може взяти і взламати
   - Рішення: використовувати .env файл

4. **Float замість Decimal для грошей**
   - Помилки округлення: 0.1 + 0.2 = 0.30000000000000004
   - Рішення: завжди DecimalField

5. **Забули перевірити права доступу**
   - Користувач А бачить роботи користувача Б
   - Рішення: фільтрувати за owner

### ❌ Типові помилки у коді

```python
# ❌ ПОГАНО - забув валідацію
cost = models.FloatField()  # Не підходить для грошей!

# ✓ ДОБРЕ
cost = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(Decimal('0.01'))]
)

# ❌ ПОГАНО - немає перевірки прав
def get_queryset(self):
    return Work.objects.all()  # Всі бачать всім!

# ✓ ДОБРЕ
def get_queryset(self):
    user = self.request.user
    if user.is_staff:
        return Work.objects.all()
    return Work.objects.filter(car__owner=user)

# ❌ ПОГАНО - немає тестів
# Просто сподіваємось, що все працює

# ✓ ДОБРЕ
class WorkAPITest(APITestCase):
    def test_create_work_api(self):
        # Тестуємо кожен feature
```

## 19. Домашнє завдання

1. **Реалізуйте нові моделі** Service та Work з усіма полями
2. **Миграції та БД** — виконайте makemigrations та migrate
3. **Serializers** — напишіть повні серіалізатори з валідацією
4. **API Views** — реалізуйте CRUD операції та фільтри
5. **Тести** — напишіть мінімум 5 тестів
6. **Адмін-панель** — зареєструйте моделі
7. **Pull Request** — зробіть PR на GitHub з описом
8. **Локальне тестування** — перевірте API через Postman
9. **Оновлення документації** — додайте приклади у README
10. **Code Review** — потрошу коллегу переглянути ваш код

## 20. Підсумок курсу

За 10 лекцій ви вивчили:

✅ **Лекція 1-2**: Основи Django, URL маршрутизація  
✅ **Лекція 3-4**: Templates, Forms, POST запити  
✅ **Лекція 5-6**: Models, Migrations, ORM  
✅ **Лекція 7**: Django REST Framework, API  
✅ **Лекція 8**: Безпека, аутентифікація, дозволи  
✅ **Лекція 9**: Deployment, production setup  
✅ **Лекція 10**: Реальний production workflow

Тепер ви можете:
- Розробляти REST API на Django
- Організовувати код в додатки
- Писати тести та код-ревью
- Розгортати на production
- Працювати в команді з Git/GitHub

**🎓 Привіт! Ви маєте повний Django-пайплайн від ідеї до production!**

---

## Додаткові ресурси

- [Django Documentation](https://docs.djangoproject.com/)
- [DRF Documentation](https://www.django-rest-framework.org/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x/)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)
- [Full Stack Django Course](https://www.fullstackpython.com/django.html)