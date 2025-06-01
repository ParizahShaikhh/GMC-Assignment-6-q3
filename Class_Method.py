# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self):
        # Constructor to initialize a new book instance
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        # Increment the total book count

    @classmethod
    def get_total_books(cls):
        return f"Total books: {cls.total_books}"
        # Return the total number of books using cls.total_books


# Example Usage
book1 = Book()
book2 = Book()
print(Book.get_total_books())  # Output: 2
