# -*- coding: utf-8 -*-
"""
Завдання для самостійного вивчення: Функції в Python
===================================================

Це файл з завданнями для закріплення матеріалу про функції в Python.
Виконайте всі завдання послідовно. Перевірити правильність можна запустивши test_selflearning.py

Теми:
- Створення функцій
- Аргументи функцій
- *args і **kwargs
- Позиційні та ключові параметри
- Лямбда-функції
- Вбудовані функції (map, zip, isinstance, type, sort, sorted)
"""

# =============================================================================
# ЗАВДАННЯ 1: Основи створення функцій
# =============================================================================

def greeting(name):
    """
    Завдання 1.1: Створіть функцію, яка приймає ім'я та повертає привітання
    
    Args:
        name (str): Ім'я для привітання
        
    Returns:
        str: Рядок привітання у форматі "Привіт, {name}!"
    """
    # TODO: Реалізуйте функцію
    
    return f'Привіт, {name}!'

print(greeting("Miki"))
print()


def calculate_area(length, width):
    """
    Завдання 1.2: Функція для обчислення площі прямокутника
    
    Args:
        length (float): Довжина прямокутника
        width (float): Ширина прямокутника
        
    Returns:
        float: Площа прямокутника
    """
    # TODO: Реалізуйте функцію
    area = length * width
    return area
print(calculate_area(2, 5))
print()



def is_even(number):
    """
    Завдання 1.3: Перевірка чи число парне
    
    Args:
        number (int): Число для перевірки
        
    Returns:
        bool: True якщо число парне, False якщо непарне
    """
    # TODO: Реалізуйте функцію
    
    if number % 2 == 0:
        num = True
    else:
        num = False
    return num
print(is_even(3))
print()


# =============================================================================
# ЗАВДАННЯ 2: Функції з позиційними та ключовими аргументами
# =============================================================================

def create_profile(name, age, city="Не вказано", profession="Не вказано"):
    """
    Завдання 2.1: Створення профілю користувача
    
    Args:
        name (str): Ім'я користувача
        age (int): Вік користувача
        city str, optional): Місто. За замовчуванням "Не вказано"
        profession (str, optional): Професія. За замовчуванням "Не вказано"
        
    Returns:
        dict: Словник з інформацією про користувача
    """
    # TODO: Поверніть словник з ключами: name, age, city, profession
    pass
    profile = {
        "name": name,
        "age": age,
        "city": city,
        "profession": profession
    }
    return profile
print(create_profile('alex', 23))
print()

def calculate_price(base_price, discount=0, tax=0.2):
    """
    Завдання 2.2: Розрахунок фінальної ціни з урахуванням знижки та податку
    
    Args:
        base_price (float): Базова ціна
        discount (float, optional): Знижка (від 0 до 1). За замовчуванням 0
        tax (float, optional): Податок (від 0 до 1). За замовчуванням 0.2
        
    Returns:
        float: Фінальна ціна після знижки та податку
    """
    # TODO: Обчисліть фінальну ціну: (base_price * (1 - discount)) * (1 + tax)
    
    price = (base_price * (1 - discount)) * (1 + tax)

    return price
print(calculate_price(10, 0.2, 0.3))
print()


# =============================================================================
# ЗАВДАННЯ 3: *args і **kwargs
# =============================================================================

def sum_all(*args):
    """
    Завдання 3.1: Функція для додавання будь-якої кількості чисел
    
    Args:
        *args: Будь-яка кількість чисел
        
    Returns:
        int/float: Сума всіх переданих чисел
    """
    # TODO: Поверніть суму всіх переданих аргументів
    sum_args = sum(args)
    return sum_args

print(sum_all(3, 4, 5))
print()


def create_student(**kwargs):
    """
    Завдання 3.2: Створення студента з довільними параметрами
    
    Args:
        **kwargs: Довільні параметри студента
        
    Returns:
        dict: Словник з обов'язковими ключами name, age та всіма переданими параметрами
    """
    # TODO: Поверніть словник з переданими параметрами
    # Якщо name або age не передані, встановіть їх за замовчуванням

    student = dict(kwargs)
    student.setdefault("name", "no data")
    student.setdefault("age", "no data")
    return student
print(create_student(name="Kamoni"))
print()


def flexible_function(*args, **kwargs):
    """
    Завдання 3.3: Функція, яка приймає і позиційні, і ключові аргументи
    
    Args:
        *args: Позиційні аргументи
        **kwargs: Ключові аргументи
        
    Returns:
        tuple: Кортеж з двох елементів: (список args, словник kwargs)
    """
    # TODO: Поверніть кортеж (list(args), kwargs)

    return list(args), kwargs
