class Book:

    def __init__(self, title, author, copies):
        """"
        Initializes the book details.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            copies (int): The number of copies available in the library.
        """
        self.title = title
        self.author = author
        self.copies = copies
        self.book = {"Title" : self.title, "Author" : self.author, "Copies" : self.copies}

    def __str__(self):
        """
        Returns a readable representation of the book details.
        """
        return f"'{self.title}' by {self.author} (Available Copies): {self.copies}"
    
    def borrow_book(self):
        """
        Borrow a copy of the book if available.
        Returns:
            str: Success or failure message.
        """
        if self.copies > 0:
            self.copies -= 1
            return f"You have successfully borrowed '{self.title}'."
        return f"'{self.title}' is currently unavailable."
    
    def return_book(self):
        """
        Returns a borrowed copy of the book.
        Returns:
            str: Success message.
        """
        self.copies += 1
        return f"You have successfully returned '{self.title}.'"
