import abc
try:
    import zyx
except ModuleNotFoundError:
    import re

def div(a, b):
    
    try:
        if a == 0:
            raise ValueError("Zero divide omn num is Zero!")
        result = a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль.")
        result = 0
    except TypeError as e:
        print(e)
        result = None
    except ValueError as e:
        print(e)
        result = -1
    return f"Результат ділення {a} на {b}: {result}"

for i in range(-4, 5):
    a = 5
    if i == -1:
        i = "i"
    elif i == 2:
        a = 0
    result = div(a, i)
    print("result", result)

def check_age(age:int):
    if not (0 <= age <= 150):
        raise ValueError("Вік не може бути від'ємним або більш 150 років")
    return True
    
# user_age = int(input("Введіть ваш вік: "))
# check_age(user_age)

try:
    user_age = 18 # int(input("Введіть ваш вік: "))
    check_age(user_age)
    print(f"Ваш вік: {user_age}")
except ValueError as ve:
    print(f"Помилка: {ve}")

class TooLargeValueError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f"Значення {value} перевищує ліміт {limit}"
        super().__init__(message)

NBU_LIMIT = 100_000
user_ask_money = int(input("Введіть сумму зняття: "))
try:
    if user_ask_money > NBU_LIMIT:
        raise TooLargeValueError(user_ask_money, NBU_LIMIT)
    else:
        print("Дякую! Ви ввели припустиме значення.")
except TooLargeValueError as e:
    print(e)
    print(f"Ваша сумма повинна бути менше на {user_ask_money - NBU_LIMIT} uah")
