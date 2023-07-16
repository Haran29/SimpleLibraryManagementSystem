import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyodbc
import datetime


def config():

    global cursor,conn
    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-I7H6893E;'
                        'Database=lms;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()



def main():
    login_page()

def on_entry_click(event):
    global User
    if User.get() == "Username":
        User.delete(0, "end")
        User.config(fg='black')

def on_focus_out(event):
    global User
    if User.get() == "":
        User.insert(0, "Username")
        User.config(fg='grey')

def on_entry_click_password(event):
    global Password
    if Password.get() == "Password":
        Password.delete(0, "end")
        Password.config(show='*', fg='black')

def on_focus_out_password(event):
    global Password
    if Password.get() == "":
        Password.config(show='', fg='grey')
        Password.insert(0, "Password")

def on_entry_click_confirm_password(event):
    global Confirm_Password
    if Confirm_Password.get() == "Confirm Password":
        Confirm_Password.delete(0, "end")
        Confirm_Password.config(show='*', fg='black')

def on_focus_out_confirm_password(event):
    global Confirm_Password
    if Confirm_Password.get() == "":
        Confirm_Password.config(show='', fg='grey')
        Confirm_Password.insert(0, "Confirm Password")

def open_signup_page():
    if 'root' in globals() and root.winfo_exists():
        root.destroy()
    signup_page()

def open_login_page():
    global signup_window,home_window
    if 'signup_window' in globals() and signup_window is not None:
        signup_window.destroy()
        signup_window = None

    # Destroy the home window if it exists
    elif 'home_window' in globals() and home_window is not None:
        home_window.destroy()
        home_window = None

    login_page()


def open_home_page():
    global root,home_window
    if 'root' in globals() and root.winfo_exists():
        root.destroy()
    home_page()



def open_add_book_page():
    global home_window
    if 'home_window' in globals() and home_window is not None:
        home_window.destroy()
    add_book_page()


def signup_page():
    global signup_window
    def signup():
        username = User.get()
        password = Password.get()
        confirm_password = Confirm_Password.get()

        if username == "Username" or password == "Password" or confirm_password == "Confirm Password":
            # Handle empty fields error
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if password != confirm_password:
            # Handle password mismatch error
            messagebox.showerror("Error", "Passwords do not match.")
            return

        
        # Connect to the MS SQL Server database
        config()

    # Generate a unique admin_id, for example by querying the current maximum admin_id and adding 1
        cursor.execute("SELECT MAX(admin_id) FROM Admins")
        result = cursor.fetchone()
        max_admin_id = result[0]
        new_admin_id = max_admin_id + 1 if max_admin_id is not None else 1

        # Insert the signup data into the Admins table
        cursor.execute("INSERT INTO Admins (admin_id, username, password) VALUES (?, ?, ?)", (new_admin_id, username, password))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    # Show success message
        messagebox.showinfo("Success", "Signup successful!")
        open_login_page()




    
    signup_window = tk.Tk()
    signup_window.title('Signup')
    signup_window.geometry('925x500+300+200')
    signup_window.configure(bg='#fff')
    signup_window.resizable(False, False)

    # Rest of your signup page code...
    img = tk.PhotoImage(file='b2.png')
    tk.Label(signup_window, image=img, bg='white').place(x=60, y=100)

    frame = tk.Frame(signup_window, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = tk.Label(frame, text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=30, y=30)

    # Signup form fields
    global User, Password, Confirm_Password
    User = tk.Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13), fg='grey')
    User.insert(0, "Username")
    User.bind('<FocusIn>', on_entry_click)
    User.bind('<FocusOut>', on_focus_out)
    User.place(x=50, y=100)

    Password = tk.Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13), fg='grey')
    Password.insert(0, "Password")
    Password.bind('<FocusIn>', on_entry_click_password)
    Password.bind('<FocusOut>', on_focus_out_password)
    Password.place(x=50, y=150)

    Confirm_Password = tk.Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13), fg='grey')
    Confirm_Password.insert(0, "Confirm Password")
    Confirm_Password.bind('<FocusIn>', on_entry_click_confirm_password)
    Confirm_Password.bind('<FocusOut>', on_focus_out_confirm_password)
    Confirm_Password.place(x=50, y=200)

    signup_btn = tk.Button(frame, text='SIGN UP', font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='#57a1f8',
                           relief='flat', activebackground='#57a1f8', activeforeground='white',
                           command=signup)
    signup_btn.place(x=50, y=250, width=100, height=40)

    login_link = tk.Label(frame, text='Already have an account? Login', font=('Microsoft Yahei UI Light', 10),
                          fg='#57a1f8', bg='white', cursor='hand2')
    login_link.place(x=50, y=320)
    login_link.bind("<Button-1>", lambda e: open_login_page())

    signup_window.mainloop()

