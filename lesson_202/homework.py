
from datetime import date

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
############################### Завдання 1
class Editor():
    def __init__(self):
        pass

    def view_document(self):
        pass

    def edit_document(self):
         print("Редагування документів недоступне для безкоштовної версії.")

class ProEditor(Editor):
    def edit_document(self):
        print("Документ відкрито для редагування.")



LICENSE_KEY = "11111" 

use_input = input("Введіть ліцензійний ключ: ")

if use_input == LICENSE_KEY:
    editor = ProEditor()
else:
    editor = Editor()

editor.view_document()
editor.edit_document()
#################################################

############################### Завдання 2
#    
#   На підставі MyClass1
#   створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.
##########################     Завдання 3
#   На підставі MyClass1
#   створіть декоратори @classmethod для формування переліку об'єктів, 
#   які підрахують кількість повнолітніх людей в Україні та Америці.

adult_ages = {"UKR": 18, "USA": 21}
class MyClass1:

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def print_info(self):
        print(self.surname + " " + self.name + " age is: " + str(self.age))

    def is_adult(self, country):
        return self.age >= adult_ages[country]

    @staticmethod
    def is_adult_ukr(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21
      
    @classmethod
    def count_adults_ukr(cls, people_list):
#        return sum(1 for person in people_list if cls.is_adult_ukr(person.age))
        return sum(1 for person in people_list if person.is_adult("UKR"))

    @classmethod
    def count_adults_usa(cls, people_list):
        return sum(1 for person in people_list if cls.is_adult_usa(person.age))


##########################     Завдання 2 test

person1 = MyClass1("Haliuk", "Serhii", 17)
person2 = MyClass1("Doe", "John", 22)

person1.print_info()
if MyClass1.is_adult_ukr(person1.age):
    print("Повнолітній в Україні")
else:
    print("Не повнолітній в Україні")

if MyClass1.is_adult_usa(person1.age):
    print("Повнолітній в США")
else:
    print("Не повнолітній в США")

country = "UKR"
if person1.is_adult(country):
    print("Повнолітній в Україні")
else:
    print("Не повнолітній в Україні")
    
country = "USA"
if person1.is_adult(country):
    print("Повнолітній в США")
else:
    print("Не повнолітній в США")
    
person2.print_info()
print("Повнолітній в Україні:", MyClass1.is_adult_ukr(person2.age))
print("Повнолітній в США:", MyClass1.is_adult_usa(person2.age))

#################################################################

##########################     Завдання 3 test

people = [
    MyClass1("Haliuk", "Serhii", 17),
    MyClass1("Ivanov", "Petro", 19),
    MyClass1("Doe", "John", 20),
    MyClass1("Brown", "Emily", 22),
]

#print(people[0].age)
print("Кількість повнолітніх в Україні:", MyClass1.count_adults_ukr(people))
print("Кількість повнолітніх в США:", MyClass1.count_adults_usa(people))
