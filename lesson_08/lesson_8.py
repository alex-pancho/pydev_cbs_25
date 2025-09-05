"""
=======================
Head
=======================
Conent for output
=======================
"""

def line_for_break(counter:int) -> str:
    output = "=" * counter
    return output

print(line_for_break(5))
print(line_for_break(40))

repeat_number = 20
text_for_output = f"""
{line_for_break(repeat_number)}
Head
{line_for_break(repeat_number)}
Conent for output
{line_for_break(repeat_number)}
"""

print(text_for_output)
print(print())

def without_return():
    a = 1 + 1
    return a

a = without_return()
print(a)

def appendix(a:int, b:int) -> int:
    """Append two nubers

    Args:
        a (int, float): First number
        b (int, float): Second number
    """
    return a + b

print("return for appendix(a, b), a=2, b=3.5: ", appendix(2, 3.5))

def line_for_break(counter:int, separator:str = "="):
    """"""
    output = separator * counter # "="
    return output

print(line_for_break(counter=repeat_number, separator="*"))

def print_args(*args):
    if 3.14 in args:
        print("pi")
    for arg in args:
        print(arg)

print_args(1, "hello", 3.14, [1, 2, 3])

# *a, = [1, "hello", 3.14, [1, 2, 3]]
# print(a)
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Приклад виклику функції
print_kwargs(name="John", age=25, city="New York",)

def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("==")
print_args_and_kwargs(1, "hello", 3.14, name="John", age=25, city="London")
print("==")
print_args_and_kwargs()
print("==")
print_args_and_kwargs(1, "hello", 3.14)
print("==")
print_args_and_kwargs(name="John", age=25, city="London")
print("==")

def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")  # Hello, Alice!
greet(greeting="Good morning", name="Bob")  # Good morning, Bob!

def describe_person(name, age, country="Unknown"):
    print(f"{name} is {age} years old and is from {country}.")
    
describe_person("Alice", 30)
describe_person("Bob", 25, country="USA")
describe_person("Cindy", 32, "Ukraine")

def int_square(x:int):
    return x ** 2

square = lambda x: x ** 2
append = lambda x, y: x + y
print(square(5))
print(append(3, 7))

print(all([1,2,3]))
print(all([1,0,3]))

print(any([1,2,3]))
print(any([0,2,0]))
print(any([0,0,0]))

# callable(Classname)
print(ascii("Україна"))
print(chr(1111))
print(ord("ї"))

code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
    '''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)

print(divmod(5, 3))

expression = "3 + 5 * 2"
print(eval(expression))  # 13

x = 10
y = 20
print(eval("x + y"))
value1 = "abc"
value2 = "DEF"

formatted_string = "Some text {} and {}.".format(value1, value2)
print(formatted_string)
print(hash(formatted_string))
# print(hash(["Hello", "World!"])) # TypeError: unhashable type: 'list'

print(id(formatted_string))

# value = input("Input value:")
x = 3.15
print(isinstance(x, (int, float)), type(x))

print(len("len"))
print(max([3, 1, 4]))
print(min([3, 1, 4]))

my_dict = {'apple': 5, 'banana': 10, 'kiwi': 3, 'orange': 8}
# Знаходження ключа з максимальним значенням
max_key = max(my_dict, key=lambda k: my_dict[k])
print(max_key)
max_value = max(my_dict.values())
print(max_value)
print(pow(3, 3), 3**3)
print()
print(range(5))
print(list(reversed([10, 2, 4])))
print(round(2.610))
print(round(2.590, 1))
print(round(2.430))
lis_sort = sorted([10, 2, 4])
print(lis_sort)
print(sum([1,1,1]))

def if_a(my_list:list):
    if "a" in my_list:
        my_list.remove("a")
    return my_list

def_list = [1, 3, 9, "s", "a"]
new = if_a(def_list)
print("new", new)
print("def_list", def_list)

num_dict = dict(enumerate(my_dict))
print(num_dict)
