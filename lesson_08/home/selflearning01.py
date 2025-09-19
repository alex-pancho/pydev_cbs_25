# selflearning_tasks.py

# Інструкція:
# 1. Уважно прочитайте коментарі до кожного завдання.
# 2. Напишіть код для виконання кожного завдання у відведеному місці.
# 3. Не змінюйте імена функцій, які ви маєте реалізувати.
# 4. Після завершення запустіть файл test_selflearning.py для перевірки вашої роботи.

# -------------------------------------------------------------------------------------

# Завдання 1: Робота з вбудованими функціями
# Мета: Закріпити навички використання функцій `sum()`, `max()`, `min()`, `len()`.
#
# Створіть функцію `analyze_list(numbers)`, яка приймає список чисел.
# Функція повинна повернути словник, що містить:
# - 'sum': суму всіх чисел у списку.
# - 'max': максимальне число у списку.
# - 'min': мінімальне число у списку.
# - 'len': кількість елементів у списку.
#
# Примітка: для порожнього списку `max()` та `min()` можуть викликати помилку.
# Опрацюйте цей випадок, щоб функція повертала None для max та min, якщо список порожній.
#
# Приклад: analyze_list([1, 2, 3, 4, 5]) повинна повернути {'sum': 15, 'max': 5, 'min': 1, 'len': 5}
def analyze_list(numbers):
    if not numbers:
        return {'sum': 0, 'max': None, 'min': None, 'len': 0}
    # Ваш код тут
    return {
        'sum': sum(numbers), 'max': max(numbers), 'min': min(numbers), 'len': len(numbers)
    }

# -------------------------------------------------------------------------------------

# Завдання 2: Різниця між `sorted()` та `sort()`
# Мета: Зрозуміти різницю між функцією `sorted()` та методом `.sort()`.
#
# Створіть функцію `get_sorted_list(numbers)`, яка приймає список чисел.
# Функція повинна повернути НОВИЙ відсортований список у порядку зростання.
# ВАЖЛИВО: оригінальний список, переданий у функцію, не повинен змінюватися.
#
# Приклад:
# original_list = [5, 2, 8, 1]
# sorted_list = get_sorted_list(original_list)
# print(sorted_list)  # повинно вивести [1, 2, 5, 8]
# print(original_list) # повинно вивести [5, 2, 8, 1]

def get_sorted_list(numbers):
    sorted_list = sorted(numbers)
    # Ваш код тут
    return sorted_list
numbers = [5, 2, 8, 1]
print(f"sorted_list: {get_sorted_list(numbers)}")
print(f"original numbers: {numbers}")
print()
# -------------------------------------------------------------------------------------

# Завдання 3: Створення функції з аргументами за замовчуванням
# Мета: Навчитися створювати функції з позиційними та іменованими аргументами,
# а також використовувати значення за замовчуванням.
#
# Створіть функцію `greet(name, greeting="Привіт")`.
# Функція повинна повертати рядок привітання у форматі: "{greeting}, {name}!".
#
# Приклад:
# greet("Іван") повинна повернути "Привіт, Іван!"
# greet("Олена", "Доброго дня") повинна повернути "Доброго дня, Олена!"
def greet(name, greeting="Привіт"):
    user_greet = f"{greeting}, {name}!"
    # Ваш код тут
    return user_greet
print(greet("Vasya", "Obebasya"))
print(greet("Tolik"))
print()
# -------------------------------------------------------------------------------------

# Завдання 4: Використання `*args`
# Мета: Навчитися створювати функції, що приймають довільну кількість позиційних аргументів.
#
# Створіть функцію `multiply_all(*args)`, яка приймає будь-яку кількість числових аргументів
# і повертає їх добуток. Якщо аргументів немає, функція повинна повернути 1.
#
# Приклад:
# multiply_all(1, 2, 3) повинна повернути 6
# multiply_all(10, 2) повинна повернути 20
# multiply_all() повинна повернути 1
def multiply_all(*args):
    multiply = 1
    for num in args:
        multiply *= num
    # Ваш код тут   
    return multiply

print(f"multiply_all(1, 2, 3): {multiply_all(1, 2, 3)}")
print(f"multiply_all(10, 2): {multiply_all(10, 2)}")
print(f"multiply_all(): {multiply_all()}")
print()

