import json

from Notebooks.book import Book

class Library:
    def __init__(self, name):
        """
        Initializes the library with its name and an empty collection of books.
        Args:
            name(str): The name of the library.
        """
        self.name = name 
        self.books = {}
        self.file = "librarydb.json"

    # def __str__(self):
    #     """
    #     Return the library name. 
    #     """
    #     return f"Welcome to {self.name} Library"
    
    def add_book(self, title, author, copies):
        """
        Add a new book or update copies if the book already exists.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            copies (int): The number of copies to add.
        """
        if title in self.books:
            self.books[title].copies += copies
            print(f"Added {copies} more copies of '{title}.'")
        else:
            self.books[title] = self.book(title, author, copies)
            print(f"Book '{title}' by {author} added to the library.")

        with open(self.file, "w") as f:
            json.dump(self.books, f)

    def borrow_book(self, title):
        """"
        Borrow a book from the library.
        Args:
            title (str): The title of the book to borrow.
        """
        
        if title in self.books:
            print(self.books[title].borrow_book())
        else:
            print(f"'{title}' is not available in the library.")

    def return_book(self, title):
        """
        Return a book to the library.
        Args:
            title (str): The title of the book to return.
        """
        if title in self.books:
            print(self.books[title].return_book())
        else:
            print(f"'{title}' is not part of this library.")

    def list_books(self):
        """
        List all available books in the library.
        """
        if self.books:
            print("Books available in the library:")
            for book in self.books.values():
                print(book)
        else:
            print("The library has no books at the moment.")

    def book_details(self, title):
        """"
        View details of a specific book.
        Args:
            title (str): The title of the book.
        """
        if title in self.books:
            print(self.books[title])
        else:
            print(f"'{title}' is not available in the library.")