def login_page():
    def login():
        username = User.get()
        password = Password.get()

    # Connect to the database
        config()

    # Check if the user exists in the Admins table
        query = "SELECT * FROM Admins WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            open_home_page()
            
        else:
            messagebox.showinfo("Invalid username or password")
        

    # Close the cursor and the connection
        cursor.close()
        conn.close()
        
    global root
    root = tk.Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False, False)

    # Rest of your login page code...
    img = tk.PhotoImage(file='b2.png')
    tk.Label(root, image=img, bg='white').place(x=60, y=100)

    frame = tk.Frame(root, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = tk.Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=30, y=30)

    # Login form fields
    global User, Password
    User = tk.Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13), fg='grey')
    User.insert(0, "Username")
    User.bind('<FocusIn>', on_entry_click)
    User.bind('<FocusOut>', on_focus_out)
    User.place(x=50, y=100)

    Password = tk.Entry(frame, width=25, font=('Microsoft Yahei UI Light', 13), fg='grey')
    Password.insert(0, "Password")
    Password.bind('<FocusIn>', on_entry_click_password)
    Password.bind('<FocusOut>', on_focus_out_password)
    Password.place(x=50, y=150)

    login_btn = tk.Button(frame, text='LOGIN', font=('Microsoft Yahei UI Light', 11, 'bold'), fg='white', bg='#57a1f8',
                          relief='flat', activebackground='#57a1f8', activeforeground='white',
                          command=login)
    login_btn.place(x=50, y=250, width=100, height=40)

    signup_link = tk.Label(frame, text='Don\'t have an account? Sign Up', font=('Microsoft Yahei UI Light', 10),
                           fg='#57a1f8', bg='white', cursor='hand2')
    signup_link.place(x=50, y=320)
    signup_link.bind("<Button-1>", lambda e: open_signup_page())

    root.mainloop()
def home_page():
    global home_window
    
    home_window = Tk()
    home_window.title('Home')
    home_window.geometry('925x500+300+200')
    home_window.configure(bg='#fff')
    home_window.resizable(False, False)
    

    # Load and place the background image
    background_image = PhotoImage(file='background.png')
    background_label = Label(home_window, image=background_image, bg='white')
    background_label.place(x=500, y=100)


    # Create the home page layout with buttons
    frame = Frame(home_window, width=300, height=400,bg='white')
    frame.place(x=40, y=50)

    add_book_button = Button(frame, text='Add Book', width=20, height=2, bg='#57a1f8', fg='white',
                             font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0, command=open_add_book_page)
    add_book_button.pack(pady=10, anchor='w')

    delete_book_button = Button(frame, text='Delete Book', width=20, height=2, bg='#57a1f8', fg='white', 
                                font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0,command=delete_book_page)
    delete_book_button.pack(pady=10, anchor='w')

    borrow_book_button = Button(frame, text='Borrow Book', width=20, height=2, bg='#57a1f8', fg='white',
                                font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0,command=borrow_book_page)
    borrow_book_button.pack(pady=10, anchor='w')

    logout_button = Button(frame, text='Logout', width=20, height=2, bg='#57a1f8', fg='white',
                           font=('Microsoft Yahei UI Light', 12, 'bold'), bd=0, command=open_login_page)
    logout_button.pack(pady=10, anchor='w')

    home_window.mainloop()

