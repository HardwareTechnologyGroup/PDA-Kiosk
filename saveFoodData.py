from tkinter import messagebox
from Mysqlconnect import cursor, db

def save_food_data(ration_id,family_count):
    if family_count and ration_id:
        sql="INSERT INTO food (ration_id,Rice,Wheat,Sugar,Dal) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        Rice=5 #5kg/p, 
        Wheat=2 #2kg/p, 
        Sugar=1 #1kg/p, 
        Dal=2 #2kg/p, 
#         oil=1 #1L/p, 
#         peas=1 #1kg/p
        values = (ration_id,Rice*int(family_count),Wheat*int(family_count),Sugar*int(family_count),Dal*int(family_count))

        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Food data saved successfully.")
        return True
    else:
        messagebox.showwarning("Error", "Please enter both ration Id and Family Count.")
        return False        
