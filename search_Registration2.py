import tkinter as tk
from tkinter import scrolledtext, messagebox
from Mysqlconnect import cursor
from tabulate import tabulate

def search_registration_data(family_textbox,food_textbox,search_query):
    # Clear the existing data in the textbox
    family_textbox.delete("1.0", "end")
    food_textbox.delete("1.0", "end")
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
        family_rows = []
        food_rows = []

        for data in registration_data:
            family_Details = f"First Name: {data[1]}\nLast Name: {data[2]}\nAge: {data[3]}\nAadhaar Number: {data[4]}\nRation ID: {data[5]}\nFamily Count: {data[6]}"
            food_Details = f"Rice: {data[9]} kg\nWheat: {data[10]} kg\nSugar: {data[11]} kg\nDal: {data[10]} kg\n"
            family_rows.append([family_Details])
            food_rows.append([food_Details])

        # Convert the data to a formatted table
        family_headers = ["Family Details"]
        food_headers = ["Food Details"]

        family_table = tabulate(family_rows, family_headers, tablefmt="plain", stralign="left")
        food_table = tabulate(food_rows, food_headers, tablefmt="plain", stralign="left")

        # Insert the tables into separate textboxes or display sections
        family_textbox.insert(tk.END, family_table)
        food_textbox.insert(tk.END, food_table)

    else:
        messagebox.showwarning("Error", "No registration data found.")
