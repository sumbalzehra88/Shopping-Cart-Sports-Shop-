import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from product_menu import ProductMenu


class ManageUserAccount:
    def __init__(self, filename="user_info.txt"):
        """
        Initialize the ManageUserAccount class.
        :param filename: The name of the file to store user information.
        """
        self.filename = filename

    def save_user(self, username, password, address, contact):
        """
        Save user details to a file in a formatted manner.
        :param username: The username of the user.
        :param password: The password of the user.
        :param address: The address of the user.
        :param contact: The contact information of the user.
        """
        with open(self.filename, "a+") as f:
            f.write(f"{'Username':<15} : {'Password':<15} : {'Address':<30} : {'Contact':<15}\n")
            f.write(f"{'-' * 80}\n")
            f.write(f"{username:<15} : {password:<15} : {address:<30} : {contact:<15}\n")

    def user_exist(self, username):
        """
        Check if a username already exists in the file.
        :param username: The username to check.
        :return: True if the username exists, False otherwise.
        """
        try:
            with open(self.filename, "r") as f:
                # Skip the headers
                next(f)
                next(f)
                for line in f:
                    user_data = line.strip().split(" : ")
                    if len(user_data) == 4:
                        file_username = user_data[0].strip()
                        if file_username == username:
                            return True
        except FileNotFoundError:
            return False
        return False

    def authenticate_user(self, username, password):
        """
        Verify user credentials.
        :param username: The username of the user.
        :param password: The password of the user.
        :return: True if credentials are valid, False otherwise.
        """
        try:
            with open(self.filename, "r") as f:
                # Skip the headers
                next(f)
                next(f)
                for line in f:
                    user_data = line.strip().split(" : ")
                    if len(user_data) == 4:
                        file_username, file_password, file_address, file_contact = user_data
                        if file_username.strip() == username and file_password.strip() == password:
                            return True
            return False
        except FileNotFoundError:
            return False


