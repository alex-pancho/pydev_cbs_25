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
print ("task 01==")
print ()
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
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
rolling in wealth.""".replace ("\n", " ")
print (adwentures_of_tom_sawer)
print ()


# task 02 ==
print ("task 02 ==")
print ()
""" Замініть .... на пробіл
"""
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
rolling in wealth.""".replace ("....", " ")
print (adwentures_of_tom_sawer)
print ()


# task 03 ==
print ("task 03 ==")
print ()
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
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
rolling in wealth.""".replace (" .... ", " ").replace (" ....\n", " \n")
print (adwentures_of_tom_sawer)
print ()


# task 04
print ("task 04 ==")
print ()
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count ("h")
print (count_h)
print ()


# task 05
print ("task 05 ==")
print ()
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
count = sum (1 for letter in adwentures_of_tom_sawer if letter.isupper ())
print (count)
print ()


# task 06
print ("task 06 ==")
print ()
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = adwentures_of_tom_sawer.find ("Tom")
second_position = adwentures_of_tom_sawer.find ("Tom", first_position + 1)
print (second_position)
print ()


# task 07
print ("task 07 ==")
print ()
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = [s.strip () + "." for s in adwentures_of_tom_sawer.split (".") if s.strip ()]
print (adwentures_of_tom_sawer_sentences)
print ()


# task 08
print ("task 08 ==")
print ()
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print (adwentures_of_tom_sawer_sentences [3].lower ())
print ()


# task 09
print ("task 09 ==")
print ()
""" Перевірте чи починається якесь речення з "By the time".
"""
for s in adwentures_of_tom_sawer_sentences:
    if s.startswith ("By the time"):
        print ("Знайдено речення:", s)
print ()


# task 10
print ("task 10 ==")
print ()
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentense = adwentures_of_tom_sawer_sentences [-1]
word_count = len (last_sentense.split())
print ("Кількість слів в останньому реченні:", word_count)
