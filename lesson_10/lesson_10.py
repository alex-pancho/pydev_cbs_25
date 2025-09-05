import typing
from subprocess import Popen, PIPE

# from foo import (
#     azz, 
#     buzz, 
#     clazz, 
#     jazz, 
#     zazz
# )

def long_function_name(var_one, var_two, var_three, var_four): # i can add some
    # long part of comment
    print(var_one)


def long_function_name(
        var_one, var_two, var_three,
        var_four,
    ):
    print(var_one)


def long_function_name(
        var_one,
        var_two,
        var_three,
        var_four,
    ):
    print(var_one)
    print(var_two)

    if var_three:
        print(var_four)
    
    return var_four


class MyClass():

    def func_1(self):
        pass

    def func_2(self):
        pass


if __name__ == "__main__":
    print("hello")
    print()
