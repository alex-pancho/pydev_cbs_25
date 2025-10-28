import math
import json
import random
import re
import os
import sys

from datetime import datetime 
from collections import OrderedDict
from urllib import request

# from mymodule...

def func_a():
    return datetime.now()

def func_b(a=25):
    return math.sqrt(a)

def some_extra_long_and_wery_long_named_function():
    return random.randint(1, 10)

def make_os():
    return os.name

__all__ = [
    func_a, 
    func_b, 
    some_extra_long_and_wery_long_named_function
]

if __name__ =="__main__":
    print(make_os())
    print(sys.version)
    data = '{"name": "John", "age": 30, "city": "New York"}'
    parsed_data = json.loads(data)   # перетворюємо словних у json
    print(parsed_data)
    my_dict = {'a': 1,  'c': 3, 'b': 2,}
    # у впорядкованому словнику значення завджи зберігаються у заданому порядку
    ordered_dict = OrderedDict(my_dict) 
    print(ordered_dict)
    print(dir(ordered_dict))

    print(dir(__builtins__))

    print(json.__file__)
