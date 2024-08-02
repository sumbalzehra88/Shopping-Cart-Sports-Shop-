import tkinter as tk
from tkinter import ttk
from check_out import Checkout


class ViewCart:
    def __init__(self, main_window, username):
        super().__init__()
        self.cart_items = []
        self.view = None
        self.tree = None
        self.username = username
        self.main_window = main_window

    def read_items_from_file(self):
        self.cart_items = []
        try:
            with open('temporary_cart.txt', 'r') as file:
                for line in file:
                    item_data = line.strip().split(' : ')
                    if len(item_data) == 3:
                        name, quantity, total_price = item_data
                        self.cart_items.append({
                            "name": name,
                            "quantity": int(quantity.split()[0]),  # Extract quantity as integer
                            "price": int(total_price)
                        })
        except FileNotFoundError:
            pass  # If the file doesn't exist, assume no items in the cart

    def show(self):
        self.read_items_from_file()  # Read the latest cart items each time `show` is called
        self.view = tk.Tk()
        self.view.title("View Cart")
        self.view.geometry('600x370+150+50')

        # Create a frame for the cart items
        self.cart_frame = tk.Frame(self.view)
        self.cart_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Treeview to display cart items in a tabular form
        self.tree = ttk.Treeview(self.cart_frame, columns=("Item", "Quantity", "Price"), show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populate the Treeview with cart items
        for item in self.cart_items:
            self.tree.insert("", tk.END, values=(item["name"], item["quantity"], f"${item['price']}"))

        # Buttons (e.g., Checkout, Continue Shopping)
        self.button_frame = tk.Frame(self.view)
        self.button_frame.pack(pady=10)

        self.checkout_button = tk.Button(self.button_frame, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=0, column=0, padx=5)

        self.continue_button = tk.Button(self.button_frame, text="Continue Shopping", command=self.continue_shopping)
        self.continue_button.grid(row=0, column=1, padx=5)

        self.view.mainloop()

    def continue_shopping(self):
        self.view.destroy()
        self.main_window.deiconify()  # Show the main product menu window

    def checkout(self):
        self.view.destroy()
        checkout = Checkout(self.username)
        checkout.show_checkout()  # Assuming Checkout has a show_checkout method to display the checkout window
