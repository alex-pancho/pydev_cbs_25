

class BasicCar:

    def __init__(self):
        self.brand = "Mersedes"
        self.model = "A4"
        self.wheels = 4


my_car = BasicCar()
my_car.brand = "Toyota"
my_car.model = "Corolla"
print("my_car", my_car.brand, my_car.model, my_car.wheels)

my_second_car = BasicCar()
print("my_second_car", my_second_car.brand, my_second_car.model, my_second_car.wheels)

class Car:
    is_engine_on = False

    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        # self.is_engine_on = False
    
    def engine_key(self):
        print("Зміна стану двигуна викликана")
        self.is_engine_on = not self.is_engine_on

my_3_car = Car("Nissan", "Patrol", 5) # 
print("my_3_car", my_3_car.brand, my_3_car.model, my_3_car.wheels)
print("my_3_car engine",my_3_car.is_engine_on)
my_3_car.engine_key()
print("my_3_car engine afr call engine_key",my_3_car.is_engine_on)


class CarNew:
    is_engine_on = False

    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        # self.is_engine_on = False
    
    def engine_key(self, valid_key:int):
        print("Зміна стану двигуна викликана")
        if valid_key == 112233:
            self.is_engine_on = not self.is_engine_on
            print("Все добре")
        else:
            print("Невірний ключ, двигун не заведеться")

my_4_car = CarNew("Zaz", "Zapor", 5) # 
print("my_3_car", my_4_car.brand, my_4_car.model, my_4_car.wheels)
print("my_3_car engine", my_4_car.is_engine_on)
my_4_car.engine_key(114445)
# my_4_car.is_engine_on = True
print("my_3_car engine afr call engine_key", my_4_car.is_engine_on)


class CarIncap:

    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        self.__is_engine_on = False
    
    @property
    def is_engine_on(self):
        return self.__is_engine_on
    
    @is_engine_on.setter
    def is_engine_on(self, valid_key:int):
        print("Зміна стану двигуна викликана")
        if valid_key == 112233:
            self.__is_engine_on = not self.__is_engine_on
            print("Все добре")
        else:
            print("Невірний ключ, двигун не заведеться")

my_5_car = CarIncap("BMW", "Detroyit", 5) # 
print("my_3_car", my_5_car.brand, my_5_car.model, my_5_car.wheels)
print("my_3_car engine", my_5_car.is_engine_on)
my_5_car.is_engine_on = 112233
# my_5_car.is_engine_on = True
print("my_3_car engine afr call engine_key", my_5_car.is_engine_on)

car6 = CarIncap("Toyota", "Supra")
print("my_6_car engine afr call engine_key", car6.is_engine_on)

class Animal:

    def __init__(self):
        self.legs = 4
        # інкапсуляція
        self.name = ""
    
    #@staticmethod
    def breathe(self):
        return "This animal breathes"  # Виправлено повідомлення та додано self

    def speak(self):
        pass  # Загальний метод для всіх тварин


class Dog(Animal):

    def speak(self):
        return "Gav!!!"

class Cat(Animal):

    def __init__(self, name:str):
        super().__init__()
        self.name = name
    
    def speak(self):
        return "Myavv"

class DoglyCat(Dog, Cat):
    pass
    def __repr__(self):
        return f"Its {self.name}, DoglyCat"
    
    def __str__(self):
        return f"Its DoglyCat named {self.name}"


bingo = Dog()
bingo.name = "Bingo!"
print(bingo.speak(), bingo.breathe(), bingo.name)

tom = Cat("Tom")
print(tom.speak(), tom.breathe(), tom.name)

polymorph = DoglyCat("Polly")
print(polymorph.speak(), polymorph.breathe(), polymorph.name)
print(polymorph)
