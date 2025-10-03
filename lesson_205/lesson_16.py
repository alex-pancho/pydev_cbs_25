

class TooLargeValueError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f"Значення {value} перевищує ліміт {limit}"


print(dir(TooLargeValueError(1000, 100)))
some_obj = TooLargeValueError(1000, 100)

print(dir(print))

# <class 'type'>
print(type(object))
# <class 'type'>
print(type(type))
# <class 'type'>
print(type(float))
# <class 'float'>
print(type(7.5))


class MyClass(object):
    pass


# <class 'type'>
print(type(MyClass))
# <class '__main__.MyClass'>
print(type(MyClass()))
# True
print(isinstance(object, object))
# True
print(isinstance(type, object))

"""Виклик type() з одним аргументом дозволяє отримати тип зазначеного[аргументом] об'єкта (зазвичай повертається той же
тип, що зберігається в атрибуті об'єкта __class__). Для перевірки відповідності типу об'єкта якому - або типу (або
декільком) рекомендується скористатися функцією isinstance(), з огляду на того що вона приймає до уваги ієрархію типів.
"""

my_var = 1.4
# <type 'float'>
print(type(my_var))

"""У версії Python 2.2 та вище виклик type() з трьома аргументами дозволяє сконструювати н
овий об'єкт типу во час виконання.
"""

# Визначення типу за допомогою інструкції
# Для Python 2 - MyType(object)


class MyType:
    x = 1.5


# Те саме визначення типу, але під час виконання за допомогою type()
MyType = type('MyType', (object,), {'x': 1.5})
print(MyType)
print(type(MyType()))
print(MyType.x)

class Item():

    def __init__(self, name):
        self.item = name

class Homepage():

    button = "//button"
    password = "//input[@class='password']"

#homepage = Homepage().password.item()

class MyClass:
    my_attr = 1


m_c = MyClass()
m_c.my_attr = 54
print(hasattr(m_c, 'my_attr'))
print(m_c.my_attr)
delattr(m_c, 'my_attr')
print(hasattr(m_c, 'my_attr'))
print(m_c.my_attr)

class Student:
    surname = 'Ivanov'
    name = 'Ivan'
    marks = 95


person = Student()

surname = getattr(person, 'surname')
# Ivanov
print(surname)

name = getattr(person, 'name')
# Ivan
print(name)

marks = getattr(person, 'marks')
# 95
print(marks)
some = hasattr(person, 'some')
print(some)

class MyCls1():
    pass

class MyCls2(MyCls1):
    pass

print("MyCls1(), MyCls1", isinstance(MyCls1(), MyCls1))

print("MyCls2(), MyCls1", isinstance(MyCls2(), MyCls1))
print("type(MyCls1())", type(MyCls1()) == MyCls1)
print("type(MyCls2())", type(MyCls2()) == MyCls1)
print(issubclass(MyCls1, MyCls2))
print(issubclass(MyCls2, MyCls1))


magazines = [
    {"name": "Space", "volume": 20000, "price": 12.45},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Fortune", "volume": 10000, "price": 17.99},
    {"name": "Vouge", "volume": 25000, "price": 7.68},
]

def avg_price(magazines: list, volume: int = 10000):
    prices = [] # False
    for mag in magazines:
        if mag["volume"] > volume:
            price = mag.get("price", 0)
            prices.append(price)
    avg = 0
    if prices:
        # sum = 0
        # for p in prices:
        #     sum += p
        avg = sum(prices)/len(prices)
    return avg


print(avg_price(magazines))