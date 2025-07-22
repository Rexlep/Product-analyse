import customtkinter as ctk

def update_total_price(*args):
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        total = price * quantity
        total_price_label.configure(text=f"Total Price: {total} $")
    except ValueError:
        total_price_label.configure(text="Total Price: -")

app = ctk.CTk()
app.geometry("400x300")
app.title("Live Total Price")

# Entry for price
price_entry = ctk.CTkEntry(app, placeholder_text="Price")
price_entry.pack(pady=10)

# Entry for quantity
quantity_entry = ctk.CTkEntry(app, placeholder_text="Quantity")
quantity_entry.pack(pady=10)

# Label to show total price
total_price_label = ctk.CTkLabel(app, text="Total Price: -", font=("Arial", 14))
total_price_label.pack(pady=10)

# Bind both entries to call update function when changed
price_entry.bind('<KeyRelease>', update_total_price)
quantity_entry.bind('<KeyRelease>', update_total_price)

app.mainloop()
