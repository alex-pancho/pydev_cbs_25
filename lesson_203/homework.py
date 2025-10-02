from PIL import Image, ImageDraw

"""
Завдання 1 
Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази 
відповідно "Hello from Base" та "Hello from Child".
"""
class Base():
      
    def method(self):
        return "Hello from Base"
      
class Child(Base):
      
    def method(self):
        return "Hello from Child"
      
my_base = Base()
my_child = Child()

print(my_base.method())
print(my_child.method())

"""
Завдання 2 
Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від 
класу Shape. Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма 
методами. В результаті повинно з’явитися зображення. Перегляньте їх. 
"""


class Shape:
    def __init__(self):
        # Колір тла
        self.back_color = (155, 213, 117, 100)
        # Створюємо зображення 500 * 500
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)
        print("Shape self.im id", id(self.im))
        print("Shape self.draw1 id", id(self.draw1))
 
    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Cone(Shape):
  
    def __init__(self, height, diametr):
        super().__init__()
        self.height = height
        self.diametr = diametr
             
        print("Cone self.im id", id(self.im))
        print("Cone self.draw1 id", id(self.draw1))
        print(self.im.width, self.im.height)
 

    def draw(self):
       
        cone_top = [self.im.width//2, 50]  
        
        elips_box = [cone_top[0]-self.diametr//2, cone_top[1]+self.height-50, cone_top[0]+self.diametr//2, cone_top[1]+self.height+50]  
        


        self.draw1.line([cone_top, (cone_top[0]-self.diametr//2, cone_top[1]+self.height)], fill=(255, 255, 255))#"black")
        self.draw1.line([cone_top, (cone_top[0]+self.diametr//2, cone_top[1]+self.height)], fill=(255, 255, 255))#"black")

        self.draw1.ellipse(elips_box, outline=(255, 255, 255))

         
    # def erase(self):
    #     self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)
        
    def save(self):
        print("Image with Cone was created")
        return self.im.save('draw-cone.png', quality=95)
    

class Paraboloid(Cone):

    def __init__(self, height, diametr):
        super().__init__(height, diametr)
        # self.height = height
        # self.diametr = diametr
        print("Paraboloid self.im id", id(self.im))
        print("Paraboloid self.draw1 id", id(self.draw1))
        print(self.im.width, self.im.height, self.height, self.diametr)

    def draw(self):
     
        # print("Paraboloid self.im id", id(self.im))
        # print("Paraboloid self.draw1 id", id(self.draw1))
        # print(self.im.width, self.im.height)
        
        radius = self.diametr//2
        paraboloid_top = [self.im.width//2, 50]  
    
        line_coordinates = []
        for x in range(0, radius+1):
            y_pos = ((x//7)**2)## можна міняти формулу, якщо збільшувати число на яке ділимо тоді парабола розширюється і навпаки
            if y_pos > self.height:

                break
            line_coordinates.append(y_pos)

        line1_begin = paraboloid_top
        line2_begin = paraboloid_top
        
        for x in range(0, len(line_coordinates)):
            line1_end = [paraboloid_top[0]+x, paraboloid_top[1] + line_coordinates[x]]
            self.draw1.line([line1_begin, line1_end], fill=(255, 255, 255))
            
            line2_end = [paraboloid_top[0]-x, paraboloid_top[1] + line_coordinates[x]]
            self.draw1.line([line2_begin, line2_end], fill=(255, 255, 255))
           
            line1_begin = line1_end
            line2_begin = line2_end
            
        elips_box = [line2_begin[0], line2_begin[1]-50, line1_begin[0], line1_begin[1]+50]  
        self.draw1.ellipse(elips_box, outline=(255, 255, 255))

    def save(self):
        print("Image with Paraboloid was created")
        return self.im.save('draw-paraboloid.png', quality=95)


class Circle(Shape):
    def draw(self):
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    def draw(self):
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    def draw(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


def work_with_obj(obj):
    obj.draw()
    obj.save()


def update_obj(obj):
    obj.erase()
    obj.save()


def menu():
    while True:
        value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
                          '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
                          '8. Cтворити конус\n\t9. Cтворити параболоід\n\t0. Вихід з програми\nОберіть необхідний пункт меню: '))
        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                c = Circle()
                update_obj(c)
            case 6:
                sq = Square()
                update_obj(sq)
            case 7:
                t = Triangle()
                update_obj(t)
            case 8:
                height = 300
                diametr = 300
                cone = Cone(height, diametr)
                work_with_obj(cone)
            case 9:
                height = 300
                diametr = 300
                paraboloid = Paraboloid(height, diametr)
                work_with_obj(paraboloid)
            case 0:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


menu()

"""
Завдання 3 
Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані? 
Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set). 
"""

class Car:
    def __init__(self, brand, model, car_mileage=0):
        self.brand = brand         
        self.model = model        
        self.year = 2022 
        self.__car_mileage = car_mileage    # пробіг 
        self.__engine_status = False    # стан двигуна   
        
    def __str__(self):
        return f"Авто: Бренд:{self.brand}, Модель:{self.model}, Пробіг: {self.__car_mileage}"      
        
    def engine_key(self):
        print("Зміна стану двигуна викликана")
        self.__engine_status = not self.__engine_status
        
    def get_mileage(self):
        return self.__car_mileage

    def set_mileage(self, new__car_mileage):
        if new__car_mileage >= self.__car_mileage:  
            self.__car_mileage = new__car_mileage
            print(f"Зміна пробігу")
        else:
            print("Помилка: пробіг не може зменшуватись!")

my_car = Car("Nissan", "Patrol")
print(f"Пробег: {my_car.get_mileage()}")
my_car.set_mileage(100)
print(f"Пробег: {my_car.get_mileage()}")
my_car.set_mileage(50)
print(f"Пробег: {my_car.get_mileage()}")
print(my_car)


"""
Завдання 4 
Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). 
Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії 
цих двох об'єктів в одній функції (функція hello_friend).
"""

class Eng_language:
    def greeting(self):
      return "Hello frind!"
      
class Ukr_language:
    def greeting(self):
        return "Привіт друже!"

def hello_friend(language):
    print(language.greeting())


eng = Eng_language()
ukr = Ukr_language()

hello_friend(eng)  
hello_friend(ukr)
print()


"""
Завдання 5 
Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як 
властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і 
дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть 
бути задані в одній шкалі, а отримані в іншій. 
"""

class Temperature:
    def __init__(self):
        self._t_celsius = None 
        self.__t_farenheit = None  
    
    @property
    def t_celsius(self):
        return self._t_celsius

    @t_celsius.setter
    def t_celsius(self, value):
        self._t_celsius = value
        self.__t_farenheit = (self._t_celsius * 9 / 5) + 32 

    @t_celsius.deleter
    def celsius(self):
        self._t_celsius = None 
        self.__t_farenheit = None  

    
    @property
    def t_farenheit(self):
        return self.__t_farenheit

    @t_farenheit.setter
    def t_farenheit(self, value):
        self.__t_farenheit = value
        self._t_celsius = (value - 32) * 5 / 9

    @t_farenheit.deleter
    def t_farenheit(self):
        self._t_celsius = None 
        self.__t_farenheit = None  



t = Temperature()

print(f"Тепература в цельсіях {t.t_celsius} C")       
print(f"Тепература в фаренгейтах {t.t_farenheit} F")   
print()

t.t_celsius = 100
print(f"Тепература в цельсіях {t.t_celsius} C")       
print(f"Тепература в фаренгейтах {t.t_farenheit} F")       
print()

t.t_farenheit = 100
print(f"Тепература в цельсіях {t.t_celsius} C")       
print(f"Тепература в фаренгейтах {t.t_farenheit} F")      
print()

del t.t_farenheit
print(f"Тепература в цельсіях {t.t_celsius} C")       
print(f"Тепература в фаренгейтах {t.t_farenheit} F")       
