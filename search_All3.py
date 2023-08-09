import tkinter as tk
from tkinter import scrolledtext, messagebox
from Mysqlconnect import cursor
from tabulate import tabulate

def search_all_data(family_textbox,food_textbox,transaction_textbox, search_query):
    # Clear the existing data in the textbox
    family_textbox.delete("1.0", "end")
    food_textbox.delete("1.0", "end")
    transaction_textbox.delete("1.0", "end")
    # SQL query to retrieve data from multiple tables based on the ration_id
    # sql = """
    # SELECT registration2.*, food.*, transaction.*
    # FROM registration2
    # JOIN food ON registration2.ration_id = food.ration_id
    # JOIN transaction ON registration2.ration_id = transaction.ration_id
    # WHERE registration2.ration_id = %s
    # """

    sql = """
    SELECT registration2.*, food.*
    FROM registration2
    JOIN food ON registration2.ration_id = food.ration_id
    WHERE registration2.ration_id = %s
    """
    sql1 = """
    SELECT *
    FROM transaction
    WHERE ration_id = %s
    ORDER BY id DESC
    """


    # Execute the SQL query
    cursor.execute(sql, (search_query,))
    
    # Fetch all rows from the result set
    registration_data = cursor.fetchall()
    cursor.execute(sql1, (search_query,))
    registration_data2 = cursor.fetchall()

    if registration_data2:
        transaction_rows = []
        for data in registration_data2:
            transaction_Details = f"\nMonth: {data[2]}\nYear: {data[3]}\nRice: {data[4]} kg\nWheat: {data[5]}\nSugar: {data[6]} kg\nDal: {data[5]}\nTime: {data[10]}\n\n"
            transaction_rows.append([transaction_Details])
            transaction_rows.append(["----------------------------------------------------------------"])            
    else:
        transaction_rows = []
        transaction_Details=f"---No Transaction Made till Now---"
        transaction_rows.append([transaction_Details])



    if registration_data:
        # Initialize the data for each section
        family_rows = []
        food_rows = []
        # transaction_rows = []

        for data in registration_data:
            family_Details = f"First Name: {data[1]}\nLast Name: {data[2]}\nAge: {data[3]}\nAadhaar Number: {data[4]}\nRation ID: {data[5]}\nFamily Count: {data[6]}"
            food_Details = f"Rice: {data[9]} kg\nWheat: {data[10]} kg\nSugar: {data[11]} kg\nDal: {data[10]} kg\n"
            # transaction_Details = f"Month: {data[13]}\nYear: {data[14]}\nRice: {data[15]}\nDal: {data[16]}\nSugar: {data[17]}\nSalt: {data[18]}\nOil: {data[19]}\nPeas: {data[20]}\nTime: {data[21]}\n"

            # Append the data to the respective section
            family_rows.append([family_Details])
            food_rows.append([food_Details])
        # transaction_rows.append([transaction_Details])

        # Format the headers for each section
        family_headers = ["---Family Details---"]
        food_headers = ["---Food Details---"]
        transaction_headers = ["---Transaction Details---"]

        # Convert the data to formatted tables
        family_table = tabulate(family_rows, family_headers, tablefmt="plain", stralign="left")
        food_table = tabulate(food_rows, food_headers, tablefmt="plain", stralign="left")
        transaction_table = tabulate(transaction_rows, transaction_headers, tablefmt="plain", stralign="left")

        # Insert the tables into separate textboxes or display sections
        family_textbox.insert(tk.END, family_table)
        food_textbox.insert(tk.END, food_table)
        transaction_textbox.insert(tk.END, transaction_table)
    else:
        messagebox.showwarning("Error", "No registration data found.")
