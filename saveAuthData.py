from tkinter import messagebox
from Mysqlconnect import cursor, db

def save_auth_data(ration_id,family_count):
    if family_count and ration_id:
        sql="INSERT INTO AuthData (ration_id, password, kiosk_id) VALUES (%s,%s,%s)"
        
        values = (ration_id,password, kiosk_id)

        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Kiosk data saved successfully.")
        return True
    else:
        messagebox.showwarning("Error", "Please enter both ration Id and Family Count.")
        return False        

