from tkinter import messagebox
from Mysqlconnect import cursor, db
from date import formatted_date


def save_transaction_data(ration_id, month, year, rice, dal, sugar, salt, oil, peas):
    sql = "SELECT month,year,time FROM transaction WHERE ration_id = %s"

    # Execute the SQL query
    cursor.execute(sql, (ration_id,))

    # Fetch all rows from the result set
    results = cursor.fetchall()
    if results:
        monthe, yeare, timee = results
    else:
        monthe = "default"
        yeare = 000
        timee = 00

    if ration_id and month and year and (rice or dal or sugar or salt or oil or peas):
        if month == monthe and year == yeare:
            messagebox.showwarning("Error", "This Ration_id has already taken this month on" + timee)
        else:
            sql1 = "INSERT INTO transaction (ration_id,month,year,rice,dal,sugar,salt,oil,peas,time) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (ration_id, month, year, rice, dal, sugar, salt, oil, peas, formatted_date)

            cursor.execute(sql1, values)
            db.commit()

            messagebox.showinfo("Success", "Transaction data saved successfully.")
            return True
    else:
        messagebox.showwarning("Error", "Please enter ration_id and month and year and any of the food item.")
        return False