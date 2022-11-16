# Import all the required modules
from tkinter import Tk, Label, Entry, Button, messagebox
import sqlite3 as sql

# Create a function to create the new user window
def new_student():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("New Student")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a list to store the data
    data = []
    
    # Create a label for name
    name_label = Label(window, text="Name:")
    name_label.place(x=50, y=50)
    # Create an entry for name
    name_entry = Entry(window, width=20)
    name_entry.place(x=200, y=50)
    # Append the name
    data.append(name_entry)
    
    # Create a label for registration number
    reg_no_label = Label(window, text="Registration Number:")
    reg_no_label.place(x=50, y=100)
    # Create an entry for registration number
    reg_no_entry = Entry(window, width=20)
    reg_no_entry.place(x=200, y=100)
    # Append the registration number
    data.append(reg_no_entry)
    
    # Create a label for specialization
    specialization_label = Label(window, text="Specialization:")
    specialization_label.place(x=50, y=150)
    # Create an entry for specialization
    specialization_entry = Entry(window, width=20)
    specialization_entry.place(x=200, y=150)
    # Append the specialization
    data.append(specialization_entry)
    
    # Create a label for mobile number
    mobile_no_label = Label(window, text="Mobile Number:")
    mobile_no_label.place(x=50, y=200)
    # Create a entry for mobile number
    mobile_no_entry = Entry(window, width=20)
    mobile_no_entry.place(x=200, y=200)
    # Append the mobile number
    data.append(mobile_no_entry)
    
    # Create a label for email
    email_label = Label(window, text="Email:")
    email_label.place(x=50, y=250)
    # Create an entry for email
    email_entry = Entry(window, width=20)
    email_entry.place(x=200, y=250)
    # Append the email
    data.append(email_entry)
    
    # Create a label for password
    password_label = Label(window, text="Password:")
    password_label.place(x=50, y=300)
    # Create an entry for password
    password_entry = Entry(window, width=20)
    password_entry.place(x=200, y=300)
    # Append the password
    data.append(password_entry)
    
    # Create a button to register
    register_btn = Button(window, text="Register", command=lambda: register(data))
    register_btn.place(x=200, y=350, width=200)
    
    # Run the login window
    window.mainloop()
    
# Create a function to register the user
def register(data):
    try:
        # Connect to the database
        db = sql.connect(database="student.db")
        # Create a cursor
        cur = db.cursor()
        
        # Create a table if not exits
        cur.execute("CREATE TABLE IF NOT EXISTS Student (name TEXT, registration TEXT, specialization TEXT, phone TEXT, email TEXT, password TEXt)")
        # Insert the data into the table
        cur.execute(f"INSERT INTO Student (name, registration, specialization, phone, email, password) VALUES('{data[0].get()}', '{data[1].get()}', '{data[2].get()}', '{data[3].get()}', '{data[4].get()}', '{data[5].get()}')")
        # Commit the changes
        db.commit()
        
        # Show a message
        messagebox.showinfo("Success", "You have successfully registered")
    except:
        messagebox.showerror("Error", "Something went wrong")
