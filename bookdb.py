import json

class BookDataBase:

    def __init__(self):
        self.file = "data/bookdb.json"
        self.load_data()

    def load_data(self):
        """
        Attempts to load the data from the file. Creates a new file if not found.
        """
        try:
            with open(self.file, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = {}
            with open(self.file, "w") as f:
                json.dump(self.books, f)

    def save_data(self):
        """
        Saves the current data dictionary to the JSON file.
        """
        with open(self.file, "w") as f:
            json.dump(self.books, f)

    def add_book(self, title, author, copies):
        """
        Adds a new book to the database with a title, author and copies.
        """
        if title in self.books:
            self.books[title]["Copies"] += copies
        else:
            self.books[title] = {"Title": title, "Author": author, "Copies": copies}
        self.save_data()
        return True
    

    def borrow_book(self, title):
        """"
        Borrow a book from the library.
        Args:
            title (str): The title of the book to borrow.
        """
        if title in self.books:
            if self.books[title]["Copies"] > 0:
                self.books[title]["Copies"] -= 1
                return True
        else:
            return False
        self.save_data()
    
    def return_book(self, title):
        """
        Return a book to the library.
        Args:
            title (str): The title of the book to return.
        """
        self.books[title]["Copies"] += 1
        self.save_data()

    def list_books(self):
        """
        List all available books in the library.
        """
        book = []
        if self.books:
            for b in list(self.books.keys()):
                book.append(b)
            return book
        else:
            return False

    def book_details(self, title):
        if title in self.books:
            return list(self.books[title].values())[0], list(self.books[title].values())[1], list(self.books[title].values())[2]
        else:
            return False
        
    