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

class Student():
    average_mark = 0
    def __init__(self, name, second_name, age):
        self.name = name
        self.second_name = second_name
        self.age = age
        
    def set_average_mark(self, average_mark):
        self.average_mark = average_mark
    


student = Student("Serhii", "Haliuk", 51)
student.set_average_mark(100)
print(f"Student: {student.name} {student.second_name}, age {student.age}. Average mark: {student.average_mark}")


class Book():
    review_list = []
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        
    def __repr__(self):
        return f"Its class Book for book {self.name}"    
    def __str__(self):
        if len(self.review_list):
            self.revievs_str = "Revievs:\n"
            self.revievs_str += '\n'.join(self.review_list)
            return self.revievs_str
        else:
            return f"Book {self.name} has no revievs"
          
    def add_review(self, review):
        self.review_list.append(review)
        
class Review:
    def __init__(self, reviewer, text):
        self.reviewer = reviewer
        self.text = text

    def __str__(self):
        return f"{self.reviewer}: {self.text}"
        
      
book1 = Book("Shogun", "James Clavel", 1975)
print(f"Book: {book1.name} {book1.author}, {book1.year}.")
print(book1.__repr__())
print(book1)
print (book1.__str__())

book1.add_review(str(Review("Serhii", "Good book!")))
book1.add_review(str(Review("Serhii", "Good book!")))
book1.add_review(str(Review("Serhii", "Good book!")))

print(book1)
print (book1.__str__())