# Лекція 4: Forms та POST Запити

## Що таке Forms в Django?

Form — це компонент для безпечного обробління користувацьких даних (POST запити). Django автоматично обробляє:
- CSRF захист (Cross-Site Request Forgery)
- Валідацію даних
- Генерування HTML форм
- Оброблення помилок

## Типи Forms

### 1. Django Forms (для HTML сторінок)

```python
# cars/forms.py
from django import forms
from .models import Car, Brand, Model

class CarForm(forms.ModelForm):
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        label="Car Brand"
    )
    model = forms.ModelChoiceField(
        queryset=Model.objects.all(),
        label="Car Model"
    )
    year = forms.IntegerField(
        label="Year",
        min_value=1900,
        max_value=2024,
        help_text="Enter vehicle year"
    )
    
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Car description'}
            ),
            'year': forms.NumberInput(attrs={'type': 'number'}),
        }
```

### 2. Serializers (для REST API)

```python
# cars/serializers.py
from rest_framework import serializers
from .models import Car, Brand, Model

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'name', 'brand']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    model = ModelSerializer(read_only=True)
    brand_id = serializers.IntegerField(write_only=True)
    model_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'brand_id', 'model_id',
            'year', 'description', 'owner', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
    
    def validate_year(self, value):
        """Кастомна валідація року"""
        if value < 1900 or value > 2024:
            raise serializers.ValidationError(
                "Year must be between 1900 and 2024"
            )
        return value
    
    def create(self, validated_data):
        """Створення машини з brand_id та model_id"""
        brand_id = validated_data.pop('brand_id')
        model_id = validated_data.pop('model_id')
        
        brand = Brand.objects.get(id=brand_id)
        model = Model.objects.get(id=model_id)
        
        car = Car.objects.create(
            brand=brand,
            model=model,
            **validated_data
        )
        return car
```

## View обробка Forms (HTML)

### 1. Function-Based View

```python
from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car

def car_create(request):
    """Створення нового автомобіля"""
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('cars:car_detail', pk=car.id)
        # Форма з помилками буде відправлена в template
    else:
        form = CarForm()
    
    return render(request, 'cars/car_form.html', {'form': form})

def car_update(request, pk):
    """Оновлення автомобіля"""
    car = Car.objects.get(pk=pk)
    
    # Перевірка прав доступу
    if car.owner != request.user and not request.user.is_staff:
        return redirect('cars:car_list')
    
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars:car_detail', pk=car.id)
    else:
        form = CarForm(instance=car)
    
    return render(request, 'cars/car_form.html', {
        'form': form,
        'car': car,
    })

def car_delete(request, pk):
    """Видалення автомобіля"""
    car = Car.objects.get(pk=pk)
    
    # Перевірка прав
    if car.owner != request.user and not request.user.is_staff:
        return redirect('cars:car_list')
    
    if request.method == 'POST':
        car.delete()
        return redirect('cars:car_list')
    
    return render(request, 'cars/car_confirm_delete.html', {'car': car})
```

### 2. Class-Based View

```python
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars:car_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('cars:car_list')
    
    def get_queryset(self):
        # Користувачі можуть редагувати тільки свої машини
        return Car.objects.filter(owner=self.request.user)

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('cars:car_list')
    
    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)
```

## HTML Forms in Templates

### Базова форма

```html
<!-- cars/templates/cars/car_form.html -->
{% extends 'base.html' %}

{% block title %}Add Car - Car Service{% endblock %}

{% block content %}
    <h2>{% if car %}Edit Car{% else %}Add New Car{% endif %}</h2>
    
    <!-- Виведення всіх помилок форми -->
    {% if form.non_field_errors %}
        <div class="errors">
            {% for error in form.non_field_errors %}
                <p style="color: red;">{{ error }}</p>
            {% endfor %}
        </div>
    {% endif %}
    
    <form method="post">
        {% csrf_token %}  <!-- Обов'язков для POST! -->
        
        <!-- Простий варіант -->
        {{ form.as_p }}
        
        <!-- Або разом по одному -->
        <div>
            {{ form.brand.label_tag }}
            {{ form.brand }}
            {% if form.brand.errors %}
                <span style="color: red;">{{ form.brand.errors }}</span>
            {% endif %}
        </div>
        
        <div>
            {{ form.model.label_tag }}
            {{ form.model }}
            {% if form.model.errors %}
                <span style="color: red;">{{ form.model.errors }}</span>
            {% endif %}
        </div>
        
        <div>
            {{ form.year.label_tag }}
            {{ form.year }}
            {% if form.year.errors %}
                <span style="color: red;">{{ form.year.errors }}</span>
            {% endif %}
        </div>
        
        <div>
            {{ form.description.label_tag }}
            {{ form.description }}
        </div>
        
        <button type="submit">Save Car</button>
        <a href="{% url 'cars:car_list' %}">Cancel</a>
    </form>
{% endblock %}
```

