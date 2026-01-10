# Лекція 2: URLs та Views

## Розуміння URL маршрутизації

URL маршрутизація — це відображення URL-адреси на функцію або клас (view), що обробить запит.

### Потік обробки запиту:

```
GET /api/cars/
    ↓
URL router шукає відповідний pattern
    ↓
Знайдена функція/клас в views.py
    ↓
View обробляє запит
    ↓
Повертає відповідь (JSON, HTML, тощо)
```

## Налаштування URL в Django

### 1. Головний urls.py (autocheck_api/urls.py)

Це основний файл маршрутизації всього проекту:

```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Адміністративна панель
    path('admin/', admin.site.urls),
    
    # API маршути
    path('api/cars/', include('cars.urls')),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('users.auth_urls')),
    
    # Документація API
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'title': 'Swagger'}
    ), name='swagger'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html'
    ), name='redoc'),
    
    # Frontend
    path('', include('frontend.urls')),
]
```

### 2. URL додатку cars (cars/urls.py)

Кожний додаток може мати свої URL маршути:

```python
from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    # Список та створення автомобілів
    path('', views.CarListCreateView.as_view(), name='car_list_create'),
    
    # Деталі, оновлення та видалення автомобіля
    path('<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    
    # Бренди та моделі
    path('brands/', views.BrandListView.as_view(), name='brand_list'),
    path('models/', views.ModelListView.as_view(), name='model_list'),
]
```

**Важливо**: `app_name` дозволяє посилатися на URL як `cars:car_list_create`.

### 3. URL користувачів (users/urls.py)

```python
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Поточний користувач
    path('current/', views.CurrentUserView.as_view(), name='current_user'),
    
    # Профіль користувача
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
```

### 4. URL аутентифікації (users/auth_urls.py)

```python
from django.urls import path
from . import auth_views

urlpatterns = [
    # Реєстрація
    path('signup/', auth_views.SignupView.as_view(), name='signup'),
    
    # Вхід
    path('signin/', auth_views.SigninView.as_view(), name='signin'),
    
    # Оновлення токену
    path('token/refresh/', auth_views.TokenRefreshView.as_view(), 
         name='token_refresh'),
]
```

## Типи URL Patterns

### 1. Із посленням рядка (string)

```python
path('cars/<str:brand>/', views.car_list_by_brand)
# Матчить: /cars/Toyota/, /cars/BMW/
```

### 2. Із цілим числом (int)

```python
path('cars/<int:pk>/', views.car_detail)
# Матчить: /cars/1/, /cars/42/
# Не матчить: /cars/abc/
```

### 3. Із слугом (slug)

```python
path('cars/<slug:slug>/', views.car_detail_slug)
# Матчить: /cars/my-car-name/, /cars/toyota-camry/
```

### 4. Із регулярними виразами (для складних правил)

```python
from django.urls import re_path

re_path(r'^cars/(?P<year>\d{4})/$', views.cars_by_year)
# Матчить: /cars/2024/, /cars/2000/
```

## Views (Представлення)

View — це функція або клас, який отримує web-запит і повертає web-відповідь.

### Типи Views:

1. **Function-based Views (FBV)** — функції
2. **Class-based Views (CBV)** — класи (краще для REST API)

## Function-Based Views (FBV)

Простий приклад для проекту Car Service:

```python
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Car, Brand

# Отримання списку автомобілів
@require_http_methods(["GET"])
def car_list(request):
    cars = Car.objects.all()
    data = [
        {
            'id': car.id,
            'brand': car.brand.name,
            'model': car.model.name,
            'year': car.year,
        }
        for car in cars
    ]
    return JsonResponse({'cars': data})

# Отримання однієї машини
@require_http_methods(["GET"])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        data = {
            'id': car.id,
            'brand': car.brand.name,
            'model': car.model.name,
            'year': car.year,
            'owner': car.owner.username,
        }
        return JsonResponse(data)
    except Car.DoesNotExist:
        return JsonResponse(
            {'error': 'Car not found'}, 
            status=404
        )

# Брендів список
@require_http_methods(["GET"])
def brand_list(request):
    brands = Brand.objects.all()
    data = [{'id': b.id, 'name': b.name} for b in brands]
    return JsonResponse({'brands': data})
```

**Проблеми FBV:**
- Грізно писати код для CRUD операцій
- Важко керувати diferentes HTTP методи (GET, POST, PUT, DELETE)
- Мало переважної кода для REST API

