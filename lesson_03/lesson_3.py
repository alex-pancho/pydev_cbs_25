
user_age = 18 #int(input('user_age = '))

# Якщо число x більше п'яти, то буде видано
# відповідне повідомлення

if user_age >= 50:
    print("you are old old boy")
elif user_age >= 18:
    print("you are adult")
elif user_age < 0:
    print("wrong age input")
else:
    print("you are children yet")
print("end")

is_ready = True

# if is_ready:
#     print('Ready')
# else:
#     print("Not yet")
state_msg = 'Ready' if is_ready else "Not yet"
print(state_msg)

# "Alex" # True
# [] # True
# 7 # True
# 0.000 # False 

False == "", [], (), {}, 0, 0.0 # None

user_name = input('Enter your name: ')

if user_name:
    print(f"Hello {user_name}!")
else:
    print("Enter name, pls")

user_age = input('user_age = ')
if user_age:
    if user_age.isdigit():
        # add somth
        user_age = int(user_age)
    else:
        # add number 2
        print("Enter age, int pls")
else:
    # add 3
    print("Enter age, int pls")

value = None

if value is not None: #  value == None !! CANT DO IT !!!
    pass # add logic

result = 5 if 4 > 3 else 0  # ternary operator; equals to 5
print(result)

result2 = 5 if 3 > 4 else 0  # ternary operator; equals to 0
print(result2)

day = int(input('Введіть номер дня тижня:'))

if day == 1:
    print('понеділок', 'Початок робочого тижня')
elif day == 2:
    print('вівторок', 'Другий робочий день')
elif day == 3:
    print('середа', 'маленка п\'ятниця')
elif day == 4:
    print('четвер', 'передост робочий день')
elif day == 5:
    print('п\'ятниця', 'це вона!!! робочий день')
else:
    print("Щось вихідне")

match day:
    case 1:
        print('понеділок', 'Початок робочого тижня')
    case 2:
        print('вівторок', 'Другий робочий день')
    case 'середа':
        print('Середина тижня')
    case 'субота' | 'неділя':
        print("Щось вихідне")
    case _:
        print("Щось непонятне")
