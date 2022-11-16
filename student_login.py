# Import all the required modules
from tkinter import Tk, Label, Entry, Button, messagebox
import sqlite3 as sql
from new_student import new_student


# Create a function to create the login window
def student_login():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("Login")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a label for username
    username_label = Label(window, text="Username:")
    username_label.place(x=50, y=100)
    # Create an entry for username
    username_entry = Entry(window, width=20)
    username_entry.place(x=200, y=100)
    
    # Create a label for password
    password_label = Label(window, text="Password:")
    password_label.place(x=50, y=150)
    # Create an entry for password
    password_entry = Entry(window, width=20)
    password_entry.place(x=200, y=150)
    
    # Create a button for login
    login_btn = Button(window, text="Login", command=lambda: login(username_entry, password_entry))
    login_btn.place(x=200, y=200, width=200)
    
    # Create a button for new user
    new_user_btn = Button(window, text="New User", command=new_student)
    new_user_btn.place(x=200, y=250, width=200)
    
    # Run the login window
    window.mainloop()
    

# Create a function to login
def login(user, pswd):
    # Check if user and password are given
    if user and pswd:
        # Connect to the database
        db = sql.connect(database="student.db")
        # Create a cursor
        cur = db.cursor()
        
        # Select the username and password from the database
        cur.execute(f"SELECT * FROM Student WHERE registration='{user.get()}' AND password='{pswd.get()}'")
        # Fetch the data
        row = cur.fetchone()
        
        # Check if user is found
        if row:
            # Show a message
            messagebox.showinfo("Login", "Login Successful")
        else:
            # Show a success message
            messagebox.showerror("Login", "Login Failed")
    else:
        # Show an error message
        messagebox.showerror("Error", "Please enter username and password")
        
