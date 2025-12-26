"""
**Генератори:**

1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""

def even_numbers_generator1(max_number):
    for i in range(0, max_number + 1, 2):
        yield i

max_number = 20
even_number_list1 = []
for number in even_numbers_generator1(max_number):
    even_number_list1.append(number)
print("List of even number 1: ", even_number_list1)
###########################################################

even_numbers_generator2 = (x for x in range(0, max_number + 1, 2))
even_number_list2 = []
for number in even_numbers_generator2:
    even_number_list2.append(number)
print("List of even number 2: ", even_number_list2)
###############################################################

def even_numbers_generator3(max_number):
    return  list(x for x in range(0, max_number + 1, 2))

even_number_list3 = even_numbers_generator3(max_number)
print("List of even number 3: ", even_number_list3)

##################################################################

"""
2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""
def fib_generator(max_number):
    a, b = 0, 1
    while a < max_number:
        yield a
        a, b = b, a + b

max_number = 100
fib_list = []
for number in fib_generator(max_number):
    fib_list.append(number)
print(f"List of Fibonacci  until number {max_number}:  {fib_list}")

"""

**Ітератори:**

1. Реалізуйте ітератор для зворотного виведення елементів списку.

"""

class ReverseIterator:
    def __init__(self, in_data):
        if not isinstance(in_data, list):
            raise TypeError("Input must be list")
        self.data = in_data
        self.out_index = len(in_data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.out_index == 0:
            raise StopIteration
        self.out_index -= 1
        return self.data[self.out_index]

my_num_list = [1, 2, 3, 4, 5]
print(f"Reverse list of list {my_num_list}: ", end=" ") 
for item in ReverseIterator(my_num_list):
    print(item, end=" ") 

print()

"""
2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""

class EvenNumbers:
    def __init__(self, max_number):
        if not isinstance(max_number, int) or max_number < 0:
            raise ValueError("Incorrect input max_number value. must be int and >= 0")
        self.n = max_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
    

max_number = 20
print(f"Even number list until number {max_number}:: ", end=" ") 
for num in EvenNumbers(max_number):
    print(num, end=" ")