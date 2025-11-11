import xml.etree.ElementTree as ET
from pathlib import Path


curr_dir = Path(__file__).parent
# ================== БАЗОВІ ПОНЯТТЯ ==================
"""
XML ДЕРЕВО - це ієрархічна структура даних:
- Кореневий елемент (root) - один головний елемент
- Вузли (nodes) - елементи XML
- Дочірні елементи (children) - вкладені елементи
- Атрибути (attributes) - властивості елементів
- Текст (text) - вміст між тегами
"""
def get_xml_string():
    """Повертає базову структуру XML дерева"""
    return  """<?xml version="1.0" encoding="UTF-8"?>
    <library name="Central Library" established="1990">
        <book id="1" genre="fiction">
            <title>Тіні забутих предків</title>
            <author nationality="Ukrainian">
                <name>Михайло Коцюбинський</name>
                <birth_year>1864</birth_year>
            </author>
            <price currency="UAH">250</price>
            <available>true</available>
        </book>
        <book id="2" genre="drama">
            <title>Лісова пісня</title>
            <author nationality="Ukrainian">
                <name>Леся Українка</name>
                <birth_year>1871</birth_year>
            </author>
            <price currency="UAH">180</price>
            <available>false</available>
        </book>
        <magazine id="101">
            <title>Наука і техніка</title>
            <issue>№3</issue>
            <year>2024</year>
        </magazine>
    </library>"""

def filewrite(content:str, filename: str = "library.xml"):
    """Записує XML вміст у файл"""
    filepath = curr_dir / filename
    # Збережемо у файл для демонстрації
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# ================== ПАРСИНГ XML ==================
def parse_xml_file(filename: str = "library.xml"):
    """Парсить XML з файлу і повертає кореневий елемент"""
    filepath = curr_dir / filename
    tree = ET.parse(filepath)
    return tree.getroot(), tree 

def parse_xml_string(xml_content: str):
    """Парсить XML з рядка і повертає кореневий елемент"""
    return ET.fromstring(xml_content)

print("=" * 50)
print("ОСНОВНІ ВЛАСТИВОСТІ ЕЛЕМЕНТІВ")
print("=" * 50)
filewrite(get_xml_string())  # Записуємо XML у файл для демонстрації
root, tree = parse_xml_file()  # Парсимо XML з файлу

# ================== ОСНОВНІ ВЛАСТИВОСТІ ==================

# tag - назва тега
print(f"Кореневий тег: {root.tag}")

# attrib - словник всіх атрибутів
print(f"Атрибути кореня: {root.attrib}")

# text - текстовий вміст (між відкриваючим і закриваючим тегами)
print(f"Текст кореня: {repr(root.text)}")  # None, бо немає прямого тексту

# ================== НАВІГАЦІЯ ПО ДЕРЕВУ ==================

print("\n" + "=" * 50)
print("НАВІГАЦІЯ ПО ДЕРЕВУ")
print("=" * 50)

# Отримання всіх дочірніх елементів
print("Дочірні елементи кореня:")
for child in root:
    print(f"  - {child.tag} (атрибути: {child.attrib})")

# Доступ до конкретного дочірнього елемента за індексом
first_book = root[0]  # Перша книга
print(f"\nПерша книга: {first_book.tag}, id={first_book.get('id')}")

# ================== МЕТОДИ ПОШУКУ ==================

print("\n" + "=" * 50)
print("МЕТОДИ ПОШУКУ")
print("=" * 50)

# find() - знаходить ПЕРШИЙ елемент
first_book = root.find("book")
print(f"Перша знайдена книга: {first_book.find('title').text}")

# findall() - знаходить ВСІ елементи
all_books = root.findall("book")
print(f"Кількість книг: {len(all_books)}")

# findtext() - знаходить текст першого елемента
first_title = root.findtext("book/title")
print(f"Назва першої книги: {first_title}")

# ================== РОБОТА З АТРИБУТАМИ ==================

print("\n" + "=" * 50)
print("РОБОТА З АТРИБУТАМИ")
print("=" * 50)

for book in root.findall("book"):
    book_id = book.get("id")          # get() - безпечний спосіб
    genre = book.attrib.get("genre")   # через attrib словник
    
    print(f"Книга ID: {book_id}, Жанр: {genre}")
    
    # Додавання/зміна атрибутів
    book.set("processed", "true")
    
    # Видалення атрибутів
    # del book.attrib["genre"]  # Розкоментуйте для видалення

# ================== ГЛИБОКИЙ ПОШУК ==================

print("\n" + "=" * 50)
print("ГЛИБОКИЙ ПОШУК")
print("=" * 50)

# Пошук на будь-якому рівні вкладеності
all_names = root.findall(".//name")  # .// означає "будь-де в дереві"
print("Імена авторів:")
for name in all_names:
    print(f"  - {name.text}")

# Пошук з умовами (XPath)
fiction_books = root.findall(".//book[@genre='fiction']")
print(f"\nКількість художніх книг: {len(fiction_books)}")

# Пошук за текстом
expensive_books = root.findall(".//book[price>200]")
print(f"Книги дорожче 200 грн: {len(expensive_books)}")

# ================== СТВОРЕННЯ НОВИХ ЕЛЕМЕНТІВ ==================

print("\n" + "=" * 50)
print("СТВОРЕННЯ НОВИХ ЕЛЕМЕНТІВ")
print("=" * 50)

# Створення нового елемента
new_book = ET.Element("book")
new_book.set("id", "3")
new_book.set("genre", "poetry")

