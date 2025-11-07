"""Приклад роботи з функціями як з об'єктами першого класу"""

# Створення посилання на об'єкт
out = print

# Тепер у змінних out і print посилання на той самий алгоритм,
# тому ми можемо використовувати out так само, як і print
out('Hello')

# Збереження посилань на функції у структурі даних

def add(x, y):
    return x + y


def sub(x, y):
    return x - y

# Використовуємо функції всередині словника як звичайні змінні
# ВАЖЛИВО: Після add і sub не стоять дужки "()", тому що наше завдання передати їх
# як змінні, а не викликати

operations = {
    '+': add,
    '-': sub
}

# За ключом словника отримуємо повноцінну функцію, яку одразу можна викликати
print(operations['+'](2, 3))
print(operations['-'](2, 3))
out()
out(operations['+'](2, 3))
out(operations['-'](2, 3))

add1 = lambda x, y: x + y
sub1 = lambda x, y: x - y

print(add1(3, 2))
print(sub1(3, 2))

square = lambda x: x ** 2
print(square(5))

#G
variable = 4
#LEGB
def make_closure():
    # Створили змінну
    variable = 40 + square(5) #enclose

    # Створили функцію, яка має доступ до змінної батьківської функції
    def closure():
        #variable = 2
        return variable #L

    # Повернули створену функцію з батьківської
    return closure


# Ми вже дізналися, що ми можемо зберігати функції у звичайних змінних. Зберігаємо отриману функцію змінну fn
fn = make_closure()

# Запускаємо отриману функцію та виводимо її результат
print(fn)
print(fn())
print(type(fn))


def make_powers(n):
    """Функція, яка повертає список функцій, кожна з яких обчислює
    ступінь аргументу, що дорівнює цьому індексу плюс 1
    (Неправильна реалізація)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x, i=i: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))




def make_powers_2(n):
    """Функція, яка повертає список функцій, кожна з яких обчислює
    ступінь аргументу, що дорівнює цьому індексу плюс 1
    (Неправильна реалізація)
    """

    functions = []

    for i in range(1, n + 1):
        def pow_x(x):
            y = i
            return x ** y
        pw = pow_x
        functions.append(pw)

    return functions


for function in make_powers_2(3):
    print(function(2))



def ordinary_add(x, y):
    """Звичайна функція"""
    return x + y


def curryied_add(x):
    """Карирована функція"""
    def do_add(y):
        return x + y

    return do_add

print(ordinary_add(2, 3))
print(curryied_add(2)(3))

print("*"*88)
add_to_five = curryied_add(5)

print(add_to_five(2))
print(add_to_five(3))

curryied_add = lambda x: lambda y: x + y
print(curryied_add(2)(3))

print("*"*88)

def forward_print(fn):
    """Приклад декоратору"""

    def decorated_fn(*args, **kwargs):
        """Модифікована функція"""

        print('Decorated function says:')
        x = fn(*args, **kwargs)  # виклик початкової функції
        print("++++++++++++++++++++++++")
        return x

    return decorated_fn

@forward_print
def hello():
    print('Hello!')


# Виклик декорованої функції
hello()

@forward_print
def ordinary_add(x, y):
    """Звичайна функція"""
    return x + y

print(ordinary_add(7,8))

def cast_result(type_):
    """Приклад створення декоратора з параметром"""

    def cast_decorator(function):
        """Сам декоратор"""

        def decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return type_(result)

        return decorated_function

    return cast_decorator


@cast_result(float)
def add(x, y):
    return x + y

print(add(2, 3))

n = add(5,7)
print(n)

import decimal


@cast_result(repr)
@cast_result(decimal.Decimal)
def div(x, y):
    return x / y


print(div(3, 2))
print(type(div(3, 2)))
n = div(3, 2)
print(n, type(n))