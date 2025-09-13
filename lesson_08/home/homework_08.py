# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        
        result = number * multiplier
        
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print()

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_2_numbers(num1: int | float, num2: int | float):
    """
    A function that calculates the sum of two numbers

    Args:
        num1(int or float): 1st number
        num2(int or float): 2nd number

    Returns:
        sum of 1st and 2nd number(int or float)
        
    """
    return num1 + num2


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(*args: int | float):
    """
    A function that calculates the arithmetic mean of a list of numbers

    Args:
        list numbers args(int or float)

    Returns:
        arithmetic mean of a list of numbers(int or float)

    """
    return sum(args) / len(args)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(string: str):
    """
    A function that takes a string and returns it in reverse order.

    Args:
        original string: string(str)
        reversed string: reversed_string
    Returns:
        string in reverse order
    """
    reversed_string = string[::-1]
    return reversed_string

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def biggest_word(*args):
    """
    A function that takes a list of words and returns the longest word in the list.

    Args:
        args: a list of words
        long_word: the longest word

    Returns:
        The longest word in the list
    """
    long_word = max(args, key=len)
    return long_word


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
       
    # return str1.find(str2)

    len_str1 = len(str1)
    len_str2 = len(str2)

    for num in range(len_str1 - len_str2 +1):
        if str1[num:num + len_str2] == str2:
            return num
    
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def swich_key_value(**kwargs):

    """
    функція яка заміняе ключі та значення місцями у словнику

    Args:
        kwargs: словник користувача
        new_dict :зміненний словник

    Returns:
        замінені ключі та значення місцями

    """
    new_dict = {v: k for k, v in kwargs.items()}

    return new_dict

print(swich_key_value(name="poltavskiy", surname="paliy"))
print()

# task 8
def sum_sets(set1, set2):
    """
        Обчисліть суму елементів двох множин, які не є спільними

    Args:
        set_1: 1 список чисел
        set_2: 2 список чисел
        sum_set: сумма

    Returns:
        суму елементів двох множин, які не є спільними
    """
    set_1 = set(set1)
    set_2 = set(set2)
    set_dif = set_1 ^ set_2
    sum_set = sum(set_dif)
    return sum_set

print(sum_sets([1, 2, 3, 4, 5], [4, 6, 5, 10]))
print()


# task 9

def unuque_nambers(*numbers: int | float):
    """
    Знайдіть всі унікальні елементи в списку

    Args:
        numbers: users numbers
        unique_number: unique numbers

    Return:
        унікальні елементи в списку
    """

    unuque_num = []
    for num in numbers:
        if num not in unuque_num:
            unuque_num.append(num)
    return unuque_num

print(unuque_nambers(1, 2, 3, 4, 3, 2))
print()

# task 10

def check_dublicate(*args: int | float):
    """
    Перевірте, чи є в списку дублікати

    Args:
        args: список чисел
        dublicate_numbers: дублікати в списку

    Returns:
        дублікати в списку
    """

    dublicate_numbers = set(x for x in args if args.count(x) > 1)
    
    return dublicate_numbers

print(check_dublicate(1, 2, 3, 4, 5, 3))
print()
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""