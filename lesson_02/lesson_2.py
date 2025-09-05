
user_age = 18 
user_name = "Anna"
is_user_student = True # bool
PI = 3.141549
G = 9.8

long_quotes = '''Це
рядок з тикратним
повторенням лапок'''

my_list = [
    1, 
    2,
    3, 
    4,
    5, 
    6,
]

'''
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
'''

'''
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
'''
a = 5
b = 2
sums = a + b
diff = a - b
divs = a / b
div_int = a // b
div_rest = a % b
print("Math division", divs)
print("Int division", div_int)
print("Rest division", div_rest)

t1 = True
t2 = True
f1 = False
f2 = False

result = t1 and t2
print(result)
result2 = t1 and f1
print(result2)
result3 = f1 and t2
print(result3)
result4 = f1 and f2
print(result4)

print("*"*8)
result = t1 or t2
print(result)
result2 = t1 or f1
print(result2)
result3 = f1 or t2
print(result3)
result4 = f1 or f2
print(result4)

a = True
result = not a  # Результат: False

"""
(       )       [       ]       {       }
,       :       .       ;       @
"""
res = (2 + 3) * 4
print(res)

some_lst = [1, 2, res]
item = some_lst[0]
print("list item", item)

print(some_lst.__len__())
print(len(some_lst))

val1 = "VALue#1"; val2 = "valUE#2"

"""
    Обмеження цілих чисел у Python залежить від архітектури вашої системи.
    У зазвичай 32-бітних системах це може бути від 
    -2,147,483,648 до 2,147,483,647, 
    а на 64-бітних системах це може бути від 
    -9,223,372,036,854,775,808 до 9,223,372,036,854,775,807.
"""
bin_age = 0b11001001010111011
print("mr. Bin", bin_age)
hex_age = 0x0123456789abcdef
print("mr. Hex", hex_age)

a = 0.1 + 0.2
b = 0.3

print("a =", repr(a))
print("b =", repr(b))
print("a == b:", a == b)
print("Різниця (a - b):", a - b)

my_string = 'I\'m a Python fanatic'
my_second = 'A not very long string \
that spans two lines'

my_th ="""An even bigger \
string that spans \
three lines*"""
print(my_th)
print("part:", my_th[3:10])
print(len(my_th))

None

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
out = '{:-9} YES votes {:1.3%}'.format(yes_votes, percentage)
print(out)
print('%s YES votes %s' % (yes_votes, percentage))

query_sting = "підказка, що буде виведена на екран і повинна пояснити,\
 що ми очікуємо від користувача: "
# variable = input(query_sting)

verse = 'Йшов\n\tдощ\n\t\tі я'
print(verse)

for char in query_sting:
    print(char, end='*')
print()
a = "sjdhas"
b = "jjhhhhhh"
c = "21392839"
print(a, b, c, sep=" *** ")

n = 1
s = 2
# n = n + s
n += s
print(n)
