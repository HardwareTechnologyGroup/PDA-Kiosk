from tkinter import messagebox
from Mysqlconnect import cursor, db

def save_transaction_data(ration_id,family_count):
    if family_count and ration_id:
        sql="INSERT INTO Transaction (kiosk_id, ration_id, rice, wheat, sugar, dal, withdrawl_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        rice=5 #5kg/p,
        wheat=2 #2kg/p,
        sugar=1 #1kg/p,
        dal=2 #2kg/p,

        values = (ration_id, rice*int(family_count), wheat*int(family_count), sugar*int(family_count), dal*int(family_count), now())

        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Ration transaction data saved successfully.")
        return True
    else:
        messagebox.showwarning("Error", "Please enter both ration Id and Family Count.")
        return False