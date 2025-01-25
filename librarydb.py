import json
from bookdb import BookDataBase

class DataBase:

    def __init__(self):
        self.file = "data/librarydb.json"
        self.load_data()
        self.bookdb = BookDataBase()
        
    def load_data(self):
        """
        Attempts to load the data from the file. Creates a new file if not found.
        """
        try:
            with open(self.file, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            with open(self.file, "w") as f:
                json.dump(self.data, f)

    def save_data(self):
        """
        Saves the current data dictionary to the JSON file.
        """
        with open(self.file, "w") as f:
            json.dump(self.data, f)

    def add_user(self, name, email, password):
        """
        Adds a new user to the database with a name, email, and password.
        """
        if email in self.data:
            return False
        self.data[email] = {"Name" : name, "Email" : email, "Password" : password, "Books" : {}}
        self.save_data()
        return True
    
    def authenticate_user(self, email, password):
        """
        Validates if the email and password match any user in the database.
        """
        return email in self.data and self.data[email]["Password"] == password

    def borrow_book(self, email, title):
        """
        Borrowed book is added to the user.
        """
        if self.bookdb.borrow_book(title):
            if self.bookdb.book_details(title):
                _, author, _ = self.bookdb.book_details(title)
                self.data[email]["Books"][title] = {"Title": title, "Author": author}
                return True
        else:
            return False
        self.save_data()
    
    def return_book(self, email, title):
        """
        Return the borrowed book.
        """
        if title in self.data[email]["Books"]:
            self.bookdb.return_book(title)
            del self.data[email]["Books"][title]
        else:
            return False
        self.save_data()
        return True
        