# -------------------------------------------------------------------------------------

# Завдання 5: Використання `**kwargs`
# Мета: Навчитися створювати функції, що приймають довільну кількість іменованих аргументів.
#
# Створіть функцію `create_profile(**kwargs)`, яка приймає іменовані аргументи
# (наприклад, name="John", age=30, city="New York") і повертає рядок,
# що описує профіль у форматі "Key: Value", де кожна пара ключ-значення знаходиться на новому рядку.
# Пари мають бути відсортовані за ключем для узгодженості.
#
# Приклад:
# create_profile(name="Іван", age=25) повинна повернути рядок:
# "age: 25\nname: Іван"


def create_profile(**kwargs):
    profile = []
    for key in kwargs:
       profile.append(f'{key}: {kwargs[key]}')
    return "\n".join(profile)


def create_profile(**kwargs):
    profile = []
    for key, value in kwargs.items():
       profile.append(f'{key}: {value}')
    return "\n".join(profile)


def create_profile(**kwargs):
   return "\n".join([f'{key}: {value}' for key, value in kwargs.items()])


print(create_profile(name="Іван", age=25))
print()
print(create_profile(name="John", age=30, city="New York"))
print()
# -------------------------------------------------------------------------------------

# Завдання 6: Комбінація позиційних та ключових аргументів
# Мета: Навчитися комбінувати різні типи аргументів у одній функції.
#
# Створіть функцію `format_data(main_title, *items, **options)`.
# - `main_title`: обов'язковий позиційний аргумент (рядок).
# - `*items`: довільна кількість позиційних аргументів (рядків).
# - `**options`: довільна кількість іменованих аргументів. Функція повинна шукати
#   опцію `separator` (за замовчуванням ', ') та `prefix` (за замовчуванням 'Item').
#
# Функція повинна повернути один рядок, що починається з `main_title`,
# за яким іде двокрапка, а потім перелік `items`, де кожен елемент має `prefix` і
# вони розділені `separator`.
#
# Приклад:
# format_data("Products", "Apple", "Banana", separator=" | ", prefix="Fruit")
# повинна повернути: "Products: Fruit: Apple | Fruit: Banana"
#
# format_data("Cities", "Kyiv", "Lviv")
# повинна повернути: "Cities: Item: Kyiv, Item: Lviv"
def format_data(main_title, *items, **options):
     # Ваш код тут
    prefix = options.get('prefix', 'Item')
    separator = options.get('separator', ', ')

    data_items = []
    for item in items:
        data_items.append(f'{prefix}: {item}')
    
    sep_data_items = separator.join(data_items)

    ret_sep_data_items = f'{main_title}: {sep_data_items}'

    return ret_sep_data_items
 
print(format_data("Products", "Apple", "Banana", separator=" | ", prefix="Fruit"))
print(format_data("Cities", "Kyiv", "Lviv"))


# -------------------------------------------------------------------------------------

# Завдання 7: Лямбда-функції
# Мета: Зрозуміти синтаксис та використання лямбда-функцій.
#
# Створіть змінну `is_even`, якій присвоєно лямбда-функцію.
# Ця лямбда-функція повинна приймати одне число і повертати `True`, якщо воно парне,
# і `False` в іншому випадку.
#
# Приклад:
# is_even(2) повинно повернути True
# is_even(3) повинно повернути False

is_even = lambda x: x % 2 == 0

print(is_even(2))
print(is_even(3))
# Ваш код тут, замініть None на лямбда-функцію

# -------------------------------------------------------------------------------------

# Завдання 8: Використання `filter` з лямбда-функцією
# Мета: Навчитися використовувати `filter` для фільтрації даних.
#
# Створіть функцію `filter_positive_numbers(numbers)`, яка приймає список чисел
# і повертає список, що містить тільки додатні числа (число 0 не є додатнім).
# Використайте для цього функцію `filter` та лямбда-функцію.
#
# Приклад:
# filter_positive_numbers([-1, 2, -3, 4, 0, 5]) повинна повернути [2, 4, 5]
def filter_positive_numbers(numbers):
    # Ваш код тут
    filter_numbers = list(filter(lambda x: x >= 1, numbers))
    return filter_numbers

print(filter_positive_numbers([-1, 2, -3, 4, 0, 5]))
