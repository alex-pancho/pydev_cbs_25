"""
Завдання 0
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.

Завдання 1
Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та
жанр. Створіть кілька різних книжок. Визначте для нього методи __repr__ та __str__.

Завдання 2
Створіть клас, який описує відгук до книги. Додайте до класу книги поле(атрибут) – список_відгуків. Зробіть так,
щоб при виведенні обєкту классу книги на екран за допомогою функції print (__str__) також виводилися відгуки до неї.
"""
# Вирішив переробити 0 завдання, щоб попрактикувати
class Student():
    def __init__(self):
        self.name = "Іван"
        self.age = 23
        self.grade = 6
    def changegrade(self, newgrade):
        self.grade = newgrade

study = Student()
study.changegrade(newgrade=10)
print(study.name, study.age, study.grade)

class Book():
    def __init__(self, year, author, genre, book):
        self.author = author
        self.year = year
        self.genre = genre
        self.book = book
    def __str__(self):
        return f'Назва книги: {self.book} Автор: {self.author} Рік видання: {self.year} Жанр: {self.year}'
infobook = Book("Гамлет", "Вільям Шекспір", 1623, "Трагедія")
print(infobook)

class Review():
    def __init__(self):
        self.user = input("Напишіть ваше ім'я: ")
        self.rating = int(input("Напишіть оцінку до книги: "))
        self.comment = input("Напишіть коментар до книги: ")
    def __str__(self):
        return f'Користувач: {self.user} Оцінка до книги: {self.rating} Коментар: {self.comment}'
review1 = Review()
print(review1)
# Вирішив попрактикувати з input, для того щоб зробити функціонал для відгуків.
    
        
