from Mysqlconnect import cursor, db

# SQL query to create the registration table
create_table_query = """
CREATE TABLE Kiosk_Food (
    kiosk_id INT AUTO_INCREMENT PRIMARY KEY,
    ration_id VARCHAR(255),
    FOREIGN KEY (ration_id) REFERENCES Customer(ration_id),
    rice VARCHAR(255) NOT NULL,
    wheat VARCHAR(255) NOT NULL,
    sugar VARCHAR(255) NOT NULL,
    dal VARCHAR(255) NOT NULL
)
"""

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()

