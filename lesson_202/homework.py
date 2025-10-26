"""
Завдання 1

Створіть клас Editor, який містить методи view_document та edit_document. 
Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для безкоштовної версії. 
Створіть підклас ProEditor, у якому цей метод буде перевизначено. 
Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
Викликайте методи перегляду та редагування документів.

# Завдання 1.1

# Створіть ієрархію класів із використанням множинного успадкування. 
# Виведіть на екран порядок вирішення методів для кожного класу. 
# Поясніть, чому лінеаризація даних класів виглядає саме так.

Завдання 2
На підставі MyClass1
створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.

Завдання 3
На підставі MyClass1
створіть декоратори @classmethod для формування переліку об'єктів, які підрахують кількість повнолітніх людей в Україні та Америці.

# Завдання 3.1 

# Створіть ієрархію класів транспортних засобів. 
# У загальному класі опишіть загальні всім транспортних засобів поля, 
# у спадкоємцях – специфічні їм. 
# Створіть кілька екземплярів. 
# Виведіть інформацію щодо кожного транспортного засобу.
"""

class Editor():
    def view_document(self):
        print("Ви переглядаете документ.")
    def edit_document(self):
        print("Редагування документів недоступне для безкоштовної версії.")
class ProEditor(Editor):
    def edit_document(self):
        print("Ви редагуєте документ, зміни збережено!")

LICENSE_KEY = "QWERTY1"
key = input("Введіть ліцензійний ключ: ")
if key == LICENSE_KEY:
    editor = ProEditor()
    print("Ключ підтверджено!")
else:
    editor = Editor()
    print("Ключ невірний")
editor.view_document()
editor.edit_document()

class Parent1():
    pass
class Parent2():
    pass
class Parent3():
    pass
class Parent4(Parent1, Parent2, Parent3):
    pass

print(f"MRO для родича Parent1 {Parent1.__mro__}")
print(f"MRO для родича Parent2 {Parent2.__mro__}")
print(f"MRO для родича Parent3 {Parent3.__mro__}")
print(f"MRO для родича Parent4 {Parent4.__mro__}") 

# Бере сам клас, потім додає лінеаризацію батьків зліва направо, при цьому локальний порядок наслідування і гарантує, що підкласи завжди мают пріоритет над батьками.

class MyClass1():
    @staticmethod
    def in_Ukraine(age):
        return age >= 18
    @staticmethod
    def in_USA(age):
        return age >= 21
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    @classmethod
    def count_people_in_Ukraine(cls, people):
        count = sum(1 for person in people if person.country == "UA" and cls.in_Ukraine(person.age))
        return count
    @classmethod
    def count_people_in_USA(cls, people):
        count = sum(1 for person in people if person.country == "USA" and cls.in_USA(person.age))
        return count
people = [
    MyClass1("Іван", 20, "UA"),
    MyClass1("Оля", 17, "UA"),
    MyClass1("Джон", 22, "USA"),
    MyClass1("Мері", 19, "USA"),
    MyClass1("Макс", 25, "UA"),
]

adults_in_ukraine = MyClass1.count_people_in_Ukraine(people)
adults_in_USA = MyClass1.count_people_in_USA(people)
print(f"Кількість повнолітних в Україні {adults_in_ukraine}")
print(f"Кількість повнолітних у США {adults_in_USA}")

age = int(input("Введіть свій вік: "))

if MyClass1.in_USA(age):
    print("Ви повнолітні у США")
elif MyClass1.in_Ukraine(age):
    print("Ви повнолітні в Україні")
else:
    print("Ви не являетесь повнолітним")


class Vehicle():
    def __init__(self, brand, color, wheels):
        self.brand = brand
        self.color = color
        self.wheels = wheels
    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Колір:{self.color}")
        print(f"Кількість коліс: {self.wheels}")
class Car(Vehicle):
    def __init__(self, brand, color, wheels, doors, fuel_type):
        super().__init__(brand, color, wheels)
        self.doors = doors
        self.fuel_type = fuel_type
    def display_info(self):
        super().display_info()
        print(f"Кількість дверей: {self.doors}")
        print(f"Тип пального: {self.fuel_type}")
class Bike(Vehicle):
    def __init__(self, brand, color, wheels, bike_type):
        super().__init__(brand, color, wheels)
        self.bike_type = bike_type
    def display_info(self):
        super().display_info()
        print(f"Тип велосипеда: {self.bike_type}")
class Plane(Vehicle):
    def __init__(self, brand, color, wheels, engine_type, max_speed):
        super().__init__(brand, color, wheels)
        self.engine_type = engine_type
        self.max_speed = max_speed
    def display_info(self):
        super().display_info()
        print(f"Тип двигуна: {self.engine_type}")
        print(f"Максимальна швидкість: {self.max_speed} км/год")
car = Car("Toyota", "Червоний", 4, 5, "Бензин")
bike = Bike("Trek", "Синій", 2, "Гірський")
plane = Plane("Boeing", "Білий", 8, "Реактивний", 900)

print("Інформація про автомобіль:")
car.display_info()
print("Інформація про велосипед:")
bike.display_info()
print("Інформація про літак:")
plane.display_info()