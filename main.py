# Import all the required modules
from tkinter import Tk, Button
from student_login import student_login
from new_student import new_student
from supervisor import supervisor


# Create a function to create the main window
def main():
    # Create the main window
    window = Tk()
    # Set the title of the main window
    window.title("Student")
    # Set the size of the main window
    window.geometry("600x400")
    
    # Create a login button
    login_btn = Button(window, text="Login", width=20, command=student_login)
    login_btn.place(x=200, y=100)
    
    # Create a button for new student
    new_user_btn = Button(window, text="New User", width=20, command=new_student)
    new_user_btn.place(x=200, y=150)
    
    # Create a button for request for supervisor
    supervisor_btn = Button(window, text="Request for Supervisor", width=20, command=supervisor)
    supervisor_btn.place(x=200, y=200)
    
    # Start the main window
    window.mainloop()


# Run the main window
if __name__ == "__main__":
    main()
