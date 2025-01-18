# Magic methods = Dunder methods (double underscore) _init_, _str_ _eq
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.R. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book2)
print(book3)