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
with open("hello.txt", "w", encoding="utf8") as f:
    f.write("```\n")
    f.write("Hello, Python!\n")
    f.write("```\n")
    print(f)

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
with open("hello.txt", "r", encoding="utf8") as f:
    content = f.read()
    print(content)

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with open("hello.txt", "a", encoding="utf8") as f:
    f.write("```\n")
    f.write("Learning file operations.\n")
    f.write("```\n")


"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with open("hello.txt", "r", encoding="utf8") as f:
    for line in f:
        print(line.strip("\n"))
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
with open("hello.txt", "r", encoding="utf8") as f:
    content = f.read()
    print(len(content))

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
Path("data").mkdir(parents=True, exist_ok=True)

with open("data/notes.txt", "w") as file:
    file.write("```\n")
    file.write("My first note.\n")
    file.write("```\n")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here

folder = Path("data")

files = [f.name for f in folder.iterdir() if f.is_file()]
for file in files:
    print(file)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here

folder = Path("data")

source_file = folder / "notes.txt"
destination_file = folder / "copy.txt"

content = source_file.read_text()

destination_file.write_text(content)

print(f"вміст файлу '{source_file}' був успішно скопійований до '{destination_file}'.")
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here

folder = Path("data")

file_a = folder / "a.txt"
file_b = folder / "b.txt"
file_ab = folder / "ab.txt"

file_a.write_text("Це вміст файлу a.txt.\n")
file_b.write_text("Це вміст файлу b.txt.\n")

content_a = file_a.read_text()
content_b = file_b.read_text()

file_ab.write_text(content_a + content_b)

print(f"Вміст файлів '{file_a}' і '{file_b}' успішно об'єднано у файл '{file_ab}'.")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here

folder_path = Path('data')
file_path = folder_path / 'notes.txt'

try:
    content = file_path.read_text()
    if 'note' in content:
        print("Знайдено")
    else:
        print("Не знайдено")
except FileNotFoundError:
    print(f"Файл {file_path} не знайдено.")