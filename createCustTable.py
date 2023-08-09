from Mysqlconnect import cursor, db

# SQL query to create the registration table
create_table_query = """
CREATE TABLE Customer (
    ration_id VARCHAR(255) PRIMARY KEY,
    cust_name VARCHAR(255) NOT NULL,
    aadhar_no VARCHAR(255) NOT NULL,
    age VARCHAR(255) NOT NULL,
    family_count VARCHAR(255) NOT NULL   
)
"""

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()
