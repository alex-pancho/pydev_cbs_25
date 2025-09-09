adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

my_adwentures_of_tom_sawer_1 = adwentures_of_tom_sawer.replace("\n", " ")
print(my_adwentures_of_tom_sawer_1)
print()

# task 02 ==
""" Замініть .... на пробіл
"""
my_adwentures_of_tom_sawer_2 = my_adwentures_of_tom_sawer_1.replace("....", " ")
print(my_adwentures_of_tom_sawer_2)
print()

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
import re

my_adwentures_of_tom_sawer_3 = re.sub(r'\s+', ' ', my_adwentures_of_tom_sawer_2)
print(my_adwentures_of_tom_sawer_3)
print()



# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

num_h = adwentures_of_tom_sawer.find("h")
all_num_h = adwentures_of_tom_sawer.find("h", num_h + 1)
print(f"Літера 'h' зустрічається у тексті {all_num_h} разів")
print()

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""


all_cap_let = "QWERTYUIOPASDFGHJKLZXCVBNM"
count_cap_let = 0

for all_cap in all_cap_let:
    count_cap_let += adwentures_of_tom_sawer.count(all_cap)  

print(f"{count_cap_let} слів у тексті починається з Великої літери")
print()

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index_tom_1 = adwentures_of_tom_sawer.find('Tom')
index_tom_2 = adwentures_of_tom_sawer.find('Tom', index_tom_1 + 1)

print(f"{index_tom_2} позиція, на якій слово Tom зустрічається вдруге")
print()


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = my_adwentures_of_tom_sawer_3.split(".")
print(adwentures_of_tom_sawer_sentences)
print()

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

adwentures_of_tom_sawer_sentences_4 = adwentures_of_tom_sawer_sentences[3].lower()
print(adwentures_of_tom_sawer_sentences_4)
print()

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

element_to_find = "By the time"

for element in adwentures_of_tom_sawer_sentences:

    if element_to_find in element:
        index_sentence = adwentures_of_tom_sawer_sentences.index(element)
        print(f"{index_sentence} речення починається з {element_to_find}")
    elif element_to_find not in element:
        continue
    else:   
        print(f"Нема речення що починається з {element_to_find}")
        
print()

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-2]
last_sentence_split = last_sentence.split()
len_last_sent = len(last_sentence_split)

print(last_sentence)
print(f"\n{len_last_sent} слів в останньом реченнi")
print()