### Форма з кастомним дизайном

```html
<form method="post" class="form">
    {% csrf_token %}
    
    <div class="form-group">
        <label for="{{ form.brand.id_for_label }}">Brand</label>
        {{ form.brand }}
    </div>
    
    <div class="form-group">
        <label for="{{ form.model.id_for_label }}">Model</label>
        {{ form.model }}
    </div>
    
    <div class="form-group">
        <label for="{{ form.year.id_for_label }}">Year</label>
        {{ form.year }}
    </div>
    
    <div class="form-group">
        <label for="{{ form.description.id_for_label }}">Description</label>
        {{ form.description }}
    </div>
    
    <button type="submit" class="btn btn-primary">Save</button>
</form>
```

## POST запити до REST API

### 1. APIView

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

class CarListCreateView(APIView):
    def post(self, request):
        """Створення машини через API"""
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
```

### 2. ViewSet (найпростіше)

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Автоматично присвоює owner"""
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        """Фільтрація за власником"""
        user = self.request.user
        if user.is_staff:
            return Car.objects.all()
        return Car.objects.filter(owner=user)
```

## Приклади curl запитів

### GET список

```bash
curl -X GET http://127.0.0.1:8000/api/cars/ \
  -H "Content-Type: application/json"
```

### POST (створення)

```bash
curl -X POST http://127.0.0.1:8000/api/cars/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "brand_id": 1,
    "model_id": 2,
    "year": 2024,
    "description": "My new car"
  }'
```

### PUT (оновлення)

```bash
curl -X PUT http://127.0.0.1:8000/api/cars/5/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "brand_id": 1,
    "model_id": 3,
    "year": 2023
  }'
```

### DELETE

```bash
curl -X DELETE http://127.0.0.1:8000/api/cars/5/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Валідація в Serializer

```python
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year']
    
    def validate_year(self, value):
        """Валідація одного поля"""
        if value < 1900:
            raise serializers.ValidationError(
                "Year cannot be earlier than 1900"
            )
        return value
    
    def validate(self, data):
        """Валідація кількох полів разом"""
        if data['model'].brand != data['brand']:
            raise serializers.ValidationError(
                "Selected model does not match the brand"
            )
        return data
    
    def validate_brand(self, value):
        """Асинхронна валідація"""
        if not value.is_active:
            raise serializers.ValidationError(
                "This brand is not available"
            )
        return value
```

## CSRF захист

Кожний POST запит повинен включати CSRF токен:

### У HTML формі

```html
<form method="post">
    {% csrf_token %}
    <!-- поля форми -->
</form>
```

### У JavaScript/Fetch

```javascript
// Отримання CSRF токену
const token = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Або з cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// POST запит
fetch('/api/cars/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({
        brand_id: 1,
        model_id: 2,
        year: 2024,
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Оброблення помилок у API

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CarDetailView(APIView):
    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response(
                {'error': 'Car not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = CarSerializer(car, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
```

## Домашнє завдання

1. Створіть `cars/forms.py` з CarForm
2. Реалізуйте views для створення, оновлення та видалення машин
3. Створіть template для форми
4. Реалізуйте API endpoints для POST/PUT/DELETE
5. Протестуйте curl запити
6. Перевірте CSRF захист

## Контрольні питання

1. Яка різниця між Forms та Serializers?
2. Як включити CSRF захист у формі?
3. Як перевірити права користувача на редагування?
4. Як створити кастомну валідацію в Serializer?
5. Як обробити помилки валідації в API?

## Посилання

- [Django Forms](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Model Forms](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/)
- [DRF Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [CSRF Protection](https://docs.djangoproject.com/en/stable/ref/csrf/)
