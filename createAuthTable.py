from Mysqlconnect import cursor, db

# SQL query to create the customer authentication table
create_table_query = """
CREATE TABLE AuthData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ration_id VARCHAR(255),
    FOREIGN KEY (ration_id) REFERENCES Customer(ration_id),
    password VARCHAR(255) NOT NULL,
    kiosk_id INT,
    FOREIGN KEY (kiosk_id) REFERENCES Kiosk_Food(kiosk_id)
)
"""

# Execute the create table query
cursor.execute(create_table_query)

data_insert = "INSERT INTO AuthData ("
cursor.execute("INSERT INTO ")

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
