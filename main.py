import customtkinter as ctk
import csv
import pandas as pd
from CTkMessagebox import CTkMessagebox
from datetime import datetime

from docutils.nodes import entry


# -------------------- Functions --------------------


def is_float(value):
    """This function checks if a string is a float."""
    try:
        # Check if we can change the value into flot
        float(value)
        return True
    except ValueError as e:
        CTkMessagebox(title="Info", message=f"{e}", icon='cancel')


def is_valid_date(date_string, date_format="%Y-%m-%d"):
    """This function check the type of  the string and see if it is a valid date."""
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def write_new_information():
    """This function writes the new information to the dataset"""

    # Extract the info from entry
    customer_id = customer_id_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    product_name = product_name_combo_box.get()
    date = date_entry.get()

    # Make a dict with their name and their corresponding value
    fields = {
        'Customer ID': customer_id,
        'Quantity': quantity,
        'Price': price,
        'Product Name': product_name,
        'Date': date,
    }

    # Make a dict for number fields
    number_fields = {
        'Customer ID': customer_id,
        'Quantity': quantity,
    }

    # hi my name is amir

    listddd = [] 


    # Make a list to add the not True values in them
    not_number_fields = []
    empty_fields = []

    # Loop through the dict and see if the entry values are empty or not
    for field_name, value in number_fields.items():
        if not value.isdigit(): not_number_fields.append(field_name)

    for field_name, value in fields.items():
        if not value: empty_fields.append(field_name)  # This part check if the string is empty and if it is added it to list

    # Check if the lists are empty or not if it is not empty we get an error for digit numbers or empty fields
    # For empty fields
    if empty_fields:
        CTkMessagebox(title="Info", message=f"The following fields cannot be empty: {', '.join(empty_fields)}", icon='cancel')

    # For not a number of fields
    if not_number_fields:
        CTkMessagebox(title="Info", message=f"The following fields should be number: {', '.join(not_number_fields)}", icon='cancel')
        return

    # Check if it is not a valid date show an error
    if not is_valid_date(date, '%d/%m/%Y'):
        CTkMessagebox(title="Info", message="The date is not valid format is (Day/Month/Year)", icon='cancel')

    # Check if the price is a number or not
    if not is_float(price):
        CTkMessagebox(title="Info", message=f"Enter a number for price", icon='cancel')


    # This part runs when there is no error
    else:
        current_time = datetime.now().time().replace(microsecond=0)
        current_date = datetime.strptime(date, '%d/%m/%Y')

        combined_datetime = datetime.combine(current_date, current_time)

        # Make a row for writing it in csv file
        data = [customer_id, quantity, float(price), product_name, combined_datetime]

        # Open the file
        with open('products.csv', 'a', newline='') as csvfile:
            # CVS writer writes the row
            writer = csv.writer(csvfile)
            writer.writerow(data)

            # Add all text inputs in a list to iterate into it and delete the text in it
            all_entry = [customer_id_entry, quantity_entry, price_entry, date_entry]
            # Loop for iterate on the text inputs list
            for i in all_entry:
                i.delete(0, 'end')

            # Show message when the data has been added
            CTkMessagebox(title="Info", message="The information added")


def expense_tracker():
    # Read the file and change it into data frame
    df = pd.read_csv('products.csv')

    df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

    # Delete the old stuf in list box
    expense_tracker_list_box.delete('0.0', 'end')
    # Insert the data frame in list box
    expense_tracker_list_box.insert('0.0', df.to_string())


def checkbox_event():
    """This function is called when the checkbox is clicked"""
    reverse = checkbox.get()  # Get the value of the checkbox
    value = combobox_expense_tracker.get()  # Get the value of the combobox
    df = pd.read_csv('products.csv')
    df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

    if value == 'Date':
        df = df.sort_values(by='date', ascending=not reverse).reset_index(drop=True)
    elif value == 'Price':
        df = df.sort_values(by='price', ascending=not reverse).reset_index(drop=True)
    elif value == 'Quantity':
        df = df.sort_values(by='quantity', ascending=not reverse).reset_index(drop=True)
    elif value == 'Normal':
        df = df.sort_values(by='date', ascending=not reverse).reset_index(drop=True)

    expense_tracker_list_box.delete('0.0', 'end')
    expense_tracker_list_box.insert('0.0', df.to_string())


