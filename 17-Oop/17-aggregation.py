# Aggregation = Represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books] #list comprehension 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#Our Library and book can exist without each other, where the aggregation comes in Our
# library object will contain our book object
library = Library('Khulna Public Library')

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("The Hobbit", "J. R. R Tolkien")
book3 = Book("The Last Don", "Mario Puzo")
book4 = Book("The Colour of magic", "Terry Pratchett")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)    # {Note: Our library object just containing the books}
library.add_book(book4)

print(library.name)
# print(library.list_books())
for book in library.list_books():
    print(f"* {book}")