from tkinter import messagebox
from Mysqlconnect import cursor, db

def save_registration_data(fname, lname, age, addhar_number,ration_id,family_count):
    cursor = db.cursor()
    sql = "SELECT * FROM registration2 WHERE addhar_number = %s"

    # Execute the SQL query
    cursor.execute(sql, (addhar_number,))

    # Fetch all rows from the result set
    registration_data = cursor.fetchall()
    if registration_data:
        messagebox.showwarning("Error", "Aadhaar Number already registered")
    elif fname and addhar_number:
        sql = "INSERT INTO registration2 (fname,lname,age, addhar_number,ration_id,family_count) VALUES (%s, %s,%s,%s,%s,%s)"
        values = (fname, lname, age, addhar_number,ration_id,family_count)

        cursor.execute(sql, values)
        db.commit()

        messagebox.showinfo("Success", "Registration data saved successfully.")
        return True
    else:
        messagebox.showwarning("Error", "Please enter both name and Aadhaar number.")
        return False
