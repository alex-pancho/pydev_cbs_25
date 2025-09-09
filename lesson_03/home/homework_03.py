# Вправа 1: Проста математика
print("\n=== ВПРАВА 1: Калькулятор ===")
print("Створіть простий калькулятор для двох чисел і двох дій")
print("Підтримувані операції: +, -")

# Початок реалізації:
num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))

if operation == "+": 
    result_add = num1 + num2
    print(f"{num1} + {num2} = {result_add}")
elif operation == "-":
    result_subt = num1 - num2
    print(f"{num1} - {num2} = {result_subt}")
else:
    print("Error value")


# Вправа 2: Перевірка паролю
print("\n=== ВПРАВА 2: Перевірка паролю ===")
print("Створіть систему перевірки паролю")
print("Пароль повинен містити принаймні 8 символів")

pass_1 = "12345678"
user_pass = input('\nПеревiрка паролю: ')
if user_pass == pass_1:
    print("Вірний пароль")
elif user_pass.__len__() != 8:
    print("Пароль повинен містити принаймні 8 символів")
else:
    print("Невірний пароль")
print()

# Вправа 3: Визначення високосного року
print("\n=== ВПРАВА 3: Високосний рік ===")
print("Рік є високосним, якщо:")
print("- Ділиться на 4 i не ділиться на 100")
print("- АБО ділиться на 400")
print()

leap_year = int(input("Введiть рiк: "))

if leap_year % 4 == 0 and leap_year % 100 != 0 and leap_year or leap_year % 400 == 0:
    print(f"\n{leap_year} - високосний рік")
else:
    print(f"\n{leap_year} не високосний рік ")
print()




# Вправа 4: Лічильник голосних
print("\n=== ВПРАВА 4: Лічильник голосних ===")
print("Підрахуйте кількість голосних у рядку")

text = input("Введіть текст: ").lower()
vowels = "аеиіїоуюя"
count = 0

# код тут

for char in text:
    if char in vowels:
        count += 1

print(f"\nКiлькiсть голосних: {count}")
print()


# Вправа 5: Гра 
print("\n=== ВПРАВА 5: Гра ===")
"""
Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
Перевірте роботу гри самостійно, змінюючи значення alien_color
"""

alien_color = {'green' : 5, 'yellow' : 10, 'red' : 15}


user_color = input("\nЯкого кольору був інопланетянин (green, yellow або red): ")
if user_color in alien_color:
    points = alien_color.get(user_color)
    print(f"\nВи заробили {points} балів.")
else:
    print("Невiрний колір прибульця")
print()

# Вправа 6: Піцерія *
print("\n=== ВПРАВА 6: Начинки для піци (pizza_topping) ===")
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

pizza_topping = []

while True:
    
    user_topping = input("\nВведiть ряд начинок для піци: ")
    if user_topping == 'quit':
        break
    pizza_topping.append(user_topping)

print(f"\nВ вашоi пицi такi начинки: {" , ".join(pizza_topping)}")    




# Вправа 7: Зворотний порядок цифр
print("\n=== ВПРАВА 7: Зворотний порядок ===")
print("Виведіть цифри числа у зворотному порядку")

try:
    users_num = int(input("\nВиведiть цифри: "))
    rev_num = str(users_num)[::-1]
    print(f"\nЦифри числа у зворотному порядку: {rev_num}")
except ValueError:
    print("\nВведить тiльки цифри")


# Вправа 8: Пошук максимального числа
print("\n=== ВПРАВА 8: Пошук максимального ===")
print("Знайдіть найбільше число серед введених")
print("Введіть 0 для завершення")

user_num = []

while True:
    try:
        users_numbers = int(input("Введить числа: "))
        if users_numbers == 0:
         break
        user_num.append(users_numbers)
    except ValueError:
        print("Введить тiльки числа")


max_num = user_num[0]
for num in user_num:
    if num > max_num:
        max_num = num

print(f"\n{max_num} найбільше число серед введених")
print()


# Вправа 9: Виключення зі списку
print("\n=== ВПРАВА 9: Виключення зі списку ===")
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(f"\n{fruit}")


# Вправа 10: Вираз в один рядок
print("\n=== ВПРАВА 10: Вираз з умовою в один рядок ===")
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for num in numbers:
#     if num % 2 == 0:
#         num_sq = num ** 2
#         result.append(num_sq)

result = [num ** 2 for num in numbers if num % 2 == 0]

print(f"\n{result}")  #  [4, 16, 36, 64, 100]
print()
