import sqlite3
from tkinter import *

# --------------------------------------------------------------------------#
# Functions ----------------------------------------------------------------#

# Submit function for our database
def submit(f_name, l_name, ad, city, state, zip):

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

# Query function to return all records in database
def query(root):
    global query_label
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute('SELECT *,oid FROM addresses')
    records = cursor.fetchall()

    format_records = ''

    for record in records:
        format_records += (str(record[6]) + '. ' + record[0] + ' ' +
                           record[1] + ' - ' + record[2] + ', ' +
                           record[3] + ' - ' + record[4] + ', ' +
                           str(record[5]) + '\n')

    query_label = Label(root, text=format_records)
    query_label.grid(row=10, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Delete function for our database
def delete(select_field):
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM addresses WHERE oid=" + select_field.get())

    conn.commit()
    conn.close()

#Update function for our database

#Save function
def save(oid):
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute("""UPDATE addresses SET
    
                       'first_name' = :f_name,
                       'last_name' = :l_name,
                       'address' = :ad,
                       'city' = :city,
                       'state' = :state,
                       'zip_code' = :zip
                       
                   WHERE oid = :oid""",
                    {
                        'f_name': f_name.get(),
                        'l_name': l_name.get(),
                        'ad': ad.get(),
                        'city': city.get(),
                        'state': state.get(),
                        'zip': zip.get(),
                        'oid': oid
                   })

    conn.commit()
    conn.close()

    editor.destroy()

#Update function
def update(select_field):
    global editor, f_name, l_name, ad, city, state, zip
    editor = Tk()
    editor.title("Edit Record")
    editor.geometry("360x600")

    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM addresses WHERE oid =' + select_field.get())
    records = cursor.fetchall()

    # --------------------------------------------------------------------------#
    # Label Widgets for Input Fields--------------------------------------------#

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 5))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0, pady=(0, 5))

    ad_label = Label(editor, text="Address")
    ad_label.grid(row=2, column=0, pady=(0, 5))

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0, pady=(0, 5))

    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0, pady=(0, 5))

    zip_label = Label(editor, text="Zip Code")
    zip_label.grid(row=5, column=0, pady=(0, 5))

    # --------------------------------------------------------------------------#
    # Input Fields (Entry Widget)-----------------------------------------------#

    # First Name field
    f_name = Entry(editor, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 5))

    # Last Name field
    l_name = Entry(editor, width=30)
    l_name.grid(row=1, column=1, padx=20, pady=(0, 5))

    # Address field
    ad = Entry(editor, width=30)
    ad.grid(row=2, column=1, padx=20, pady=(0, 5))

    # City field
    city = Entry(editor, width=30)
    city.grid(row=3, column=1, padx=20, pady=(0, 5))

    # State field
    state = Entry(editor, width=30)
    state.grid(row=4, column=1, padx=20, pady=(0, 5))

    # Zip Code field
    zip = Entry(editor, width=30)
    zip.grid(row=5, column=1, padx=20, pady=(0, 5))

    # --------------------------------------------------------------------------#
    # Button Widgets------------------------------------------------------------#

    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(1, record[1])
        ad.insert(2, record[2])
        city.insert(3, record[3])
        state.insert(4, record[4])
        zip.insert(5, record[5])

    # Submit Button
    save_btn = Button(editor, text="Save Record", command=lambda: save(select_field.get()))
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=132)

    # --------------------------------------------------------------------------#

    conn.commit()
    conn.close()

    editor.mainloop()



