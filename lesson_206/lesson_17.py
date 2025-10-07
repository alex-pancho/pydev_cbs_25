
def my_iter():
    yield 1
    yield 2
    yield 1
    yield 4
    yield 6

m = my_iter()
print(m)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
try:
    print(next(m))
except StopIteration:
    print("stop")


# Створення ітератора для списку
my_iterable = iter([1, 2, 3, 4, 5])

# Прохід по ітератору вручну
print(next(my_iterable))  # Виведе: 1 my_iter.__next__()
print(next(my_iterable))  # Виведе: 2 my_iter.__next__()
print(next(my_iterable))  # Виведе: 3 my_iter.__next__()
print(next(my_iterable))  # Виведе: 4 my_iter.__next__()
print(next(my_iterable))  # Виведе: 5 my_iter.__next__()

# Помилка StopIteration при спробі отримати наступний елемент
try:
    print(next(my_iterable))
except StopIteration:
    print("StopIteration: Ітератор закінчився")

class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 2
            return self.current
        # else:
        #     self.current += 1
        #     return self.current
        else:
            raise StopIteration
        
my_iterator = MyIterator(6)
for num in my_iterator:
    print(num)


my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

print("FibonacciFibonacciFibonacciFibonacciFibonacciFibonacci")
class Fibonacci:

    def __init__(self, max, last1:int=1, last2:int=1):
        self.max = max
        self.last_numbers = (last1, last2)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        last_number, current_number = self.last_numbers
        last_number, current_number = current_number, last_number + current_number
        self.last_numbers = last_number, current_number
        self.count += 1

        if self.count > self.max:
            raise StopIteration
        
        return last_number


fibo = Fibonacci(10,) # 987, 1597

for number in fibo:
    print(number)

def fibonacci_generator(last1:int=1, last2:int=1):
    a, b = last1, last2
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))

print("call a", next(fib))

squares_generator = (x ** 2 for x in range(10))

for square in squares_generator:
    print(square)

print("call b", next(fib))

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# Створюємо генератор
counter = count_up_to(5)

for i in counter:
    print(i)

# print(next(counter))

cnt = count_up_to(5)
print(*cnt)
cnt = count_up_to(5)
print(list(cnt))
cnt = count_up_to(5)
print(tuple(cnt))
cnt = count_up_to(5)
print(set(cnt))

a = [1, 2, 3]
b = ["a", "b", "c"]
get_zipped = zip(b, a)
print(list(get_zipped))

get_map = map(sum, [[1, 1, 1], [1, 4], [-1, 1]])
print(*get_map)
get_map = map(sum, [[1, 1, 1], [1, 4], [-1, 1]])
print(list(get_map))
