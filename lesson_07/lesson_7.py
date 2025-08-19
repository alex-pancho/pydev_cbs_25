
fruits = {"яблуко", "банан", "апельсин", "яблуко", "яблуко", "яблуко",}
print(fruits, type(fruits))
fruits.update(("good",))
print(fruits)
error_set = {"", 1, 2} # [1, 2]
print(error_set)

if "яблуко" in fruits:
    print("we have an apple!")

one_fruit = fruits.pop()
print("one_fruit:", one_fruit)
fruits.update(["good", "bad"])
fruits.remove("bad")
print("after remove", fruits)

fruits_2 = {"kivi", "mango", "papaya"}
fruits.update(fruits_2)
print("update", fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
    
logical_union = set1.union(set2)
# or
logical_union = set1 | set2
print("union", logical_union)

logical_intersection = set1.intersection(set2)
# or
logical_intersection = set1 & set2
print("logical_intersection", logical_intersection)

logical_difference_1_2 = set1.difference(set2)
# or
logical_difference_1_2 = set1 - set2
print("logical_difference_1_2", logical_difference_1_2)
logical_difference_2_1 = set2.difference(set1)
# or
logical_difference_2_1 = set2 - set1
print("logical_difference_2_1", logical_difference_2_1)

logical_symmetric_difference = set1.symmetric_difference(set2)
# or
logical_symmetric_difference = set1 ^ set2
print("logical_symmetric_difference", logical_symmetric_difference)

my_text = "Приклади створення множини в Python з інших типів даних за допомогою `set()`"
set_from_string = set(my_text)
print(set_from_string)
my_list = [1, 2, 3, 3, 4, 5, 6, 7, 6]
set_from_list = set(my_list)
print(set_from_list)
if len(my_list) != len(set_from_list):
    print("Has duplicate!")

numbers = [1, 2, 3, 4, 5]
squared_numbers = {x**2 for x in numbers}
print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_squared_numbers = {x for x in numbers if x % 2 == 0}
print(even_squared_numbers)

my_short_dict = {"key":"ключ", "go":"іти", "jump":"стрибати"}
my_long_dict = dict(key="yek", go="og", jump="pumj")
print(my_short_dict)
print(my_long_dict)
#int #float #str #bool #tuple

diff_for_dict = {(1, 2, 3): "Що ти робиш?", 3.141596: "pi"}
print(diff_for_dict)

# err_dict = {[1]: "asds"}
word_for_translate = "go"
print(f"\"{word_for_translate}\" Українською буде \"{my_short_dict[word_for_translate]}\"")
print(f"'jump' Українською буде '{my_short_dict['jump']}'")

user_data = {'name': 'Василь', 'age': 25, 'city': 'Київ'}
user_age = user_data['age']
print("user_data", user_age)
print("in", 'age' in user_data)

all_keys = user_data.keys()
all_vals = user_data.values()
all_dict = user_data.items()
print("****")
print(all_keys, type(all_keys))
print(all_vals)
print(all_dict)

for k in user_data:
    print(k, user_data[k])

for v in user_data.values():
    print(v)

for k, v in user_data.items():
    print(k, v)

my_dict_25 = {'ключ1':1, 'ключ2':2, 'ключ3':3}
my_dict_25.clear()
print(my_dict_25)

my_dict_27 = {'ключ1':1, 'ключ2':2, 'ключ3':3, 1: "asd", "key": ["abc", "asdf", {"a": "value"}], } # "неіснуючий ключ": "Kolya"
my_dict_27_copy = my_dict_27.copy()

# print(my_dict_27["неіснуючий ключ"])
un_exist_value = my_dict_27.get("неіснуючий ключ", "Olya")
print(un_exist_value)

get_pop_value = my_dict_27.pop("key")
print(get_pop_value)
get_pop_value_2 = my_dict_27.pop("неіснуючий ключ", ["a", "b", "cdef"])
print(get_pop_value_2)

my_dict_33 = {"неіснуючий ключ": ["a", "b", "cdef"]}
my_dict_27.update(my_dict_33)

print("updated dict", my_dict_27)

for key, value in my_dict_27.items():
    print(key, value)
    # del my_dict_27[key]
    # my_dict_27.pop(key)

list_tuple = [('ключ1', 'значення1'), ('ключ2', 'значення2'), ('ключ3', 'значення3')]
new_dict = dict(list_tuple)
print(new_dict)

list_list = [['ключ1', 'значення1'], ['ключ2', 'значення2'], ['ключ3', 'значення3']]
new_dict_2 = dict(list_list)
print(new_dict_2)

my_keys = ['ключ1', 'ключ2', 'ключ3']
my_vals = ['значення1', 'значення2', 'значення3']
new_dict_3 = dict(zip(my_keys, my_vals))
print(new_dict_3)

# {ключ_вираз: значення_вираз for змінна in ітерабельний_об'єкт}
# {x: x**2 for x in range(10) if x % 2 == 0}
# Результат: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

def is_ukrainian_name(name):
    # Множина українських букв + апостроф
    ukrainian_letters = set("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" +
                            "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'")

    # Перевірка, чи різниця множин порожня
    #  (тобто всі символи належать українським буквам)
    diff =  set(name) - ukrainian_letters
    return True if not diff else False

first_name = "Іван"
last_name = "Петренко-Jacson"
print(is_ukrainian_name(first_name))
print(is_ukrainian_name(last_name))

employees_data = {
    'Іваненко_Іван': ('Іван', 'Іваненко', 'Розробник', 2015),
    'Петренко_Ольга': ('Ольга', 'Петренко', 'Менеджер', 2018),
    'Коваленко_Михайло': ('Михайло', 'Коваленко', 'Дизайнер', 2017),
    # Додайте інші записи за потребою
}

# Додавання нового співробітника
employees_data['Міщенко_Анна'] = ('Анна', 'Міщенко', 'Інженер', 2019)

# Приклад пошуку за критерієм
def find_employees_by_position(position):
    # 2 це iндекс посади у кортежi данних спрiвробiтника
    return [emp_id for emp_id, emp_data in employees_data.items() if emp_data[2] == position]

# Пошук всіх розробників
developers = find_employees_by_position('Розробник')
print("Розробники:")
print(developers)