## Class-Based Views (CBV)

Краще підходять для REST API. Django надає готові базові класи:

### View (базовий клас)

```python
from django.views import View
from django.http import JsonResponse
from .models import Car

class CarListView(View):
    def get(self, request):
        """Отримати список машин"""
        cars = Car.objects.all()
        data = [
            {
                'id': car.id,
                'brand': car.brand.name,
                'model': car.model.name,
                'year': car.year,
            }
            for car in cars
        ]
        return JsonResponse({'cars': data})
    
    def post(self, request):
        """Створити нову машину"""
        # Логіка збереження
        return JsonResponse(
            {'message': 'Car created'}, 
            status=201
        )

class CarDetailView(View):
    def get(self, request, pk):
        """Отримати деталі машини"""
        try:
            car = Car.objects.get(pk=pk)
            return JsonResponse({
                'id': car.id,
                'brand': car.brand.name,
                'model': car.model.name,
                'year': car.year,
            })
        except Car.DoesNotExist:
            return JsonResponse(
                {'error': 'Not found'}, 
                status=404
            )
    
    def put(self, request, pk):
        """Оновити машину"""
        # Логіка оновлення
        return JsonResponse({'message': 'Car updated'})
    
    def delete(self, request, pk):
        """Видалити машину"""
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return JsonResponse(
                {'message': 'Car deleted'}, 
                status=204
            )
        except Car.DoesNotExist:
            return JsonResponse(
                {'error': 'Not found'}, 
                status=404
            )
```

### APIView (для REST API)

Django REST Framework пропонує `APIView` — краще для API:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(APIView):
    def get(self, request):
        """GET /api/cars/ - Список машин"""
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """POST /api/cars/ - Створення машини"""
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )

class CarDetailView(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """GET /api/cars/{id}/ - Деталі машини"""
        car = self.get_object(pk)
        if not car:
            return Response(
                {'error': 'Not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """PUT /api/cars/{id}/ - Оновлення машини"""
        car = self.get_object(pk)
        if not car:
            return Response(
                {'error': 'Not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        """DELETE /api/cars/{id}/ - Видалення машини"""
        car = self.get_object(pk)
        if not car:
            return Response(
                {'error': 'Not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### ViewSets (найпростіший варіант для CRUD)

Генерують усі views автоматично:

```python
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # Автоматично генерує:
    # GET /api/cars/          - список
    # POST /api/cars/         - створення
    # GET /api/cars/{id}/     - деталі
    # PUT /api/cars/{id}/     - оновлення
    # DELETE /api/cars/{id}/  - видалення
```

Реєстрація в URLs:

```python
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.CarViewSet, basename='car')

urlpatterns = router.urls
```

## HTTP Status Codes

Правильні коди для API:

```python
200 OK              # Успішно
201 CREATED         # Ресурс створений
204 NO CONTENT      # Успішно, немає змісту (DELETE)
400 BAD REQUEST     # Невірні дані
401 UNAUTHORIZED    # Потрібна аутентифікація
403 FORBIDDEN       # Доступ заборонений
404 NOT FOUND       # Ресурс не знайдено
500 SERVER ERROR    # Помилка сервера
```

## Примітки про GET параметри

Запит: `GET /api/cars/?brand=Toyota&year=2024`

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class CarListView(APIView):
    def get(self, request):
        # Отримання параметрів
        brand = request.query_params.get('brand')
        year = request.query_params.get('year')
        
        # Фільтрація
        cars = Car.objects.all()
        if brand:
            cars = cars.filter(brand__name=brand)
        if year:
            cars = cars.filter(year=year)
        
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
```

## Домашнє завдання

1. Створіть `cars/urls.py` з маршрутами для CRUD операцій
2. Імплементуйте базові CBV views (GET список, GET деталі, POST, PUT, DELETE)
3. Налаштуйте `users/urls.py` для маршрутів користувачів
4. Тестуйте URLs через браузер та curl:
   ```bash
   curl http://127.0.0.1:8000/api/cars/
   ```

## Контрольні питання

1. Чим відрізняються FBV та CBV?
2. Як визначити параметр в URL?
3. Що таке app_name в urls.py?
4. Які HTTP статус коди використовуються в REST API?
5. Що робить APIView краще за звичайний View?

## Посилання

- [Django URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [REST Framework APIView](https://www.django-rest-framework.org/api-guide/views/)
