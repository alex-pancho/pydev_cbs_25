import re

string = "Test1 Text2 Test3 Tost4 Tist5 TTTttt"

# re.match(pattern, string) - призначений для пошуку за заданим шаблоном на початку рядка
pattern = r"T..t"
pattern_ext = r"T..t\d?"
pattern_all = r"T[a-z]*t\s?"
result = re.match(pattern, string)
print(result)
# метод group() повертає фрагмент рядка, в якому було виявлено збіг
print(result.group(0))

# поле string поверне рядок, який передавали для пошуку
print(result.string)

# метод span() поверне кортеж, який містить початкову та кінцеву позиції шуканого фрагмента
print(result.span())

# Позиція початку шаблону у рядку
print(result.start())

# Позиція кінця шаблону в рядку
print(result.end())

# Результат – None, т.к. фрагмент знаходиться не спочатку
result1 = re.match(r"Test2", string)
print(result1)


pattern_new = r"Test3"

result_search = re.search(pattern_new, string)
print(result_search)
# метод group() повертає фрагмент рядка, в якому було виявлено збіг
print(result_search.group(0))
# print(result_search.group(1)) # IndexError: no such group

result_all = re.findall(pattern, string)
print(result_all, type(result_all))

result_all_2 = re.findall(r"fhgfjg", string)
print(result_all_2)

for match in re.finditer(pattern, string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    # Виводимо кожен знайдений результат:
    print(s)

mach = re.finditer(pattern, string)
print(*mach)

result = re.sub(r"t", "T", string)
print(result)

result = re.sub(r"I", "A", string)
print(result)

# re.split(pattern, string, [maxsplit=0]) - призначений для поділу рядка за заданим шаблоном
# Стільки поділів, скільки це можливо
result = re.split(r"t", string)
print(result)

result = re.split(pattern, string,) # maxsplit=3
print(result)

pattern = re.compile("T")
result1 = pattern.findall(string)
print(result1)

result_all = re.findall(pattern_all, string)
print(result_all, type(result_all))

phone_number_pattern = re.compile('\(\d{3}\) \d{3}-\d{4}') #"\(\d{3}\)\s?(\d{3}-\d{4}|\d{3}-?\d{2}-?\d{2})"

ph_string = """
(123) 456-7890
(097) 456-7890
(099) 456-7890
(080) 456-7890
(080)45678-90
(080)456-7890
(080) 456-78-90
"""
phones = phone_number_pattern.findall(ph_string)
print(phones)

email = "user@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Email введено правильно.")
else:
    print("Некоректний формат email.")


pattern1 = '^L{0,3}(CM|CD|D?C{0,3})(XC|XL|M?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern1, 'LDMV'))

pattern2 = """
    ^ - start
    L{0,3}
    (CM|CD|D?C{0,3})
    (XC|XL|L?X{0,3})
    (IX|IV|V?I{0,3})
    $ - end
    """
print(pattern2)
print(re.search(pattern2, 'LDV', re.VERBOSE))

# Використання прапора компіляції
re.compile('''
           [\w\.-]+
           @
           [\w\.-]+'
           ''',
           re.VERBOSE)

