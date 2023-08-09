import tkinter as tk
from tkinter import scrolledtext, messagebox
from Mysqlconnect import cursor

# def search_registration_data(registration_textbox, search_query):
#     # Clear the existing data in the listbox
#     registration_textbox.delete("1.0", "end")

#     # SQL query to retrieve data matching the search query from the registration table
#     sql = "SELECT * FROM registration2 WHERE ration_id = %s"

#     # Execute the SQL query
#     cursor.execute(sql, (search_query))

#     # Fetch all rows from the result set
#     registration_data = cursor.fetchall()

#     if registration_data:
#         # Insert the data into the listbox
#         for data in registration_data:
#             full_data = f"Rice: {data[1]} kg\nDal: {data[2]} kg\nSugar: {data[3]} kg\nSalt: {data[4]} Packet(1kg)\nOil: {data[5]} Litre\nPeas: {data[6]} kg\n"
#             registration_textbox.insert(tk.END, full_data + "\n\n")
#     else:
#         messagebox.showwarning("Error", "No registration data found.")

def search_registration_data(registration_textbox, search_query):
    # Clear the existing data in the textbox
    registration_textbox.delete("1.0", "end")

    # SQL query to retrieve data matching the search query from the registration2 table, joining with the food table
    sql = """
    SELECT registration2.*, food.*
    FROM registration2
    JOIN food ON registration2.ration_id = food.ration_id
    WHERE registration2.ration_id = %s
    """

    # Execute the SQL query
    cursor.execute(sql, (search_query,))

    # Fetch all rows from the result set
    registration_data = cursor.fetchall()

    if registration_data:
        # Insert the data into the textbox
        for data in registration_data:
            full_data = f"Registration2 Table:\nRation ID: {data[0]}\nField 1: {data[1]}\nField 2: {data[2]}\n"
            full_data += f"Food Table:\nRice: {data[3]} kg\nWheat: {data[4]} kg\nSugar: {data[5]} kg\nDal: {data[4]} kg\n"
            registration_textbox.insert(tk.END, full_data + "\n\n")
    else:
        messagebox.showwarning("Error", "No registration data found.")
