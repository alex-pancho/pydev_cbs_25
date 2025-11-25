# 1. Додавання
def add(a, b):
    return a + b


# 2. Перевірка парності
def is_even(n):
    return n % 2 == 0


# 3. Розворот рядка
def reverse_string(s):
    return s[::-1]


# 4. Мінімум у списку
def find_min(nums):
    return min(nums)


# 5. Перевірка підрядка
def contains_substring(s, sub):
    return sub in s


# 6. Факторіал
def factorial(n):
    if n < 0:
        raise ValueError("Факторіал не визначений для від’ємних чисел")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 7. Ділення з винятком
def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


# 8. Паліндром
def is_palindrome(s):
    return s == s[::-1]


# 9. Сума елементів списку
def sum_list(nums):
    return sum(nums)


# 10. Конвертація в верхній регістр
def to_upper(s):
    return s.upper()
