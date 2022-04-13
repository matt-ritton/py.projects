from tkinter import *
from crud import *
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("360x600")

# --------------------------------------------------------------------------#

# Create or Connect to a Database
conn = sqlite3.connect('./tkinter.crud/address_book.db')

# Create a cursor to execute commands in our database
cursor = conn.cursor()

# --------------------------------------------------------------------------#

# Create table [Execute this only one time!]
'''cursor.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text, 
    zip_code integer)""")'''

# --------------------------------------------------------------------------#
# Label Widgets for Input Fields--------------------------------------------#

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 5))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0, pady=(0, 5))

ad_label = Label(root, text="Address")
ad_label.grid(row=2, column=0, pady=(0, 5))

city_label = Label(root, text="City")
city_label.grid(row=3, column=0, pady=(0, 5))

state_label = Label(root, text="State")
state_label.grid(row=4, column=0, pady=(0, 5))

zip_label = Label(root, text="Zip Code")
zip_label.grid(row=5, column=0, pady=(0, 5))

show_section = Label(root, text="-------------------------- Show Records ---------------------------")
show_section.grid(row=7, column=0, columnspan=2, pady=(10, 5))

del_section = Label(root, text="-------------------------- Delete Records --------------------------")
del_section.grid(row=10, column=0, columnspan=2, pady=(10, 5))

del_label = Label(root, text="Select ID")
del_label.grid(row=11, column=0, pady=(10, 5))

# --------------------------------------------------------------------------#
# Input Fields (Entry Widget)-----------------------------------------------#

# First Name field
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 5))

# Last Name field
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20, pady=(0, 5))

# Address field
ad = Entry(root, width=30)
ad.grid(row=2, column=1, padx=20, pady=(0, 5))

# City field
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20, pady=(0, 5))

# State field
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20, pady=(0, 5))

# Zip Code field
zip = Entry(root, width=30)
zip.grid(row=5, column=1, padx=20, pady=(0, 5))

del_field = Entry(root, width=30)
del_field.grid(row=11, column=1, padx=20, pady=(10, 5))

# --------------------------------------------------------------------------#
# Button Widgets------------------------------------------------------------#

# Submit Button
submit_btn = Button(root, text="Add Record to Database", command=lambda: submit(f_name, l_name, ad, city, state, zip))
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query Button
query_btn = Button(root, text='Show All Records', command=lambda: query(root))
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Delete Button
del_btn = Button(root, text='Delete Record', command=lambda: delete(del_field))
del_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# --------------------------------------------------------------------------#

# Commit changes
conn.commit()

# Close connection
conn.close()

# --------------------------------------------------------------------------#

root.mainloop()
