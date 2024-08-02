import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sys


class Checkout:
    def __init__(self, username):
        self.window = None
        self.tree = None
        self.total_label = None
        self.payment_method_label = None
        self.total_price = 0.0
        self.username = username
        self.cart_items = self.read_cart_items()

    def read_cart_items(self):
        items = []
        try:
            with open('temporary_cart.txt', 'r') as file:
                for line in file:
                    item_data = line.strip().split(' : ')
                    if len(item_data) == 3:
                        name, quantity, total_price = item_data
                        items.append({
                            "name": name,
                            "quantity": int(quantity.split()[0]),  # Extract quantity as integer
                            "unit_price": self.get_price(name),
                            "total_price": int(total_price)
                        })
            return items
        except FileNotFoundError:
            return []

    def get_price(self, product_name):
        products = {
            'Helmet': 2000, 'Shoes': 4000, 'Jersey': 1800, 'Ball': 600, 'Bat': 1200,
            'Football': 1500, 'Football Jersey': 1800, 'Football shoes': 3500, 'Football nets': 2500,
            'Football T-Shirt': 1500,
            'Basketball': 2000, 'Crew socks': 500, 'Shooter sleeves': 800, 'Backpack': 2500,
            'Skinny hairband': 300,
            'Baseball Cleats': 3500, 'Baseball leg guards': 1500, 'Baseball chest protector': 2000,
            'Baseball T-shirt': 1200, 'Baseball bat': 2500,
            'Soccer Cleats': 3000, 'Soccer Shoes': 2800, 'Soccer pants': 1500, 'Soccer T-Shirt': 1000,
            'Soccer ball': 700,
            'Tennis ball': 600, 'Tennis T-shirt': 1200, 'Tennis shoes': 3500, 'Tennis rackets': 4500,
            'Tennis P-cap': 500,
            'Hockey Jersey': 1800, 'Hockey Hat': 400, 'Hockey Stick': 3000, 'Hockey ball': 600,
            'Hockey shoes': 3500,
            'T-shirts': 1200, 'Shorts': 800, 'Jackets': 2500, 'Hoodie': 2000, 'Cleats': 3000
        }
        return products.get(product_name, 0)

    def show_checkout(self):
        self.window = tk.Tk()
        self.window.title("Checkout")
        self.window.geometry('900x500+350+100')

        # Display current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label = tk.Label(self.window, text=f"Date & Time: {current_datetime}", font=("Arial", 12))
        self.datetime_label.pack(pady=10)

        # Create a frame for the checkout items
        self.checkout_frame = tk.Frame(self.window)
        self.checkout_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Treeview to display checkout items in a tabular form
        self.tree = ttk.Treeview(self.checkout_frame, columns=("Item", "Quantity", "Unit Price", "Total Price"),
                                 show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Unit Price", text="Unit Price")
        self.tree.heading("Total Price", text="Total Price")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populate the Treeview with checkout items
        self.total_price = 0.0
        for item in self.cart_items:
            self.tree.insert("", tk.END, values=(item["name"], item["quantity"], f"${item['unit_price']:.2f}",
                                                 f"${item['total_price']:.2f}"))
            self.total_price += item["total_price"]

        self.payment_method_label = tk.Label(self.window, text="Payment Method:\nCash on Delivery", font=("Arial", 14))
        self.payment_method_label.pack(pady=10)

        # Label to display the total price
        self.total_label = tk.Label(self.window, text=f"Total: ${self.total_price:.2f}", font=("Arial", 14))
        self.total_label.pack(pady=10)

        # Confirm purchase button
        self.confirm_button = tk.Button(self.window, text="Confirm Purchase", command=self.confirm_purchase)
        self.confirm_button.pack(pady=10)

        self.window.mainloop()

    def confirm_purchase(self):
        try:

            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            filename = f"{self.username}_{current_datetime}.txt"
            with open(filename, 'a') as file:
                file.write(f"Date & Time: {current_datetime}\n")
                file.write(f"{'Item':<30}{'Quantity':<10}{'Unit Price':<15}{'Total Price':<15}\n")
                file.write(f"{'-' * 70}\n")
                for item in self.cart_items:
                    file.write(
                        f"{item['name']:<30}{item['quantity']:<10}{item['unit_price']:<15}{item['total_price']:<15}\n")
                file.write(f"\n{'Total':<55}{self.total_price:<15}\n")
                file.write("\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Display thank you window
        self.display_thank_you_window()

    def display_thank_you_window(self):
        self.window.withdraw()

        thank_you_window = tk.Tk()
        thank_you_window.title("Thank You")
        thank_you_window.geometry('400x200+500+300')
        thank_you_window.configure(bg="lightblue")

        # Customize the background and foreground of the labels
        thank_you_label = tk.Label(thank_you_window, text="Thank you for shopping!", font=("Arial", 24, "bold"),
                                   bg="lightblue", fg="white")
        thank_you_label.pack(pady=20)

        def safe_destroy():
            if thank_you_window.winfo_exists():
                thank_you_window.destroy()
                sys.exit()

            # Schedule the window to close after 3 seconds (3000 milliseconds)

        thank_you_window.after(3000, safe_destroy)

        thank_you_window.mainloop()
