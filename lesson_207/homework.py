
from pathlib import Path


"""
### Робота з файлами та папками — завдання

1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here

#print(__file__, type(__file__))
my_file_path = Path(__file__)
#print(my_file_path, type(my_file_path))
homework_dir = my_file_path.parent
#print(homework_path)
#print(homework_path.is_dir())
open_file_path = homework_dir / "hello.txt"

my_str =    """
Hello, Python!
"""
try:
    with open(open_file_path, "w", encoding="utf8") as f:
        f.writelines(my_str)
except FileNotFoundError as e:
    pass ##

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
try:
    with open(open_file_path, "r", encoding="utf8") as f:
        text = f.readlines()
        print(text)
except FileNotFoundError as e:
    pass ##

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
my_str2 = """
Learning file operations.
"""
try:
    with open(open_file_path, "a", encoding="utf8") as f:
        f.writelines(my_str2)
except FileNotFoundError as e:
    pass
      
"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here

try:
    with open(open_file_path, "r", encoding="utf8") as f:
        text = f.readlines()
        for item in text:
            strt = item.strip("\n")
            if len(strt):
                  print(strt)
except FileNotFoundError as e:
    pass ##

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
try:
    with open(open_file_path, "r", encoding="utf8") as f:
        text = f.readlines()
        total_symbol_cnt = 0
        for item in text:
            strt = item.strip("\n")
            total_symbol_cnt += len(strt)
        print("кількість символів", total_symbol_cnt)
except FileNotFoundError as e:
    pass ##

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here

current_work_directory = Path.cwd()
print("Поточна робоча директорія:", current_work_directory)
new_directory = homework_dir / "data" 
new_directory.mkdir(parents=True, exist_ok=True)
notes_file_path = new_directory / "notes.txt"
my_note = """
My first note.
"""
try:
    with open(notes_file_path, "w", encoding="utf8") as f:
        f.writelines(my_note)
except FileNotFoundError as e:
    pass ##

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here

files = [d for d in new_directory.iterdir() if d.is_file()]
for i in files:
   print(i.name)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
try:
    with open(notes_file_path, "r", encoding="utf8") as f:
        text = f.readlines()
        copy_file_path = new_directory / "copy.txt"
        try:
            with open(copy_file_path, "w", encoding="utf8") as f:
                f.writelines(text)
        except FileNotFoundError as e:
            pass ##
except FileNotFoundError as e:
    pass ##

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
try:
    with open(homework_dir / "a.txt", "w", encoding="utf-8") as f1:
        f1.write("AAAAAAAAAAAAAAA.\n")
except FileNotFoundError as e:
    pass ##

try:
    with open(homework_dir / "b.txt", "w", encoding="utf-8") as f2:
        f2.write("BBBBBBBBBBBBBBBB.\n")
except FileNotFoundError as e:
    pass ##

try:
    with open(homework_dir / "a.txt", "r", encoding="utf-8") as f1, \
        open(homework_dir / "b.txt", "r", encoding="utf-8") as f2, \
        open(homework_dir / "ab.txt", "w", encoding="utf-8") as fout:
        fout.write(f1.read())
        fout.write(f2.read())
except FileNotFoundError as e:
    pass ##
"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
try:
    with open(notes_file_path, "r", encoding="utf8") as f:
        text = f.readlines()
        print("Знайдено") if "note" in text else print("Не знайдено")
except FileNotFoundError as e:
    pass ##