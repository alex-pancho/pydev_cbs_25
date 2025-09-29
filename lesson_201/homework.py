"""
Завдання 0
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:

    def __init__(self, name, surname, age:int, gpa:int):
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa

    def gpa_change(self):
        self.gpa = int(input("Enter GPA: "))
        return self.gpa
    

student_1 = Student("Patric", "Matric", 23, 89)

print("\nЗавдання 0")

print(f"\nStudent name: {student_1.name} {student_1.surname}, GPA is: {student_1.gpa}")
print()
print(f"Student name: {student_1.name} {student_1.surname}, changed GPA is: {student_1.gpa_change()}")
print()



"""
Завдання 1
Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр. Створіть кілька різних книжок. Визначте для нього методи __repr__ та __str__.
"""

class Books:
    
    def __init__(self, author, book_title, genre, year_publ:int):
        self.author = author
        self.book_title = book_title
        self.genre = genre
        self.year_publ = year_publ

    def __str__(self):
        return f"Book: \nAuthor: '{self.author}', Book title: '{self.book_title}', Genre: '{self.genre}', Year of public: '{self.year_publ}'"
    
book1 = Books("Nikola", "Tesla", "Scienсe", 1200)
book2 = Books("Mikola", "Besla", "Huyaense", 14568)

print("\nЗавдання 1")
print(book1)
print()
print(book2)
print()


"""
Завдання 2
Створіть клас, який описує відгук до книги. Додайте до класу книги поле(атрибут) – список_відгуків. Зробіть так,
щоб при виведенні обєкту классу книги на екран за допомогою функції print (__str__) також виводилися відгуки до неї.
"""

class reviews(Books):

    def __init__(self, author, book_title, genre, year_publ:int, review):
        super().__init__(author, book_title, genre, year_publ)   
        self.review = review

    def __str__(self):
        books_with_rev = super().__str__()
        return f"{books_with_rev}, Review: {self.review}"
    
book1 = reviews("Nikola", "Tesla", "Scienсe", 1200, "Good book")
book2 = reviews("Mikola", "Besla", "Huyaense", 14568, "Bad book")

print("\nЗавдання 2")
print(book1)
print()
print(book2)
print()