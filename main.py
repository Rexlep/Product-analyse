import customtkinter as ctk
import csv
import pandas as pd
from CTkMessagebox import CTkMessagebox
from datetime import datetime


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
    product_name = product_name_entry.get()
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

            test = [customer_id_entry, quantity_entry, price_entry, product_name_entry, date_entry]

            for i in test:
                i.delete(0, 'end')

            # Show message when the data has been added
            CTkMessagebox(title="Info", message="The information added")


def expense_tracker():
    # Read the file and change it into data frame
    df = pd.read_csv('products.csv')

    df['total price'] = df['quantity'] * df['price']

    # Delete the old stuf in list box
    expense_tracker_list_box.delete('0.0', 'end')
    # Insert the data frame in list box
    expense_tracker_list_box.insert('0.0', df.to_string())



# -------------------- UI --------------------


app = ctk.CTk()
app.title('Transaction tracker')
app.geometry('800x550')

main_frame = ctk.CTkFrame(app)
main_frame.pack(fill='both', expand=True)

tabview = ctk.CTkTabview(master=main_frame)
tabview.pack(padx=20, pady=20)

tab_insert_information = tabview.add('Insert information')
tab_expense_tracker = tabview.add('Expense tracker')
tab_product_analyse = tabview.add('Product analyse')
tab_customer_analyse = tabview.add('Customer analyse')


# -------------------- Insert information tab --------------------


explain_label = ctk.CTkLabel(tab_insert_information, text='Insert your info', font=('Arial', 20, 'bold')).pack(side='top', pady=20)

customer_id_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Customer ID', width=300, height=40)
customer_id_entry.pack(side='top', pady=20)

quantity_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Quantity', width=300, height=40)
quantity_entry.pack(side='top', pady=(0, 20))

price_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Price', width=300, height=40)
price_entry.pack(side='top', pady=(0, 20))

product_name_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Product name', width=300, height=40)
product_name_entry.pack(side='top', pady=(0, 20))

date_entry = ctk.CTkEntry(tab_insert_information, placeholder_text='Date', width=300, height=40)
date_entry.pack(side='top', pady=(0, 20))

add_button = ctk.CTkButton(tab_insert_information, text='Add', command=write_new_information).pack(side='top', pady=(0, 20))


# -------------------- Expense tracker tab --------------------

explain_label_expense = ctk.CTkLabel(tab_expense_tracker, text='See the information', font=('Arial', 20, 'bold')).pack(side='top', pady=20)

expense_tracker_list_box = ctk.CTkTextbox(tab_expense_tracker, width=800, height=500, font=('Courier', 14))
expense_tracker_list_box.pack(side='top', pady=(0, 20))

expense_tracker_list_box.insert('0.0', 'Info will appear here...')

expense_tracker()


if __name__ == "__main__":
    app.mainloop()