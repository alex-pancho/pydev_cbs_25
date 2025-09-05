my_text = "Якась послідовність символів"
print(len(my_text), id(my_text))

my_text = my_text + "."
print(len(my_text), id(my_text))

print(my_text[0])
print(my_text[1])
print(my_text[5])
print(my_text[-1])
print(my_text[-2])

for t in my_text:
    if t == " ":
        continue
    print(t, end="")

print()
print(my_text[0:6])
print(my_text[2:12])
print(my_text[2:22:2])
print(my_text[::-1])

a = "a"
b = "b"
ab = a + b
print(ab)
joined = ".".join(("ujk", "dfer", "reye", "adsfw"))
print(joined)

parts = my_text.split()
print(parts)
sppplitted = joined.split(".") # 
print(sppplitted)

line = "apple,orange,banana,grape"
parts = line.split(',', 2)
print(parts)

my_new_text = "Dive into Python"

in_start = "Di"
in_end = "thon"
if my_new_text.startswith(in_start):
    print(f"Рядок починається з '{in_start}'")

if my_new_text.endswith(in_end):
    print(f"Рядок закінчується '{in_end}'")

if my_new_text[0].isupper():
    print("YES!")

print("YES".isupper())

if my_new_text[1].islower():
    print("nononon")

if in_start.istitle():
    print("Titled!")

my_text_for_me = my_text.upper()
print(my_text_for_me)
my_text_for_small = my_text_for_me.lower()
print(my_text_for_small)
my_text_capital = my_text_for_me.capitalize()
print(my_text_capital)
my_text_title = my_text_for_me.title()
print(my_text_title)
my_swap = my_text_title.swapcase()
print(my_swap)

my_totaly_new = "It is example for text find"

start = my_totaly_new.find("e")
print(start)
second_e = my_totaly_new.find("e", start + 1)
print(second_e)

my_replaced_text = my_totaly_new.replace("text", "cakes", 1)
print(my_replaced_text)

line = "    Привіт, світ!    "
clean_str = line.strip()
print(f"|{clean_str}|")
clean_rstr = line.rstrip()
print(f"|{clean_rstr}|")
clean_lstr = line.lstrip()
print(f"|{clean_lstr}|")

line_2 = "zzzz____ Good day all ____zzzzzzzzzzzz"
clean_line = line_2.strip("z").strip("_").strip()
print(f"|{clean_line}|")

# variable = input("help for user")

num_1 = "123"
i_num = int(num_1)
print(type(i_num), type(num_1))
pi = "3.1415"
f_num = float(pi)
print(type(f_num))

list_candidate = "12,3,4,5"
out_list = list_candidate.split(",")
print(out_list)
out_2 = list(list_candidate)
print(out_2)
any_line = "False"
print(bool(any_line))

name = "Василь"
age = 25
some_str_out = f"Привіт, {name}! Тобі {age} років."
print(some_str_out)


str1 = "find me"
if str1.find("deza") == -1:
    print("unexpected find!!")