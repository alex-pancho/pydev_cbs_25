# Цикл while
# x = 0
# while x <= 0:
#     x = int(input("Введіть додатнє число: "))

# # n = 1 
# # while True:  
# #     print(n) 
# #     n += 1 

# n = 1 
# while True:
#     n += 1
#     if not n % 3:
#         print(n)
#     else:
#         continue
#     if n >= 10:
#         break

x = 0
while x < 10:
    x += 1
    if x == 5 or x == 6 or x== 9 or x == 7:
        continue
    print('Поточне число дорівнює', x)

# while True:
#     num = input("Введіть додатнє число: ")
#     if num.isdecimal():
#         x = int(num)
#         break

for i in range(5):
    print(i)
print("**")
for i in range(1, 6):
    print(i)

print("**")
for i in range(3, 32, 3):
    print(i)

verse = """
Садок вишневий коло хати,
Хрущі над вишнями гудуть,
Плугатарі з плугами йдуть,
Співають ідучи дівчата,
А матері вечерять ждуть.
"""
# len_verse = len(verse)
# for i in range(len_verse):
#     print(verse[i])

for i in verse:
    print(i, end="")


for i in range(10):
    for ii in range(10):
        print("*", end="")
    print("=")
