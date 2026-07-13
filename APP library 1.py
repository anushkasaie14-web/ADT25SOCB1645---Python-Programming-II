# Simple Library Management System using OOP

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry! '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print("Book not found in borrowed list.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered successfully.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()


# Main Program
library = Library()

# Add Books
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Data Structures", "Mark Allen Weiss")

library.add_book(book1)
library.add_book(book2)

# Register Patron
patron1 = Patron("Anushka")
library.register_patron(patron1)

# Display Books
library.display_books()

# Borrow Book
patron1.borrow_book(book1)

# Display Books
library.display_books()

# Return Book
patron1.return_book(book1)

# Display Books
library.display_books()