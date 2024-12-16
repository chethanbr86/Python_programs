#Aggregation: Library can exist without a book but a book can exist without a library, both are independant classes ("has-a" relationship)
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f'{book.title} by {book.author}' for book in self.books]
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Public Library")
book1 = Book("Python Programming", "John Doe")
book2 = Book("Java Programming", "Jane Doe")
book3 = Book("C Programming", "John Malkovich")

# library.books = [book1, book2, book3]

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book in library.list_books():
    print(book)
