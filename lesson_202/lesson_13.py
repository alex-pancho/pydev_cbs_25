from datetime import date


class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))



class Cat:
    def __init__(self, name):        
        self.name = name    
    
    def say_meow(self):        
        print(f"{self.name}: Meow!")


class Kitty(Cat):
    def bite_a_finger(self):
        print("Bite! :)")


class Bird:
    TYPE = "Bird"
    wings = 2

    def fly(self):
        print(f"I am a {self.TYPE} and I can fly!")


class Horse:    
    TYPE = "Horse"
    wings = 0

    def run(self):
        print(f"I am a {self.TYPE} and I can run!")


class Pegas(Bird, Horse):
    TYPE = "Pegas"
    def __init__(self):
        self.wings = Horse.wings
    
    @staticmethod
    def count_legs(counter):
        return counter * 4
    
    @classmethod
    def add_prpos(cls, name):
        cls.props = name

# Функція super() у поодинокому успадкуванні
class Computer:
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd


# Якщо створити дочірній клас Laptop, то буде доступ до властивості базового класу завдяки функції super().
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        # Для квадрата просто потрібно передати один параметр length.
        # При виклику 'super().__init__()' встановимо атрибути 'length' та 'width'.
        super().__init__(length, length)

class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('sub_method from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class C:', b)
        super().sub_method(b + 1)


class D(C):
    def __init__(self):
        print('Initializing: class D')
        # super() з параметрами
        super(C, self).__init__()

    def sub_method(self, b):
        print('sub_method from class D:', b)
        super().sub_method(b + 1)


# my_cat = Cat("Black")
# my_kitty = Kitty("Gray")

# my_cat.say_meow()
# my_kitty.say_meow()
# my_kitty.bite_a_finger()

# my_home_pegas = Pegas()
# my_home_pegas.run()
# my_home_pegas.fly()
# print(my_home_pegas.TYPE)
# print(my_home_pegas.wings)
# anna_home_pegas = Pegas()
# anna_home_pegas.add_prpos("asdf")
# print(my_home_pegas.props)
# print(anna_home_pegas.props)

c = C()
c.sub_method(1)
print('Зверніть увагу як відбувається ініціалізація')
print('класів при вказівці аргументів у функції super()')
d = D()
d.sub_method(1)

class Car:
    def __init__(self, brand, model):
        self.brand = brand         # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute
        self.__len = 1

    def show_model(self):
        return self._model
    
    def show_year(self):
        return self.__year
    
    def update_year(self, year):
        if year >= self.__year:
            self.__year = year
    
    def __str__(self):
        return f"It is {self.brand} {self._model}, made in {self.__year}"

    def __len__(self):
        return self.__len

    def __del__(self):
        print(str(self), "DELETE")
    
    def __add__(self, _):
        self.__len += 1
    
    def __eq__(self, cls):
        return self.__year <= cls.show_year()


my_car = Car("AUDI", "City")

print(my_car.show_model())
print(my_car.show_year())
my_car.update_year(2023)
#my_car.__init__("AUDI", "City")
print(my_car.show_year())
print(str(my_car))
print(len(my_car))
#del my_car
new_car = Car("BMW", "Octavia")
new_car + my_car
print(len(my_car))
print(len(new_car))
print(my_car == new_car)
print(new_car == my_car)