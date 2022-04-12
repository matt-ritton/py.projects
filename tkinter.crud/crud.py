from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")

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
# Functions ----------------------------------------------------------------#

# Submit function for our database
def submit():
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :ad, :city, :state, :zip)",
                   # Python Dictionary to make a key-value pair for our key values above
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'ad': ad.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zip': zip.get()
                   })

    conn.commit()
    conn.close()

    # Clear the Input Fields
    f_name.delete(0, END)
    l_name.delete(0, END)
    ad.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)


# Query function to return all records in database
def query():
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute('SELECT *,oid FROM addresses')
    records = cursor.fetchall()

    format_records = ''

    for record in records:
        format_records += (record[0] + ' ' + record[1] + ' - '
                           + record[2] + ', ' + record[3] + ' - '
                           + record[4] + ', ' + str(record[5]) + '\n')

    query_label = Label(root, text=format_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()

# --------------------------------------------------------------------------#
# Label Widgets for Input Fields--------------------------------------------#

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

ad_label = Label(root, text="Address")
ad_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zip_label = Label(root, text="Zip Code")
zip_label.grid(row=5, column=0)

# --------------------------------------------------------------------------#
# Input Fields (Entry Widget)-----------------------------------------------#

# First Name field
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

# Last Name field
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

# Address field
ad = Entry(root, width=30)
ad.grid(row=2, column=1, padx=20)

# City field
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

# State field
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

# Zip Code field
zip = Entry(root, width=30)
zip.grid(row=5, column=1, padx=20)

# --------------------------------------------------------------------------#
# Button Widgets------------------------------------------------------------#

# Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Query Button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# --------------------------------------------------------------------------#

# Commit changes
conn.commit()

# Close connection
conn.close()

# --------------------------------------------------------------------------#

root.mainloop()