print(flexible_function(2, 3, 4, name="alex", age="18"))
print()


# =============================================================================
# ЗАВДАННЯ 4: Лямбда-функції
# =============================================================================

# Завдання 4.1: Створіть лямбда-функцію для піднесення числа до квадрату
square = lambda x: x ** 2
# TODO: Замініть None на лямбда-функцію

# Завдання 4.2: Лямбда-функція для перевірки чи число більше 10
is_greater_than_10 = lambda x: x > 10 
# TODO: Замініть None на лямбда-функцію

# Завдання 4.3: Лямбда-функція для об'єднання двох рядків
concatenate = lambda x, y: x + y 
# TODO: Замініть None на лямбда-функцію


# =============================================================================
# ЗАВДАННЯ 5: Робота з вбудованими функціями
# =============================================================================


def check_type_vs_isinstance(value, check_type):
    """
    Завдання 5.1: Порівняння type() та isinstance()
    
    Args:
        value: Значення для перевірки
        check_type: Тип для перевірки
        
    Returns:
        tuple: (результат type(), результат isinstance())
    """
    # TODO: Поверніть кортеж з результатами type(value) == check_type та isinstance(value, check_type)

    return type(value) == check_type, isinstance(value, check_type)
print(check_type_vs_isinstance(2, str))
print()


def sort_vs_sorted_demo(numbers):
    """
    Завдання 5.2: Різниця між sort() та sorted()
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        tuple: (оригінальний список після sort(), новий відсортований список)
    """
    # TODO: Застосуйте sort() до оригінального списку і поверніть його разом з sorted()

    original_numbers = numbers.copy()
    numbers.sort()
    sorted_numbers = sorted(original_numbers)
    return(numbers, sorted_numbers)
print(sort_vs_sorted_demo([1, 2, 3]))
print()


# =============================================================================
# ЗАВДАННЯ 6: Складніші завдання
# =============================================================================

def filter_and_process(data, filter_func, process_func):
    """
    Завдання 6.1: Фільтрація та обробка даних
    
    Args:
        data (list): Список даних
        filter_func (function): Функція для фільтрації
        process_func (function): Функція для обробки
        
    Returns:
        list: Список оброблених елементів, які пройшли фільтрацію
    """
    # TODO: Відфільтруйте дані та обробіть їх

    return[process_func(item) for item in data if filter_func(item)]

def is_pos(num):
    return num > 0

def square_num (num):
    return num ** 2

print(filter_and_process([1, 2, 3, 4], is_pos, square_num))
print()


def create_multiplier(factor):
    """
    Завдання 6.2: Функція, яка повертає функцію (замикання)
    
    Args:
        factor (int/float): Множник
        
    Returns:
        function: Функція, яка множить переданий аргумент на factor
    """
    # TODO: Поверніть функцію, яка множить аргумент на factor
    pass


def advanced_calculator(*args, operation="sum", **kwargs):
    """
    Завдання 6.3: Розширений калькулятор
    
    **kwargs
    Args:
        *args: Числа для обчислення
        operation (str): Операція ("sum", "multiply", "max", "min")
        **kwargs: Додаткові параметри
        
    Returns:
        float/int: Результат обчислення
    """
    # TODO: Реалізуйте калькулятор з різними операціями

    
    if operation == "sum":
        res_calc = sum(args)
    elif operation == "multiply":
        res_calc = 1
        for num in args:
            res_calc *= num
    elif operation == "max":
        res_calc = max(args)
    elif operation == "min":
        res_calc = min(args)

    if "round_to" in kwargs:
        res_calc = round(res_calc, kwargs["round_to"])

    return res_calc

print(advanced_calculator(1, 2, 3.4342423424, 4, operation="multiply", round_to=2))
print()



# =============================================================================
# ПРИКЛАДИ ВИКОРИСТАННЯ (для розуміння)
# =============================================================================

if __name__ == "__main__":
    # Приклади використання функцій
    print("=== Приклади використання ===")
    
    # Після реалізації функцій, розкоментуйте код нижче:
    
    print(greeting("Олексій"))
    print(calculate_area(5, 3))
    print(is_even(4))
    
    profile = create_profile("Марія", 25, city="Київ")
    print(profile)
    
    print(sum_all(1, 2, 3, 4, 5))

    
    print("Реалізуйте всі функції та перевірте їх за допомогою test_selflearning.py")