def change_order(value):
    """This function changes the order of df based on user choice"""
    print('This is the user ',  value)

    if value == 'Normal':
        df = pd.read_csv('products.csv')
        
        # Make a total price column and put a dolor sign right to it
        df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

        # Delete the old stuf in list box
        expense_tracker_list_box.delete('0.0', 'end')
        # Insert the data frame in list box
        expense_tracker_list_box.insert('0.0', df.to_string())


    if value == 'Date':
        df = pd.read_csv('products.csv')
        
        # Make a total price column and put a dolor sign right to it
        df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

        df = df.sort_values(by='date', ascending=False).reset_index(drop=True)

        # Delete the old stuf in list box
        expense_tracker_list_box.delete('0.0', 'end')
        # Insert the data frame in list box
        expense_tracker_list_box.insert('0.0', df.to_string())

    if value == 'Price':
        df = pd.read_csv('products.csv')
        
        # Make a total price column and put a dolor sign right to it
        df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

        df = df.sort_values(by='price', ascending=False).reset_index(drop=True)

        # Delete the old stuf in list box
        expense_tracker_list_box.delete('0.0', 'end')
        # Insert the data frame in list box
        expense_tracker_list_box.insert('0.0', df.to_string())

    if value == 'Quantity':
        df = pd.read_csv('products.csv')
        
        # Make a total price column and put a dolor sign right to it
        df['total price'] = (df['quantity'] * df['price']).apply(lambda x: f"{x} $")

        df = df.sort_values(by='price', ascending=False).reset_index(drop=True)

        # Delete the old stuf in list box
        expense_tracker_list_box.delete('0.0', 'end')
        # Insert the data frame in list box
        expense_tracker_list_box.insert('0.0', df.to_string())


def product_analyse():
    """This function analyse products with their sales"""
    df1 = pd.read_csv('products.csv')

    df2 = pd.DataFrame({
        'Product': df1['product_name'],
        'Quantity': df1['quantity']
    })

    df2['Quantity'] = pd.to_numeric(df2['Quantity'], errors='coerce')

    grouped = df2.groupby('Product').agg({
        'Quantity': 'sum'
    }).reset_index()

    df1['date'] = pd.to_datetime(df1['date'])

    grouped['Month'] = df1['date'].dt.month_name()
    grouped['Date']  = df1['date']

    date_sale = grouped.groupby('Date')['Quantity'].sum()

    # This parts analyse the total sale
    total_sale = grouped.groupby('Month')['Quantity'].sum()

    print(date_sale)

    for month, total in total_sale.items():
        if total > 10:
            product_analyse_list_box2.insert('0.0', f"In {month}, high total sales were recorded ({total} items)\n")


    for date, total in date_sale.items():
        if total > 100:
            product_analyse_list_box2.insert('0.0', f"In {date} {total} recorded\n")
 

    product_analyse_list_box.delete('0.0', 'end')
    product_analyse_list_box.insert('0.0', grouped.to_string(index=False))


def top_level():
    """This function help you to add products into combobox"""
    def write_product_name():
        with open('list_of_products.txt', 'a') as product:
            product.write(entry.get() + '\n')

        entry.delete(0, ctk.END)
        CTkMessagebox(title="Info", message=f"Product added")


    top_level_window = ctk.CTkToplevel()
    top_level_window.geometry('400x300')
    top_level_window.grab_set()

    label = ctk.CTkLabel(top_level_window, text='Product name', font=('Arial', 20)).pack(side='top', pady=20)
    entry = ctk.CTkEntry(top_level_window, placeholder_text='Product name', width=300, height=40)
    entry.pack(side='top', pady=20)

    button = ctk.CTkButton(top_level_window, text='Add product name', command=write_product_name)
    button.pack(side='top', pady=20)


def update_total_price(*args):
    try:
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())

        total = price * quantity
        price_hint_label.configure(text=f"Total Price: {total}$")
    except ValueError:
        price_hint_label.configure(text="Total Price: -")