# Створення дочірніх елементів
title_elem = ET.SubElement(new_book, "title")
title_elem.text = "Кобзар"

author_elem = ET.SubElement(new_book, "author")
author_elem.set("nationality", "Ukrainian")

name_elem = ET.SubElement(author_elem, "name")
name_elem.text = "Тарас Шевченко"

price_elem = ET.SubElement(new_book, "price")
price_elem.set("currency", "UAH")
price_elem.text = "300"

# Додавання до кореня
root.append(new_book)

# ================== МОДИФІКАЦІЯ ІСНУЮЧИХ ЕЛЕМЕНТІВ ==================

print("\n" + "=" * 50)
print("МОДИФІКАЦІЯ ЕЛЕМЕНТІВ")
print("=" * 50)

# Зміна тексту
for book in root.findall("book"):
    available = book.find("available")
    if available is not None:
        if available.text == "true":
            available.text = "у наявності"
        else:
            available.text = "немає в наявності"

# Зміна атрибутів
library_name = root.get("name")
root.set("name", f"{library_name} (Оновлено)")

# ================== ВИДАЛЕННЯ ЕЛЕМЕНТІВ ==================

print("\n" + "=" * 50)
print("ВИДАЛЕННЯ ЕЛЕМЕНТІВ")
print("=" * 50)

# Видалення дочірнього елемента
magazines = root.findall("magazine")
for magazine in magazines:
    root.remove(magazine)
    print(f"Видалено журнал: {magazine.find('title').text}")

# ================== ЗБЕРЕЖЕННЯ XML ==================

print("\n" + "=" * 50)
print("ЗБЕРЕЖЕННЯ XML")
print("=" * 50)

# Збереження у файл

#tree.write(filepath, encoding="utf-8", xml_declaration=True, method="html")

# Отримання XML як рядок
xml_string = ET.tostring(root, encoding="unicode")
print("XML як рядок (перші 200 символів):")
print(xml_string[:200] + "...")

filewrite(xml_string, filename="library_updated.xml")
# ================== ПРАКТИЧНИЙ ПРИКЛАД ==================

print("\n" + "=" * 50)
print("ПРАКТИЧНИЙ ПРИКЛАД: АНАЛІЗ БІБЛІОТЕКИ")
print("=" * 50)

def analyze_library(root):
    """Аналізує XML бібліотеки і виводить статистику"""
    
    # Загальна інформація
    library_name = root.get("name")
    established = root.get("established")
    
    print(f"Бібліотека: {library_name}")
    print(f"Заснована: {established}")
    
    # Підрахунок книг
    books = root.findall("book")
    print(f"Загальна кількість книг: {len(books)}")
    
    # Статистика по жанрах
    genres = {}
    for book in books:
        genre = book.get("genre", "невідомий")
        genres[genre] = genres.get(genre, 0) + 1
    
    print("\nСтатистика по жанрах:")
    for genre, count in genres.items():
        print(f"  {genre}: {count}")
    
    # Середня ціна
    prices = []
    for book in books:
        price_elem = book.find("price")
        if price_elem is not None:
            try:
                price = float(price_elem.text)
                prices.append(price)
            except ValueError:
                continue
    
    if prices:
        avg_price = sum(prices) / len(prices)
        print(f"\nСередня ціна: {avg_price:.2f} грн")
    
    # Доступність
    available_count = 0
    for book in books:
        available = book.find("available")
        if available is not None and available.text in ["true", "у наявності"]:
            available_count += 1
    
    print(f"Доступно зараз: {available_count} з {len(books)} книг")

# Запуск аналізу
analyze_library(root)

# ================== ОБРОБКА ПОМИЛОК ==================

print("\n" + "=" * 50)
print("ОБРОБКА ПОМИЛОК")
print("=" * 50)

def safe_xml_processing(filename):
    """Безпечна обробка XML з перевіркою помилок"""
    filepath = curr_dir / filename
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Перевірка структури
        if root.tag != "library":
            print("Увага: Очікувався кореневий елемент 'library'")
        
        # Безпечне отримання значень
        for book in root.findall("book"):
            title_elem = book.find("title")
            title = title_elem.text if title_elem is not None else "Без назви"
            
            book_id = book.get("id", "невідомий")
            
            print(f"Книга: {title} (ID: {book_id})")
            
    except ET.ParseError as e:
        print(f"Помилка парсингу XML: {e}")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
    except Exception as e:
        print(f"Несподівана помилка: {e}")

# Тестування
safe_xml_processing("library.xml")

print("\n" + "=" * 50)
print("ПІДСУМОК")
print("=" * 50)

print("""
ОСНОВНІ ПОНЯТТЯ:
- tag: назва XML тега
- attrib: словник атрибутів елемента
- text: текстовий вміст між тегами
- tail: текст після закриваючого тега (рідко використовується)

МЕТОДИ ПОШУКУ:
- find(): знаходить перший елемент
- findall(): знаходить всі елементи
- findtext(): знаходить текст першого елемента
- get(): безпечно отримує атрибут

НАВІГАЦІЯ:
- root[0]: доступ за індексом
- for child in element: перебір дочірніх елементів
- element.getchildren(): отримання списку дочірніх (застарілий метод)

МОДИФІКАЦІЯ:
- set(): встановлення атрибуту
- append(): додавання дочірнього елемента
- remove(): видалення дочірнього елемента
- clear(): очищення елемента

XPATH вирази:
- ".//tag": пошук на будь-якому рівні
- "tag[@attr='value']": пошук з умовою по атрибуту
- "tag[position]": пошук по позиції
""")