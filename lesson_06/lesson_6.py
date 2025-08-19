
empty_tuple = () # tuple()
numers_and_str_tuple = (24, 42 , "asert", "DE VSI??", 1.33, ("vvv", 12133543), True, 42.0, 42,)

for i in numers_and_str_tuple:
    print(i)

print("len", len(numers_and_str_tuple))

numers_and_str_tuple = (*numers_and_str_tuple, 1234)
print(numers_and_str_tuple)
mixed_tuple_rare_form = 1, 'hello', 3.14, True
print(mixed_tuple_rare_form)

print(numers_and_str_tuple[3][1]) #
my_long_str = "використовується для підрахунку кількості входжень певного значення в кортежі." \
    " Вона повертає кількість разів, як це значення зустрічається в кортежі"
print("count K", my_long_str.count("к"))

print("count 42", numers_and_str_tuple.count(42))
print("вход" in my_long_str)
print("asert" in numers_and_str_tuple)
print("vvv" in numers_and_str_tuple)

print("index for 'asert'", numers_and_str_tuple.index("asert"))
if "vvv" in numers_and_str_tuple:
    print("index for 'vvv'", numers_and_str_tuple.index("vvv")) # raise Except if element is missing
          # 0, 1, 2, 3, 4, 5, 6, 7   
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
subtuple = my_tuple[2:7] # зріз
print(subtuple)
subtuple = my_tuple[2:7:2] # зріз і крок
print(subtuple)
a, b, c = (10, 20, 30)
print(a, b, c)
*a, b = (10, 20, 30, 40, 21, 1212)
print(a, b)

my_string = "Привіт, світ!"
tuple_from_string = tuple(my_string)

# Виведення кортежу
print(tuple_from_string)

my_list = [1, 2, 3, 'Python', True]
tuple_from_list = tuple(my_list)

# Виведення кортежу
print(tuple_from_list)

my_dict = {"key":'val', "key2":"val2"}
tuple_from_dict = tuple(my_dict.items())

# Виведення кортежу
print(tuple_from_dict)

my_set = {1, "asasa", 3, "sdds"}
tuple_from_set = tuple(my_set)

# Виведення кортежу
print(tuple_from_set)

my_list = [1, 2, 3, 'a', 'b', 'c']

for i in my_list:
    print(i)

print("len my_list", len(my_list))
print(my_list[0], my_list[-1])

my_long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sub_list = my_long_list[2:8]
print(sub_list)
sub_list_2 = my_long_list[2:8:2]
print(sub_list_2)
rev_list = my_long_list[::-1]
print(rev_list)

my_list = [1, 2, 3]
print(id(my_list))
my_list.append(4)
my_list.append("aaa")
print(my_list, id(my_list))
my_list.append((1, 2, 3))
my_list.append(["aa", 14.23, "bb king"])
print(my_list)
my_list.extend("aaa")
my_list.extend((1, 2, 3))
my_list.extend(["aa", 14.23, "bb king", [1, 2]])
print(my_list)

my_list.insert(4, 4)
print(my_list)
my_list.insert(4,"asd")
print(my_list)

my_list.remove(2)
print(my_list)

popped_element = my_list.pop(1)
print(my_list)
print(popped_element)

index_of_2 = my_list.index(2)
print("index_of_2:", index_of_2)

count_of_a = my_list.count("a")
print(count_of_a)

numbers = [1, 2, 3, 4, 5]
# Розпакування списку за допомогою *
first, *middle, last = numbers
# *first, middle, last = numbers
# first, middle, *last = numbers

# Виведення результатів
print("Перший елемент:", first)         # Перший елемент: 1
print("Серединні елементи:", middle)    # Серединні елементи: [2, 3, 4]
print("Останній елемент:", last)        # Останній елемент: 5

numbers = [5, 2, 8, 1, 3,]
numbers.sort()
print("Список, відсортований на місці:", numbers)
words = ["яблуко", "апельсин", "банан", "груш", "слива"]
sorted_w = sorted(words, key=lambda x: len(x), reverse=True)
print("сортед ліст", sorted_w)
print("words", words)

my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

my_dict = {"key":'val', "key2":"val2"}
list_from_dict = list(my_dict)
print(list_from_dict)

squares = [x**2 for x in range(10)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
word_lengths = [len(word) for word in words]
print(word_lengths)