# -------------------- UI --------------------


app = ctk.CTk()
app.title('Transaction tracker')
app.geometry('530x600')

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill='both', expand=True)

tabview = ctk.CTkTabview(master=main_frame)
tabview.pack(padx=20, pady=20)

tab_insert_information = tabview.add('Insert information')
tab_expense_tracker = tabview.add('Expense tracker')
tab_product_analyse = tabview.add('Product analyse')
tab_customer_analyse = tabview.add('Customer analyse')


# -------------------- Insert information tab --------------------
list_of_product_names = []

with open('list_of_products.txt', 'r') as f:
    for i in f.readlines():
        list_of_product_names.append(i.strip())

explain_label = ctk.CTkLabel(tab_insert_information, text='Insert your info', font=('Arial', 20, 'bold'))
explain_label.pack(side='top', pady=20)

customer_id_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Customer ID', width=300, height=40)
customer_id_entry.pack(side='top', pady=10)

quantity_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Quantity', width=300, height=40)
quantity_entry.pack(side='top', pady=10)
quantity_entry.bind('<KeyRelease>', update_total_price)

price_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Price', width=300, height=40)
price_entry.pack(side='top', pady=10)
price_entry.bind('<KeyRelease>', update_total_price)

# 🔹 لیبل کوچک زیر ورودی قیمت
price_hint_label = ctk.CTkLabel(tab_insert_information, text='Enter price in numbers only', font=('Arial', 10), text_color='gray')
price_hint_label.pack(side='top', anchor='w', padx=60, pady=(0, 10))  # سمت چپ

product_name_combo_box = ctk.CTkComboBox(tab_insert_information, width=300, height=40, values=list_of_product_names)
product_name_combo_box.pack(side='top', pady=10)

date_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Date', width=300, height=40)
date_entry.insert(0, 'day/month/year')
date_entry.pack(side='top', pady=10)

# 🔹 فریم برای دکمه‌ها
button_frame = ctk.CTkFrame(tab_insert_information, fg_color="transparent")
button_frame.pack(side='top', pady=20)

add_product_name_button = ctk.CTkButton(button_frame, text='Add a product', command=top_level)
add_product_name_button.pack(side='left', padx=10)

add_button = ctk.CTkButton(button_frame, text='Add in file', command=write_new_information)
add_button.pack(side='left', padx=10)

# -------------------- Expense tracker tab --------------------

explain_label_expense = ctk.CTkLabel(tab_expense_tracker, text='See the information', font=('Arial', 20, 'bold')).pack(side='top', pady=20)

combobox_expense_tracker = ctk.CTkComboBox(tab_expense_tracker, values=['Normal','Date', 'Price', 'Quantity'], command=change_order)
combobox_expense_tracker.pack(side='top', pady=(0, 20))
combobox_expense_tracker.set('Normal')

checkbox = ctk.CTkCheckBox(tab_expense_tracker, text="Reverse", command=checkbox_event)
checkbox.pack(side='top', pady=(0, 10))

expense_tracker_list_box = ctk.CTkTextbox(tab_expense_tracker, width=800, height=500, font=('Courier', 14))
expense_tracker_list_box.pack(side='top', pady=(0, 20))

expense_tracker_list_box.insert('0.0', 'Info will appear here...')

expense_tracker()


# -------------------- Product analyse tab --------------------

explain_label_analyse = ctk.CTkLabel(tab_product_analyse, text='See the analyse', font=('Arial', 20, 'bold')).pack(side='top', pady=20)

product_analyse_list_box = ctk.CTkTextbox(tab_product_analyse, width=800, height=250, font=('Courier', 14))
product_analyse_list_box.pack(side='top', pady=(0, 20))

product_analyse_list_box.insert('0.0', 'Info will appear here...')

product_analyse_list_box2 = ctk.CTkTextbox(tab_product_analyse, width=800, height=250, font=('Courier', 14))
product_analyse_list_box2.pack(side='top', pady=(0, 20))

product_analyse()

if __name__ == "__main__":
    app.mainloop()