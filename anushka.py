# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


# Patron Class
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)


# Library Class
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrow_book(book)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid Patron ID or Book ID.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book in patron.borrowed_books:
            book.is_borrowed = False
            patron.return_book(book)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the patron.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)


# Main Program
library = Library()

# Adding Books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Machine Learning", "David Lee"))

# Registering Patrons
library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Priya"))

# Display Books
library.display_books()

# Borrow a Book
library.borrow_book(1, 101)

# Display Books
library.display_books()

# Return the Book
library.return_book(1, 101)

# Display Books Again
library.display_books()