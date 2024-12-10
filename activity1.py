import tkinter as tk
from tkinter import messagebox, ttk
class restaurantordermanegment:
    def __init__(self, root):
        self.root = root
        self.root.title("restaurant order managment")
        self.menu_items = {
            "Fries Meal" : 2,
            "Special Lunch" : 3,
            "Family Breafast/Lunch/Dinner" : 10,
            "Burger" : 3,
            "Pizza" : 3.5,
            "Ice Cream" : 1,
            "Beverages" : 2
        }
        self.exchange_rate = 280
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx = 0.5, rely = 0.5, anchor=tk.CENTER)
        ttk.Label(frame, text = "restaurant order management", font = ("Arial", 20, "bold")).grid(row=0, columnspan=3, padx = 10, pady = 10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i, (item, price) in enumerate(self.menu_items.items(), start = 1):
            label = ttk.Label(frame, text = f"{item} (${price}):", font = ("Arial", 12))
            label.grid(row = i, column = 0, padx = 10, pady = 10)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame, width = 5)
            quantity_entry.grid(row = i, column = 1, padx = 10, pady = 5)
            self.menu_quantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text = "Currency", font = ("Arial", 12)).grid