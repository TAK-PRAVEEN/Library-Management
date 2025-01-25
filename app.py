from tkinter import *
from tkinter import messagebox

from librarydb import DataBase
from bookdb import BookDataBase

class LibraryManagement:

    def __init__(self):
        self.dbo = DataBase()
        self.bdb = BookDataBase()


        self.root = Tk()
        self.root.title("Wise Online Library")
        self.root.geometry("1200x600")
        self.root.configure(bg = "#ff9978")
        
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        """
        Displays the login form in the GUI.
        """
        self.clear()

        Label(self.root, text = "Welcome to the Wise Online Library Login Page", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 24, "bold")).pack(pady = (32, 32))

        # email input
        Label(self.root, text = "Enter email:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))
        self.email_input_login = Entry(self.root, width = 30)
        self.email_input_login.pack(ipady = 5, pady = (0, 10))

        # password input
        Label(self.root, text = "Enter password:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))
        self.password_input = Entry(self.root, width = 30, show = "•")
        self.password_input.pack(ipady = 5, pady = (0, 10))

        # login submit button
        Button(self.root, text = "Login", width = 20, command = self.perform_login).pack(pady = (20, 10))
        
        # register page button
        Label(self.root, text = "Not a member!", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        Button(self.root, text =  "Register Now!", command = self.register_gui).pack(pady = (5, 10))

    def register_gui(self):
        """
        Displays the registration form in the GUI.
        """
        self.clear()

        Label(self.root, text = "Welcome to the Wise Online Library Registration Page", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 24, "bold")).pack(pady = (32, 32))

        # name input
        Label(self.root, text = "Enter name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))
        self.name_input = Entry(self.root, width = 30)
        self.name_input.pack(ipady = 5, pady = (0, 10))

        # email input
        Label(self.root, text = "Enter email:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))
        self.email_input = Entry(self.root, width = 30)
        self.email_input.pack(ipady = 5, pady = (0, 10))

        # password input
        Label(self.root, text = "Enter password:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))
        self.password_input = Entry(self.root, width = 30, show = "•")
        self.password_input.pack(ipady = 5, pady = (0, 10))

        # login submit button
        Button(self.root, text = "Register", width = 20, command = self.perfrom_registration).pack(pady = (20, 10))

        # login page button
        Label(self.root, text = "Already a member!", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        Button(self.root, text =  "Login Now!", command = self.login_gui).pack(pady = (5, 10))
    
    def clear(self):
        """
        Clears all widgets from the current GUI.
        """
        for widget in self.root.pack_slaves():
            widget.destroy()

    def perfrom_registration(self):
        """
        Handles the logic of registration.
        """

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if self.dbo.add_user(name, email, password):
            messagebox.showinfo("Success", "Registration Successfully!")
            self.login_gui()
        else:
            messagebox.showerror("Error", "Email already exists!")

        print(name, email, password)

    def perform_login(self):
        """
        Handles the user login logic.
        """
        email = self.email_input_login.get()
        password = self.password_input.get()

        if self.dbo.authenticate_user(email, password):
            messagebox.showinfo("Success", "Login Successfully," "Welcome to the library.")
            self.current_user_email = email
            self.dashboard_gui()
        else:
            messagebox.showerror("Error", "Invalid Email/Password, Please try again.")

    def dashboard_gui(self):
        """
        Displays the user's dashboard with options.
        """
        self.clear()

        Label(self.root, text = "Dashboard", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "bold")).pack(pady = (12, 5))

        Button(self.root, text = "Add Book", width = 20, command = self.add_book).pack(pady = (5, 10))
        Button(self.root, text = "Borrow Book", width = 20, command = self.borrow_book).pack(pady = (5, 10))
        Button(self.root, text = "Return Book", width = 20, command = self.return_book).pack(pady = (5, 10))
        Button(self.root, text = "List of Books", width = 20, command = self.list_books).pack(pady = (5, 10))
        Button(self.root, text = "Deatils of Book", width = 20, command = self.book_details).pack(pady = (5, 10))

        Button(self.root, text = "Log Out!", width = 20, command = self.login_gui).pack(pady = (5, 10))

    def add_book(self):
        """
        GUI for adding book to database.
        """
        self.clear()

        Label(self.root, text = "Add Book", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 20, "bold")).pack(pady = (12, 5))

        Label(self.root, text = "Enter Book Name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.book_title_input = Entry(self.root, width = 50)
        self.book_title_input.pack(ipady = 5, pady = (0, 10))

        Label(self.root, text = "Enter Author Name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.author_name_input = Entry(self.root, width = 50)
        self.author_name_input.pack(ipady = 5, pady = (0, 10))

        Label(self.root, text = "Enter Number of Copies:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.copies_input = Entry(self.root, width = 50)
        self.copies_input.pack(ipady = 5, pady = (0, 10))

        Button(self.root, text = "Add", width = 20, command = self.adding_book).pack(pady = (5, 10))

        Button(self.root, text = "Back to Dashboard", width = 20, command = self.dashboard_gui).pack(pady = (5, 10))

    def adding_book(self):
        """
        Handles the logic to add the book to database.
        """
        title = self.book_title_input.get()
        author = self.author_name_input.get()
        copies = int(self.copies_input.get())

        if self.bdb.add_book(title, author, copies):
            messagebox.showinfo("Success", f"Book titled '{title}' added successfully!")
        else:
            messagebox.showerror("Error", "Not added!")

        print(f"{title} - {author} - {copies}")

    def borrow_book(self):
        """
        GUI for borrowing book to database.
        """
        self.clear()

        Label(self.root, text = "Borrow Book", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 20, "bold")).pack(pady = (12, 5))

        Label(self.root, text = "Enter Book Name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.title_input = Entry(self.root, width = 50)
        self.title_input.pack(ipady = 5, pady = (0, 10))

        Button(self.root, text = "Borrow", width = 20, command = self.borrowing_book).pack(pady = (5, 10))

        Button(self.root, text = "Back to Dashboard", width = 20, command = self.dashboard_gui).pack(pady = (5, 10))

    def borrowing_book(self):
        """
        Handles the logic to borrow the book from database.
        """
        title = self.title_input.get()

        if self.dbo.borrow_book(self.current_user_email, title):
            messagebox.showinfo("Success", f"Book titled '{title}' borrowed successfully!")
        else:
            messagebox.showerror("Error", f"'{title}' is not available in the library.")

        print(f"{title}")

    def return_book(self):
        """
        GUI for returning book to database.
        """
        self.clear()

        Label(self.root, text = "Return Book", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 20, "bold")).pack(pady = (12, 5))

        Label(self.root, text = "Enter Book Name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.title_input = Entry(self.root, width = 50)
        self.title_input.pack(ipady = 5, pady = (0, 10))

        Button(self.root, text = "Return", width = 20, command = self.returning_book).pack(pady = (5, 10))

        Button(self.root, text = "Back to Dashboard", width = 20, command = self.dashboard_gui).pack(pady = (5, 10))

    def returning_book(self):
        """
        Handles the logic to return the book from database.
        """
        title = self.title_input.get()

        if self.dbo.return_book(self.current_user_email, title):
            messagebox.showinfo("Success", f"Book titled '{title}' returned successfully!")
        else:
            messagebox.showerror("Error", f"'{title}' is not part of this library.")

        print(f"{title}")

    def list_books(self):
        """
        Handles the logic to return the list of books from database.
        """
        book = self.bdb.list_books()
        self.clear()

        Label(self.root, text = "List of Books", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 20, "normal")).pack(pady = (12, 5))

        listbox = Listbox(self.root, height = 10, 
                  width = 15, 
                  bg = "#461200",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "#fed9cd")  
        index = 1
        if self.bdb.list_books():
            for i in book:
                # Label(self.root, text = i, bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (12, 5))
                listbox.insert(index, i)
                print(index, i)
                index += 1
        else:
            messagebox.showerror("Error", "The library has no books at the moment.")
        listbox.pack()
        
        Button(self.root, text = "Back to Dashboard", width = 20, command = self.dashboard_gui).pack(pady = (5, 10))

    def book_details(self):
        """
        GUI for retrieving book deatils from database.
        """
        self.clear()

        Label(self.root, text = "Book Details", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 20, "bold")).pack(pady = (12, 5))

        Label(self.root, text = "Enter Book Name:", bg = "#ff9978", fg = "#681b00", font = ("Times New Roman", 12, "normal")).pack(pady = (20, 5))
        self.title_input = Entry(self.root, width = 50)
        self.title_input.pack(ipady = 5, pady = (0, 10))

        Button(self.root, text = "Get Details", width = 20, command = self.accessing_book).pack(pady = (5, 10))

        Button(self.root, text = "Back to Dashboard", width = 20, command = self.dashboard_gui).pack(pady = (5, 10))

    def accessing_book(self):
        """
        Handles the logic to return the details of book from database.
        """
        title = self.title_input.get()

        if self.bdb.book_details(title):
            _, author, copies = self.bdb.book_details(title)
            messagebox.showinfo("Book details", f"The book '{title}' by {author} is available in the library with {copies} copies.")
        else:
            messagebox.showerror("Error", f"'{title}' is not available in the library.")

            

        







LibraryManagement()