def add_book_page():
    global home_window
    def go_to_homepage():
        add_book_window.destroy()  # Close the current window
        home_page()  # Open the homepage

    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        year = year_entry.get()
        description = description_entry.get("1.0", "end-1c")

        if title == '' or author == '' or genre == '' or year == '' or description == '':
            # Handle empty fields error
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            config()

            # Generate a unique book_id, for example by querying the current maximum book_id and adding 1
            cursor.execute("SELECT MAX(book_id) FROM Books")
            result = cursor.fetchone()
            max_book_id = result[0]
            new_book_id = max_book_id + 1 if max_book_id is not None else 1

            # Insert the book details into the database
            cursor.execute("INSERT INTO Books (book_id, title, author, publication_date, isbn, availability_status) "
                           "VALUES (?, ?, ?, ?, ?, ?)",
                           (new_book_id, title, author, year, '', 'Available'))

            conn.commit()
            conn.close()

            # Show success message
            messagebox.showinfo("Success", f"Book added successfully!\nBOOK ID: {new_book_id}")

            # Clear the entry fields
            title_entry.delete(0, 'end')
            author_entry.delete(0, 'end')
            genre_entry.delete(0, 'end')
            year_entry.delete(0, 'end')
            description_entry.delete("1.0", "end")

        except pyodbc.Error as e:
            # Handle any error that occurred during the database operation
            messagebox.showerror("Error", f"Database error: {str(e)}")

    # Create a new window for the add book page
    add_book_window = Tk()
    add_book_window.title('Add Book')
    add_book_window.geometry('925x500+300+200')
    add_book_window.resizable(False, False)

    # Create the frame
    frame = Frame(add_book_window, padx=20, pady=20)
    frame.pack(fill='both', expand=True)

    # Title label and entry
    title_label = Label(frame, text='Title:', font=('Helvetica', 16, 'bold'))
    title_label.pack(anchor='w')

    title_entry = Entry(frame, width=50, font=('Helvetica', 12))
    title_entry.pack(pady=5)

    # Author label and entry
    author_label = Label(frame, text='Author:', font=('Helvetica', 12))
    author_label.pack(anchor='w')

    author_entry = Entry(frame, width=50, font=('Helvetica', 12))
    author_entry.pack(pady=5)

    # Genre label and entry
    genre_label = Label(frame, text='Genre:', font=('Helvetica', 12))
    genre_label.pack(anchor='w')

    genre_entry = Entry(frame, width=50, font=('Helvetica', 12))
    genre_entry.pack(pady=5)

    # Year label and entry
    year_label = Label(frame, text='Year:', font=('Helvetica', 12))
    year_label.pack(anchor='w')

    year_entry = Entry(frame, width=50, font=('Helvetica', 12))
    year_entry.pack(pady=5)

    # Description label and entry
    description_label = Label(frame, text='Description:', font=('Helvetica', 12))
    description_label.pack(anchor='w')

    description_entry = Text(frame, width=50, height=5, font=('Helvetica', 12))
    description_entry.pack(pady=5)

    # Add Book button
    button_width = 15
    button_height = 1

    add_button = Button(frame, text='Submit', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                        font=('Helvetica', 12, 'bold'), bd=0, command=add_book)
    add_button.pack(pady=10)

    # Button to go back to the homepage
    home_button = Button(frame, text='Home', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                         font=('Helvetica', 12, 'bold'), bd=0, command=go_to_homepage)
    home_button.pack()

    add_book_window.mainloop()


