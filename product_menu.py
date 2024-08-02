import tkinter as tk
from tkinter import ttk, Label, Frame, PhotoImage, Button, IntVar, OptionMenu, StringVar,messagebox
from view_cart import ViewCart  # Import the ViewCart class from view_cart.py


class UpdateCart:
    def __init__(self):
        self.cart = {}

    def product_list(self):
        products = [
            ['Helmet', 2000], ['Shoes', 4000], ['Jersey', 1800], ['Ball', 600], ['Bat', 1200],
            ['Football', 1500], ['Football Jersey', 1800], ['Football shoes', 3500], ['Football nets', 2500],
            ['Football T-Shirt', 1500],
            ['Basketball', 2000], ['Crew socks', 500], ['Shooter sleeves', 800], ['Backpack', 2500],
            ['Skinny hairband', 300],
            ['Baseball Cleats', 3500], ['Baseball leg guards', 1500], ['Baseball chest protector', 2000],
            ['Baseball T-shirt', 1200], ['Baseball bat', 2500],
            ['Soccer Cleats', 3000], ['Soccer Shoes', 2800], ['Soccer pants', 1500], ['Soccer T-Shirt', 1000],
            ['Soccer ball', 700],
            ['Tennis ball', 600], ['Tennis T-shirt', 1200], ['Tennis shoes', 3500], ['Tennis rackets', 4500],
            ['Tennis P-cap', 500],
            ['Hockey Jersey', 1800], ['Hockey Hat', 400], ['Hockey Stick', 3000], ['Hockey ball', 600],
            ['Hockey shoes', 3500],
            ['T-shirts', 1200], ['Shorts', 800], ['Jackets', 2500], ['Hoodie', 2000], ['Cleats', 3000],
            ['Sleeves', 600], ['Head Bands', 300]
        ]
        return products

    def __iadd__(self, product):
        if product not in self.cart:
            self.cart[product] = 1  # Add the product with quantity 1 if it's not in the cart
        else:
            if self.cart[product] < 50:
                self.cart[product] += 1  # Increase the quantity if the product is already in the cart
            else:
                messagebox.showerror("Error", f"sorry! currently we don't have more than 50 {product}")
        self.save_cart()
        return self

    def __isub__(self, product):
        if product in self.cart and self.cart[product] > 0:
            self.cart[product] -= 1  # Decrease the quantity if the product is in the cart

            if self.cart[product] == 0:
                del self.cart[product]
        self.save_cart()
        return self

    def increase(self, var, product):
        # Function created to increase the quantity on clicking the + button
        self += product  # Use __iadd__ to add the product
        var.set(self.cart[product])  # Update the variable to reflect the new quantity

    def decrease(self, var, product):
        # Function created to decrease the quantity on clicking the - button
        self -= product  # Use __isub__ to remove the product
        var.set(self.cart.get(product, 0))  # Update the variable to reflect the new quantity

    def save_cart(self):
        if not self.cart:
            # If cart is empty, clear the file content
            with open('temporary_cart.txt', 'w') as file:
                file.write("\n")  # Clear the file
        else:
            products = self.product_list()

            with open('temporary_cart.txt', 'w') as file:
                for product in self.cart:
                    for item in products:
                        if item[0] == product:
                            price = item[1]

                    file.write(f"{product} : {self.cart[product]} items : {self.cart[product] * price}\n")


class ProductMenu(tk.Tk):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self['background'] = "grey"
        self.title("Sports website")
        self.geometry('600x470+150+50')
        self.sports = Label(text="Welcome to the Online Sports Shop", bg="grey", fg="black", font=("Calibre", 20))
        self.sports.pack()

        self.label_dropdown_frame = Frame(self, bg="black")
        self.label_dropdown_frame.pack(pady=10)

        self.sports2 = Label(self.label_dropdown_frame, text="Do you wish to update your sports gear? You are at the"
                                                             " right place!", bg="black", fg="white", font=("Arial", 10)
                                                            , relief="raised")
        self.sports2.pack(side="left", padx=10)

        self.image_frame = Frame(self, bg="#AEC6CF")
        self.image_frame.pack()

        self.img3 = PhotoImage(file='S&K (2).png')
        self.img_lab2 = Label(self.image_frame, image=self.img3)
        self.img_lab2.pack()

        self.tabs = Tabs(self)
        self.tabs.notebook.pack(fill='both', expand=True)

        self.button = Button(self, text='Proceed', command=self.proceed_to_cart)
        self.button.pack()

        self.view_cart = ViewCart(self, self.username)

    def proceed_to_cart(self):
        self.tabs.update.save_cart()
        self.withdraw()  # Hide the main window
        self.view_cart.show()


