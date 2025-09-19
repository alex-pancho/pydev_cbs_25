

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
    engine_status = False

    def __init__(self, brand, model, wheels=4):
        self.brand = brand
        self.model = model
        self.wheels = wheels
        # self.engine_status = False
    
    def engine_key(self):
        print("Зміна стану двигуна викликана")
        self.engine_status = not self.engine_status

my_3_car = Car("Nissan", "Patrol", 5)
print("my_3_car", my_3_car.brand, my_3_car.model, my_3_car.wheels)
print("my_3_car engine",my_3_car.engine_status)
my_3_car.engine_key()
print("my_3_car engine afr call engine_key",my_3_car.engine_status)

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