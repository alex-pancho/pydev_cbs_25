# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unuque_num = []
for num in small_list:
    if num not in unuque_num:
        unuque_num.append(num)
print(f"\ntask 1.\nвсi унікальні елементи в списку small_list: {unuque_num}")
print()


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

arithmetic_mean = sum(small_list) / len(small_list)
print(f"task 2.\nсереднє арифметичне всіх елементів у списку small_list: {arithmetic_mean:.2f}")
print()


# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

dubl_big_list = set(dub for dub in big_list if big_list.count(dub) > 1)
print(f"task 3.\nдублiкати в списку big_list: {dubl_big_list}")
print()

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

max_key = None
max_value = None
for key, value in add_dict.items():
    if max_value is None or value > max_value:
        max_key = key
        max_value = value

print(f"task 4.\nключ з максимальним значенням у словнику: {max_key}, {max_value}")
print()

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})

new_dict = {v: k for k, v in base_dict.items()}
print(f"task 5.\nновий словник: {new_dict}")
print()

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = {**base_dict, **add_dict}
sum_dict_value_list = list(sum_dict.values())
sum_dict_value_str = [str(item) for item in sum_dict_value_list]
sum_dict_value = "".join(sum_dict_value_str)
print(f"task 6.\n{sum_dict_value}")
print()

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_line = set(line)
print(f"task 7.\n{new_line}")
print()

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

set_3 = set_1 ^ set_2
sum_set = sum(set_3)
print(f"task 8.\n{sum_set}")
print()

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

list_3 = set(list_1) ^ set(list_2)

print(f"task 9.\n{list_3}")
print()


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

new_person_dict = {}

for key, value in person_list:
    min_age = (value // 10) * 10
    max_age = min_age + 9

    new_key = f"{min_age}-{max_age}"
    
    if new_key not in new_person_dict:
        new_person_dict[new_key] = []
    new_person_dict[new_key].append(key)

new_person_dict_ord = dict(sorted(new_person_dict.items()))

print(f"task 10.\n{new_person_dict_ord}")
print()

