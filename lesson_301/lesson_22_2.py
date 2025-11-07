"""Приклад використання функції map"""

string = '2 4 8 15 42'
numbers = map(int, string.split())
print(next(numbers))
print(next(numbers))
print(list(numbers))
numbers = map(int, string.split())
print(tuple(numbers))
numbers = map(int, string.split())
print(*numbers)

"""Приклад використання функції filter"""

numbers = [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
positive_numbers = filter(lambda x: x > 0, numbers)
print(positive_numbers)
print(type(positive_numbers))
print(next(positive_numbers))
print(list(positive_numbers))
print(type(positive_numbers))

"""Приклад використання функції reduce"""

from functools import reduce

numbers = [3, 2, 1, 8, -3, -2]
# Добуток усіх чисел списку
product = reduce(lambda x, y: x * y, numbers)

print(product)

"""Приклад використання функції модуля lru_cache functools"""

from functools import lru_cache

# Тут функцію обчислення чисел Фібоначчі записано рекурсивно, але по
# продуктивності та витрати пам'яті вона буде порівнянна з нерекурсивною

# @lru_cache(maxsize=None)
# def fibonacci(index):
#     if index < 2:
#         return 1
#     else:
#         return fibonacci(index - 1) + fibonacci(index - 2)


# for i in range(1, 100):
#     print(fibonacci(i))

"""Приклад використання функції partial модуля functools"""

from functools import partial

# Часткове застосування функції
print_with_comma = partial(print, sep=', ')

print_with_comma(2, 3, 5)

"""Приклад використання комбінаторних генераторів модуля itertools"""

from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('ABC', 2)))
print()

print(list(combinations('ABC', 2)))
print()

print(list(combinations_with_replacement('ABC', 2)))

"""Приклад використання функції chain модуля itertools"""

from itertools import chain

for i in chain(range(2), range(3)):
    print(i)

"""Приклад використання функції product модуля itertools"""

from itertools import product

for a, b in product(range(2), range(3)):
    print(a, b)

print("""Прикладом використання функцій є прийняття і зупинення while модуля itertools""")

from itertools import takewhile, dropwhile

numbers = [1, 4, 3, 2, 88, 23, 4, 5, 4, 1]
predicate = lambda x: x < 5

for value in takewhile(predicate, numbers):
    print(value)

print()

for value in dropwhile(predicate, numbers):
    print(value)