class Tabs:
    def __init__(self, parent):
        self.notebook = ttk.Notebook(parent)
        self.update = UpdateCart()

        self.tabs = [
            ('Cricket Gear', '#000080'),
            ('Football Gear', '#000080'),
            ('Basketball Gear', '#000080'),
            ('Baseball Gear', '#000080'),
            ('Soccer Gear', '#000080'),
            ('Tennis Gear', '#000080'),
            ('Hockey Gear', '#000080'),
            ('Other Gear', '#000080')
        ]

        self.create_tabs()

    def create_tabs(self):
        for tab_text, tab_color in self.tabs:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=tab_text)

            button_frame = Frame(tab, bg='#d3d3d3')
            button_frame.pack(side='top', fill='x')

            if tab_text == "Cricket Gear":
                var1 = IntVar()
                self.create_label_with_buttons(button_frame, "Helmet", 2000, var1, 0)
                var2 = IntVar()
                self.create_label_with_buttons(button_frame, "Shoes", 4000, var2, 1)
                var3 = IntVar()
                self.create_label_with_buttons(button_frame, "Jersey", 1800, var3, 2)
                var4 = IntVar()
                self.create_label_with_buttons(button_frame, "Ball", 600, var4, 3)
                var5 = IntVar()
                self.create_label_with_buttons(button_frame, "Bat", 1200, var5, 4)

            if tab_text == "Football Gear":
                var6 = IntVar()
                self.create_label_with_buttons(button_frame, "Football", 1500, var6, 5)
                var7 = IntVar()
                self.create_label_with_buttons(button_frame, "Football Jersey", 1800, var7, 6)
                var8 = IntVar()
                self.create_label_with_buttons(button_frame, "Football shoes", 3500, var8, 7)
                var9 = IntVar()
                self.create_label_with_buttons(button_frame, "Football nets", 2500, var9, 8)
                var10 = IntVar()
                self.create_label_with_buttons(button_frame, "Football T-Shirt", 1500, var10, 9)

            if tab_text == "Basketball Gear":
                var11 = IntVar()
                self.create_label_with_buttons(button_frame, "Basketball", 2000, var11, 10)
                var12 = IntVar()
                self.create_label_with_buttons(button_frame, "Crew socks", 500, var12, 11)
                var13 = IntVar()
                self.create_label_with_buttons(button_frame, "Shooter sleeves", 800, var13, 12)
                var14 = IntVar()
                self.create_label_with_buttons(button_frame, "Backpack", 2500, var14, 13)
                var15 = IntVar()
                self.create_label_with_buttons(button_frame, "Skinny hairband", 300, var15, 14)

            if tab_text == "Baseball Gear":
                var16 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball Cleats", 3500, var16, 15)
                var17 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball leg guards", 1500, var17, 16)
                var18 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball chest protector", 2000, var18, 17)
                var19 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball T-shirt", 1200, var19, 18)
                var20 = IntVar()
                self.create_label_with_buttons(button_frame, "Baseball bat", 2500, var20, 19)

            if tab_text == "Soccer Gear":
                var21 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer Cleats", 3000, var21, 20)
                var22 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer Shoes", 2800, var22, 21)
                var23 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer pants", 1500, var23, 22)
                var24 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer T-Shirt", 1000, var24, 25)
                var25 = IntVar()
                self.create_label_with_buttons(button_frame, "Soccer ball", 700, var25, 26)

            if tab_text == "Tennis Gear":
                var26 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis ball", 600, var26, 27)
                var27 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis T-shirt", 1200, var27, 28)
                var28 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis shoes", 3500, var28, 29)
                var29 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis rackets", 4500, var29, 30)
                var30 = IntVar()
                self.create_label_with_buttons(button_frame, "Tennis P-cap", 500, var30, 31)

            if tab_text == "Hockey Gear":
                var31 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Jersey", 1800, var31, 32)
                var32 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Hat", 400, var32, 33)
                var33 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey Stick", 3000, var33, 34)
                var34 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey ball", 600, var34, 35)
                var35 = IntVar()
                self.create_label_with_buttons(button_frame, "Hockey shoes", 3500, var35, 36)

            if tab_text == "Other Gear":
                var36 = IntVar()
                self.create_label_with_buttons(button_frame, "T-shirts", 1200, var36, 37)
                var37 = IntVar()
                self.create_label_with_buttons(button_frame, "Shorts", 800, var37, 38)
                var38 = IntVar()
                self.create_label_with_buttons(button_frame, "Jackets", 2500, var38, 39)
                var39 = IntVar()
                self.create_label_with_buttons(button_frame, "Hoodie", 2000, var39, 40)
                var40 = IntVar()
                self.create_label_with_buttons(button_frame, "Cleats", 3000, var40, 41)

    def create_label_with_buttons(self, parent, text, price, var, row):
        Label(parent, text=text, fg='black', bg='#d3d3d3', anchor='w').grid(row=row, column=0, sticky='w', padx=5)
        Label(parent, text=f'$ {price}', fg='black', bg='#d3d3d3', anchor='w').grid(row=row, column=1, padx=5)
        Button(parent, text="+", command= lambda: self.update.increase(var, text), fg='black', bg='#d3d3d3').grid(row=row, column=2, padx=5)
        Label(parent, textvariable=var, fg='black', bg='#d3d3d3', width=3, anchor='e').grid(row=row, column=3, padx=5)
        Button(parent, text="-", command=lambda: self.update.decrease(var, text), fg='black', bg='#d3d3d3').grid(row=row, column=4, padx=5)