def delete_book_page():
    global home_window
    def go_to_homepages():
        delete_book_window.destroy()  
        home_page()  

    home_window.destroy()
    # Create a new window for the delete book page
    delete_book_window = Tk()
    delete_book_window.title('Delete Book')
    delete_book_window.geometry('925x500+300+200')
    #delete_book_window.configure(bg='#fff')
    delete_book_window.resizable(False, False)

    # Define custom fonts
    title_font = ('Helvetica', 16, 'bold')
    label_font = ('Helvetica', 12)
    entry_font = ('Helvetica', 12)
    button_font = ('Helvetica', 12, 'bold')

    # Create the frame
    frame = Frame(delete_book_window, padx=20, pady=20)
    frame.pack(fill='both', expand=True)

    # Book number label and entry
    book_number_label = Label(frame, text='Book Number:', font=title_font)
    book_number_label.pack(anchor='w')

    book_number_entry = Entry(frame, width=50, font=entry_font)
    book_number_entry.pack(pady=5)

    # Delete Book button
    def delete_book():
        book_number = book_number_entry.get()

        if book_number == '':
            # Handle empty field error
            messagebox.showerror("Error", "Please enter the book number.")
            return


        config()

            # Check if the book exists
        cursor.execute("SELECT * FROM Books WHERE book_id = ?", (book_number,))
        book = cursor.fetchone()

        if book is None:
                # Show error message if the book doesn't exist
            messagebox.showerror("Error", "Book not found.")
        else:
                # Delete the book from the database
            cursor.execute("DELETE FROM Books WHERE book_id = ?", (book_number,))
            conn.commit()
                # Show success message
            messagebox.showinfo("Success", "Book deleted successfully.")

       

        book_number_entry.delete(0, 'end')

    delete_button = Button(frame, text='Delete Book', width=12, height=2, bg='#57a1f8', fg='white',
                           font=button_font, bd=0, command=delete_book)
    delete_button.pack(pady=10)



    home_button = Button(frame, text='Home', width=12, height=2, bg='#57a1f8', fg='white',
                         font=button_font, bd=0, command=go_to_homepages)
    home_button.pack(pady=10)

    background_image = PhotoImage(file='background.png')
    background_label = Label(delete_book_window, image=background_image)
    background_label.place(x=300, y=250)


    delete_book_window.mainloop()



