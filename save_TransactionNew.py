from tkinter import messagebox
from Mysqlconnect import cursor, db
from date import formatted_date
def save_transaction_data(ration_id,month,year,Rice,Wheat,Sugar,Dal):
    
    sql = "SELECT * FROM transaction WHERE ration_id = %s"

    # Execute the SQL query
    cursor.execute(sql, (ration_id,))

    # Fetch all rows from the result set
    results = cursor.fetchall()
    # if results:
    #     for data in results:
    #         if(data[2]==month and data[3]==year):
    #             timee=data[10]
    #             messagebox.showwarning("Error", "This Ration_id has already taken this month on"+ timee)
    Not_taken = True
    if ration_id and month and year and (Rice or Wheat or Sugar or Dal):
        for data in results:
            if(data[2]==month and data[3]==year):
                timee=data[10]
                messagebox.showwarning("Error", "This Ration_id has already taken this month on"+ timee)
                Not_taken=False
        # if month==monthe and year==yeare:
        #     messagebox.showwarning("Error", "This Ration_id has already taken this month on"+ timee)
        if(Not_taken):
            sql1 = "INSERT INTO transaction (ration_id,month,year,Rice,Wheat,Sugar,Dal,time) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (ration_id,month,year,Rice,Wheat,Sugar,Dal,formatted_date)

            cursor.execute(sql1, values)
            db.commit()

            messagebox.showinfo("Success", "Transaction data saved successfully.")
            return True
    else:
        messagebox.showwarning("Error", "Please enter ration_id and month and year and any of the food item.")
        return False