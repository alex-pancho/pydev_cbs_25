# Лекція 7: Django REST Framework

## Що таке REST Framework?

Django REST Framework (DRF) — це потужна бібліотека для розробки REST API. Вона надає:
- Serializers (перетворення даних)
- APIView та ViewSets (спрощена розробка)
- Authentication та Permissions
- Pagination та Filtering
- API документація (Swagger, ReDoc)

## Встановлення і налаштування

### 1. Встановлення пакетів

```bash
pip install djangorestframework
pip install drf-spectacular  # Для Swagger документації
pip install django-cors-headers  # Для CORS
pip install djangorestframework-simplejwt  # Для JWT токенів
```

### 2. Конфігурація settings.py

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
    
    # Наші додатки
    'cars.apps.CarsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... інші middleware
]

REST_FRAMEWORK = {
    # Serializer за замовчуванням
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    
    # Пагінація
    'DEFAULT_PAGINATION_CLASS': 
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    
    # Фільтрація
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    
    # Аутентифікація
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    
    # Дозволи за замовчуванням
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

# Swagger налаштування
SPECTACULAR_SETTINGS = {
    'TITLE': 'Car Service API',
    'DESCRIPTION': 'API для управління автосервісом',
    'VERSION': '1.0.0',
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
}

# CORS налаштування
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
```

### 3. URL конфігурація (autocheck_api/urls.py)

```python
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from cars.views import CarViewSet, BrandViewSet, ModelViewSet

# Реєстрація router-а для ViewSets
router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'models', ModelViewSet, basename='model')

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    
    # Документація
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(
        url_name='schema'
    ), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(
        url_name='schema'
    ), name='redoc'),
]
```

## Serializers

Serializer перетворює Python об'єкти на JSON і навпаки.

### 1. ModelSerializer (найпростіший)

```python
# cars/serializers.py
from rest_framework import serializers
from .models import Brand, Model, Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'description', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']

class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Model
        fields = ['id', 'name', 'brand', 'brand_id', 'year_from', 'year_to']
        read_only_fields = ['id']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    model = ModelSerializer(read_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    model_id = serializers.IntegerField(write_only=True)
    owner_username = serializers.CharField(
        source='owner.username',
        read_only=True
    )
    
    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'brand_id', 'model_id',
            'year', 'description', 'license_plate', 'vin',
            'owner', 'owner_username', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'owner', 'created_at', 'updated_at'
        ]
```

### 2. Кастомна валідація

```python
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [...]
    
    # Валідація одного поля
    def validate_year(self, value):
        if value < 1900:
            raise serializers.ValidationError(
                "Year must be 1900 or later"
            )
        return value
    
    def validate_license_plate(self, value):
        if not value:
            return value
        if len(value) < 3:
            raise serializers.ValidationError(
                "License plate too short"
            )
        return value.upper()
    
    # Валідація кількох полів разом
    def validate(self, data):
        if data['model'].brand_id != data['brand_id']:
            raise serializers.ValidationError(
                "Selected model does not match the brand"
            )
        return data
    
    # Методи create та update
    def create(self, validated_data):
        brand_id = validated_data.pop('brand_id')
        model_id = validated_data.pop('model_id')
        
        car = Car.objects.create(
            brand_id=brand_id,
            model_id=model_id,
            **validated_data
        )
        return car
```

### 3. Вкладені Serializers

```python
class UserSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'cars']
        read_only_fields = ['id']

# Використання
user = User.objects.first()
serializer = UserSerializer(user)
# {
#     'id': 1,
#     'username': 'john',
#     'email': 'john@example.com',
#     'cars': [
#         {'id': 1, 'brand': {...}, ...},
#         {'id': 2, 'brand': {...}, ...},
#     ]
# }
```

## APIView

APIView дозволяє більше контролю над логікою:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Car
from .serializers import CarSerializer

class CarListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        """GET /api/cars/ - Отримати список машин"""
        # Фільтрація
        brand = request.query_params.get('brand')
        year_from = request.query_params.get('year_from')
        
        cars = Car.objects.select_related('brand', 'owner')
        
        if brand:
            cars = cars.filter(brand__name__icontains=brand)
        if year_from:
            cars = cars.filter(year__gte=year_from)
        
        # Пагінація
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(cars, request)
        
        serializer = CarSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        """POST /api/cars/ - Створити машину"""
        serializer = CarSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                {
                    'message': 'Car created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                'message': 'Validation failed',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class CarDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404("Car not found")
    
    def get(self, request, pk):
        """GET /api/cars/{id}/"""
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """PUT /api/cars/{id}/ - Оновити машину"""
        car = self.get_object(pk)
        
        # Перевірка прав
        if car.owner != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """DELETE /api/cars/{id}/"""
        car = self.get_object(pk)
        
        if car.owner != request.user and not request.user.is_staff:
            return Response(
                {'error': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        car.delete()
        return Response(
            {'message': 'Car deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
```

## ViewSets (найпростіше)

ViewSet автоматично генерує CRUD операції:

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.select_related('brand', 'owner')
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Фільтрація, пошук, сортування
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ['brand', 'year', 'is_active']
    search_fields = ['brand__name', 'model__name', 'license_plate']
    ordering_fields = ['year', 'created_at']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        """Автоматично присвоює owner при створенні"""
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        """Фільтрація за користувачем"""
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(owner=user)
    
    # Кастомна дія
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsAuthenticated]
    )
    def deactivate(self, request, pk=None):
        """POST /api/cars/{id}/deactivate/ - Деактивувати машину"""
        car = self.get_object()
        car.is_active = False
        car.save()
        return Response({'message': 'Car deactivated'})
```

## Аутентифікація та Дозволи

### 1. JWT Аутентифікація

```python
# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': "Passwords don't match"}
            )
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Генерація JWT токенів
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'message': 'User created successfully',
                'data': {
                    'user': UserSerializer(user).data,
                    'tokens': {
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# users/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 2. Дозволи

```python
from rest_framework.permissions import BasePermission, IsAuthenticated

class IsOwnerOrReadOnly(BasePermission):
    """Дозволяє редагування тільки власнику"""
    
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user

class IsStaff(BasePermission):
    """Дозволяє доступ тільки для персоналу"""
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

# Використання у ViewSet
class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # ...
```

## Pagination

```python
# Вже налаштована у settings.py
# Але можна кастомізувати:

class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Використання
class CarViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPagination
    # ...
```

## Filtering

```python
# Вже налаштована у settings.py

class CarViewSet(viewsets.ModelViewSet):
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    
    # Точна фільтрація
    filterset_fields = ['brand', 'year', 'is_active']
    
    # Пошук по полях
    search_fields = ['brand__name', 'model__name', 'license_plate']
    
    # Сортування
    ordering_fields = ['year', 'created_at']
    ordering = ['-created_at']

# Використання в запиті
# GET /api/cars/?brand=Toyota&year=2024&search=Camry&ordering=-year
```

## Домашнє завдання

1. Встановіть DRF та всі необхідні пакети
2. Налаштуйте Swagger документацію
3. Створіть Serializers для всіх моделей
4. Реалізуйте ViewSets для CRUD операцій
5. Додайте JWT аутентифікацію
6. Протестуйте API через Swagger UI

## Контрольні питання

1. Яка різниця між Serializer та ModelSerializer?
2. Як реалізувати кастомну аутентифікацію?
3. Що таке дозволи в DRF?
4. Як фільтрувати QuerySet у ViewSet?
5. Як створити кастомну дію в ViewSet?

## Посилання

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [Views and ViewSets](https://www.django-rest-framework.org/api-guide/views/)
- [Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