def borrow_book_page():
    global borrow_book_window
    global home_window
    def go_to_homepagess():
        borrow_book_window.destroy()  # Close the current window
        home_page()  # Open the homepage
    home_window.destroy()
    def borrow_book():
        book_id = book_id_entry.get()
        member_id = member_id_entry.get()
        loan_date = datetime.datetime.now().strftime('%Y-%m-%d')
        due_date = (datetime.datetime.strptime(loan_date, "%Y-%m-%d") + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

        if book_id == '' or member_id == '' or loan_date == '':
            # Handle empty field error
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            config()

            # Check if the book is available
            cursor.execute("SELECT availability_status FROM Books WHERE book_id = ?", (book_id,))
            result = cursor.fetchone()

            if result and result[0] == 'Available':
                # Generate a unique loan_id, for example by querying the current maximum loan_id and adding 1
                cursor.execute("SELECT MAX(loan_id) FROM Loans")
                result = cursor.fetchone()
                max_loan_id = result[0]
                new_loan_id = max_loan_id + 1 if max_loan_id is not None else 1

                # Calculate the due date (e.g., 14 days from the loan date)
                due_date = (datetime.datetime.strptime(loan_date, "%Y-%m-%d") + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

                # Insert the loan record into the database
                cursor.execute("INSERT INTO Loans (loan_id, member_id, book_id, loan_date, due_date, return_date) "
                               "VALUES (?, ?, ?, ?, ?, NULL)",
                               (new_loan_id, member_id, book_id, loan_date, due_date))

                # Update the book's availability status
                cursor.execute("UPDATE Books SET availability_status = 'Borrowed' WHERE book_id = ?", (book_id,))

                conn.commit()
                conn.close()

                # Show success message
                messagebox.showinfo("Success", f"Book borrowed successfully!\nLoan ID: {new_loan_id}")

                # Clear the entry fields
                book_id_entry.delete(0, 'end')
                member_id_entry.delete(0, 'end')
            else:
                messagebox.showerror("Error", "Book not available for borrowing.")

        except pyodbc.Error as e:
            # Handle any error that occurred during the database operation
            messagebox.showerror("Error", f"Database error: {str(e)}")

        # Your existing borrow_book() function code here

    # Create a new window for the borrow book page
    borrow_book_window = Tk()
    borrow_book_window.title('Borrow Book')
    borrow_book_window.geometry('925x500+300+200')
    borrow_book_window.resizable(False, False)

    # Create the frame
    frame = Frame(borrow_book_window, padx=20, pady=20)
    frame.pack(fill='both', expand=True)

    # Book ID label and entry
    book_id_label = Label(frame, text='Book ID:', font=('Helvetica', 16, 'bold'))
    book_id_label.pack(anchor='w')

    book_id_entry = Entry(frame, width=50, font=('Helvetica', 12))
    book_id_entry.pack(pady=5)

    # Member ID label and entry
    member_id_label = Label(frame, text='Member ID:', font=('Helvetica', 16, 'bold'))
    member_id_label.pack(anchor='w')

    member_id_entry = Entry(frame, width=50, font=('Helvetica', 12))
    member_id_entry.pack(pady=5)

    # Borrow Book button
    button_width = 15
    button_height = 1

    borrow_button = Button(frame, text='Borrow', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                           font=('Helvetica', 12, 'bold'), bd=0, command=borrow_book)
    borrow_button.pack(pady=10)

    return_button = Button(frame, text='return', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                           font=('Helvetica', 12, 'bold'), bd=0, command=return_book_page)
    return_button.pack(pady=10)

    # Button to go back to the homepage
    home_button = Button(frame, text='Home', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                         font=('Helvetica', 12, 'bold'), bd=0, command=go_to_homepagess)
    home_button.pack()

    background_image = PhotoImage(file='background.png')
    background_label = Label(borrow_book_window, image=background_image, bg='white')
    background_label.place(x=600, y=300)

    borrow_book_window.mainloop()

def return_book_page():
    global home_window
    global borrow_book_window

    def go_to_homepage():
        return_book_window.destroy()  # Close the current window
        home_page()  # Open the homepage

    borrow_book_window.destroy()
    def return_book():
        loan_id = loan_id_entry.get()

        if loan_id == '':
            # Handle empty field error
            messagebox.showerror("Error", "Please enter the Loan ID.")
            return

        try:
            config()

            # Check if the loan exists and the book is borrowed
            cursor.execute("SELECT * FROM Loans WHERE loan_id = ? AND return_date IS NULL", (loan_id,))
            result = cursor.fetchone()

            if result:
                book_id = result[2]

                # Update the return date for the loan
                return_date = datetime.datetime.now().strftime('%Y-%m-%d')
                cursor.execute("UPDATE Loans SET return_date = ? WHERE loan_id = ?", (return_date, loan_id))

                # Update the book's availability status
                cursor.execute("UPDATE Books SET availability_status = 'Available' WHERE book_id = ?", (book_id,))

                conn.commit()
                conn.close()

                # Show success message
                messagebox.showinfo("Success", "Book returned successfully!")

                # Clear the entry field
                loan_id_entry.delete(0, 'end')
            else:
                messagebox.showerror("Error", "Loan not found or book already returned.")

        except pyodbc.Error as e:
            # Handle any error that occurred during the database operation
            messagebox.showerror("Error", f"Database error: {str(e)}")

    # Create a new window for the return book page
    return_book_window = Tk()
    return_book_window.title('Return Book')
    return_book_window.geometry('925x500+300+200')
    return_book_window.resizable(False, False)

    # Create the frame
    frame = Frame(return_book_window, padx=20, pady=20)
    frame.pack(fill='both', expand=True)

    # Loan ID label and entry
    loan_id_label = Label(frame, text='Loan ID:', font=('Helvetica', 16, 'bold'))
    loan_id_label.pack(anchor='w')

    loan_id_entry = Entry(frame, width=50, font=('Helvetica', 12))
    loan_id_entry.pack(pady=5)

    # Return Book button
    button_width = 15
    button_height = 1

    return_button = Button(frame, text='Return', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                           font=('Helvetica', 12, 'bold'), bd=0, command=return_book)
    return_button.pack(pady=10)

    # Button to go back to the homepage
    home_button = Button(frame, text='Home', width=button_width, height=button_height, bg='#57a1f8', fg='white',
                         font=('Helvetica', 12, 'bold'), bd=0, command=go_to_homepage)
    home_button.pack()

    background_image = PhotoImage(file='background.png')
    background_label = Label(return_book_window, image=background_image, bg='white')
    background_label.place(x=600, y=300)        

    return_book_window.mainloop()


if __name__ == '__main__':
    main()


