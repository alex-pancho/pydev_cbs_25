from typing import Union


# def print(*args):
#     return None


def add_a(a, b):
    """Return the sum of two numbers."""
    return a + b


def add_b(a: int | float, b: int | float) -> int | float:
    """
    Return the sum of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        (int or float): Sum of a and b.
    """
    return a + b


def add_c(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Return the sum of two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.

    Returns
    -------
    int or float
        Sum of the two numbers.
    """
    return a + b


def get_info(error: False):
    """
    Get info if hasnt error
    Call without error == True
    """
    if error:
        print(get_info.__doc__)


get_info(True)

# LEGB
a = 10  # G


def pum_a():
    a = 7  # E

    def print_a():
        a = 5  # L
        print(a)

    print_a()


b = 25


def print_b():
    # a = 5
    global b
    if a > 1:
        b = 20
    print(a)


pum_a()
print_b()
print("b:", b)
# 5! 2*3*4*5
# import sys
# sys.setrecursionlimit(20000)  ### DANGER !!!!!


def factorial(n: int) -> int:
    if n <= 1:  # базовий випадок
        return 1
    return n * factorial(n - 1)  # рекурсивний виклик


print(factorial(10))

list_of_lists = [1, [2, [3, 4]], 5, [[[["a"]], "b"]]]


def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # рекурсія
        else:
            result.append(item)
    return result


out_flat = flatten(list_of_lists)
print(out_flat)