class Interface:
    def __init__(self):
        super().__init__()
        """
        Initialize the Interface class.
        """
        self.root = tk.Tk()
        self.root.title("ONLINE SPORTS WORLD")
        self.root.geometry("900x500+300+150")
        self.root.configure(bg="#fff")

        # Display an image on the root window by calling display function
        self.display_image("login.png")

        # Initialize instance variables
        self.signup_frame = None
        self.signin_frame = None
        self.username_entry = None
        self.password_entry = None
        self.address_entry = None
        self.contact_entry = None
        self.signup_button = None
        self.signin_button = None
        self.title_label = None
        self.label = None

        # Create an instance of ManageUserAccount
        self.account_manager = ManageUserAccount()

        # Create the signup widgets
        self.create_widgets_signup()

        self.root.mainloop()

    def display_image(self, file):
        """
        Display an image on the root window.
        :param file: The path to the image file.
        """
        # Load image
        image = Image.open(file)
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(self.root, image=photo, bg="white")
        image_label.image = photo
        image_label.place(x=50, y=50)

    def create_widgets_signup(self):
        """
        Create buttons and entry labels to get user information sign up widgets
        """
        self.signup_frame = tk.Frame(self.root, width=350, height=457, bg="white")
        self.signup_frame.place(x=480, y=20)

        self.title_label = tk.Label(self.signup_frame, text="Sign up", fg="#57a1f8", bg="white",
                                    font=("Microsoft YaHei UI light", 20, "bold"))
        self.title_label.place(x=125, y=5)

        # Username entry widget
        self.username_entry = tk.Entry(self.signup_frame, width=25, fg="Black", border=0, bg="white",
                                       font=("Microsoft YaHei UI light", 10, "bold"))
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, "username")

        self.username_entry.bind("<FocusIn>", self.on_focus_in)
        self.username_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signup_frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Password entry widget
        self.password_entry = tk.Entry(self.signup_frame, width=25, fg="Black", border=0, bg="white",
                                       font=("Microsoft YaHei UI light", 10, "bold"))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, "password")

        self.password_entry.bind("<FocusIn>", self.on_focus_in)
        self.password_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signup_frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Address entry widget
        self.address_entry = tk.Entry(self.signup_frame, width=25, fg="Black", border=0, bg="white",
                                      font=("Microsoft YaHei UI light", 10, "bold"))
        self.address_entry.place(x=30, y=220)
        self.address_entry.insert(0, "address")

        self.address_entry.bind("<FocusIn>", self.on_focus_in)
        self.address_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signup_frame, width=295, height=2, bg="black").place(x=25, y=247)

        # Contact entry widget
        self.contact_entry = tk.Entry(self.signup_frame, width=25, fg="Black", border=0, bg="white",
                                      font=("Microsoft YaHei UI light", 10, "bold"))
        self.contact_entry.place(x=30, y=290)
        self.contact_entry.insert(0, "contact")

        self.contact_entry.bind("<FocusIn>", self.on_focus_in)
        self.contact_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signup_frame, width=295, height=2, bg="black").place(x=25, y=317)

        # Signup button to submit detail for create_account
        self.signup_button = tk.Button(self.signup_frame, command=self.signup, width=39, pady=7, text="Sign up",
                                       bg="#57a1f8", fg="white", border=0)
        self.signup_button.place(x=35, y=340)

        # Ask user if they have an account
        self.label = tk.Label(self.signup_frame, text="Do You Have an Account?", fg="Black", bg="white",
                              font=("Microsoft YaHei UI light", 8, "bold"))
        self.label.place(x=75, y=390)

        # Signin button for users who have an account
        self.signin_button = tk.Button(self.signup_frame, width=6, text="Sign in", fg="#57a1f8",
                                       command=self.show_signin_window, bg="white", border=0, cursor="hand2")
        self.signin_button.place(x=270, y=390)

    def create_widgets_signin(self):
        """
        Create buttons and entry labels to get user information
        """
        self.signin_frame = tk.Frame(self.root, width=350, height=350, bg="white")
        self.signin_frame.place(x=480, y=20)

        self.title_label = tk.Label(self.signin_frame, text="Sign in", fg="#57a1f8", bg="white",
                                    font=("Microsoft YaHei UI light", 20, "bold"))
        self.title_label.place(x=125, y=5)

        # Username entry widget
        self.username_entry = tk.Entry(self.signin_frame, width=25, fg="Black", border=0, bg="white",
                                       font=("Microsoft YaHei UI light", 10, "bold"))
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, "username")

        self.username_entry.bind("<FocusIn>", self.on_focus_in)
        self.username_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signin_frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Password entry widget
        self.password_entry = tk.Entry(self.signin_frame, width=25, fg="Black", border=0, bg="white",
                                       font=("Microsoft YaHei UI light", 10, "bold"))
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, "password")

        self.password_entry.bind("<FocusIn>", self.on_focus_in)
        self.password_entry.bind("<FocusOut>", self.on_focus_out)

        tk.Frame(self.signin_frame, width=295, height=2, bg="black").place(x=25, y=177)

        # Signin button
        self.signin_button = tk.Button(self.signin_frame, width=39, command=self.signin, pady=7, text="Sign in",
                                       bg="#57a1f8", fg="white", border=0)
        self.signin_button.place(x=35, y=280)

    def show_product_menu(self):
        """
        Create and display the ProductMenu window.
        """
        product_menu = ProductMenu()  # Pass self.root or any necessary data
        product_menu.mainloop()

    def on_focus_in(self, event):
        """
        Handle the focus-in event for entry widgets.
        :param event: The focus-in event.
        """
        if event.widget.get() in ["username", "password", "address", "contact"]:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")

    def on_focus_out(self, event):
        """
        Handle the focus-out event for entry widgets.
        :param event: The focus-out event.
        """
        if event.widget.get() == "":
            default_text = {
                self.username_entry: "username",
                self.password_entry: "password",
                self.address_entry: "address",
                self.contact_entry: "contact",
            }
            event.widget.insert(0, default_text[event.widget])
            event.widget.config(fg="black")

    def show_product_menu(self, username):
        """
        Create and display the ProductMenu window with the username.
        """
        product_menu = ProductMenu(username=username)  # Pass the username
        product_menu.mainloop()

    def show_signin_window(self):
        """
        Switch to the sign-in window.
        """
        self.signup_frame.destroy()
        self.create_widgets_signin()

    def signup(self):
        """
        Handle the signup process.
        """
        # Get user input
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        address = self.address_entry.get().strip()
        contact = self.contact_entry.get().strip()

        # Validate input fields
        if username == "username" or password == "password" or address == "address" or contact == "contact":
            messagebox.showerror("Error", "Please fill all the fields.")
            return

        # Validate each input field individually
        if not Errors.is_valid_username(username):
            messagebox.showerror("Invalid Input",
                                 "Invalid Username. Username should be at least 3 characters long and contain only alphabetic characters dont give space between name.")
            return

        if not Errors.is_valid_password(password):
            messagebox.showerror("Invalid Input",
                                 "Invalid Password. Password should be at least 8 characters long and contain at least one digit.")
            return

        if not Errors.is_valid_address(address):
            messagebox.showerror("Invalid Input", "Invalid Address. Address should be at least 5 characters long.")
            return

        if not Errors.is_valid_contact(contact):
            messagebox.showerror("Invalid Input", "Invalid Contact. Contact should be exactly 11 digits long.")
            return

        # Check if username already exists
        if self.account_manager.user_exist(username):
            messagebox.showerror("Error", "Username already exists.")
            return

        # Save user details if all validations pass
        self.account_manager.save_user(username, password, address, contact)
        messagebox.showinfo("Success", "Signup successful!")
        self.root.destroy()
        # Create and display the product menu window after signup
        self.show_product_menu(username)

    def signin(self):
        """
        Handle the signin process.
        """
        # Get user input
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Validate input fields
        if username == "username" or password == "password":
            messagebox.showerror("Error", "Please fill all the fields.")
            return

        # Validate username and password
        if not Errors.is_valid_username(username):
            messagebox.showerror("Invalid Input", "Invalid Username.")
            return

        if not Errors.is_valid_password(password):
            messagebox.showerror("Invalid Input",
                                 "Invalid Password. Password should be at least 8 characters long and contain at least one digit.")
            return

        # Authenticate user
        if self.account_manager.authenticate_user(username, password):
            messagebox.showinfo("Success", "Signin successful!")
            self.root.destroy()
            # Create and display the product menu window after signup
            self.show_product_menu(username)
            # Proceed to the main application window or functionality
        else:
            messagebox.showerror("Error", "Invalid username or password.")


class Errors:
    @staticmethod
    def is_valid_username(username):
        """
        Check if the username is valid.
        :param username: The username to validate.
        :return: True if the username is valid, False otherwise.
        """
        return len(username) >= 3 and username.isalpha()

    @staticmethod
    def is_valid_password(password):
        """
        Check if the password is valid.
        :param password: The password to validate.
        :return: True if the password is valid, False otherwise.
        """
        return len(password) >= 8 and any(char.isdigit() for char in password)

    @staticmethod
    def is_valid_address(address):
        """
        Check if the address is valid.
        :param address: The address to validate.
        :return: True if the address is valid, False otherwise.
        """
        return len(address) >= 5

    @staticmethod
    def is_valid_contact(contact):
        """
        Check if the contact is valid.
        :param contact: The contact to validate.
        :return: True if the contact is valid, False otherwise.
        """
        return contact.isdigit() and len(contact) == 11


if __name__ == "__main__":
    Interface()
