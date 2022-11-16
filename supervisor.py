# Import all the required modules
from tkinter import Tk, Button
from supervisor_login import supervisor_login
from new_supervisor import new_supervisor


# Create a function to create the supervisor window
def supervisor():
    # Create the login window
    window = Tk()
    # Set the title of the login window
    window.title("Supervisor")
    # Set the size of the login window
    window.geometry("600x400")
    
    # Create a login button
    login_btn = Button(window, text="Login", command=supervisor_login)
    login_btn.place(x=200, y=100, width=200)
    
    # Create a button for new user
    new_user_btn = Button(window, text="New User", command=new_supervisor)
    new_user_btn.place(x=200, y=150, width=200)
    
    # Create a button for open hours
    open_hours_btn = Button(window, text="Open Hours")
    open_hours_btn.place(x=200, y=200, width=200)
    
    # Create a button for select student
    select_student_btn = Button(window, text="Select Student")
    select_student_btn.place(x=200, y=250, width=200)
    
    # Run the supervisor window
    window.mainloop()
