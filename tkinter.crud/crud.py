import sqlite3

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
    query_label.grid(row=9, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Delete function for our database
def delete(del_field):
    conn = sqlite3.connect('./tkinter.crud/address_book.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM addresses WHERE oid=" + del_field.get())

    conn.commit()
    conn.close()

