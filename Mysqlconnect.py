import mysql.connector
import os
#from dotenv import load_dotenv

#load_dotenv()
# Establish a connection to your MySQL database
db = mysql.connector.connect(
    # host="localhost",
    # user=os.getenv('USER'),
    # # user="root",
    # password=os.getenv('MYSQL_PASS'),
    # database=os.getenv('DATABASE_NAME')
    # # password="bik@Skill#1",
    # # database="database1"
    host = "localhost",
    user = "admin",
    password = "root",
    database = "kioskDataBase"
)
# print(os.getenv('DATABASE_NAME'))

# Create a cursor object to execute SQL queries
cursor = db.cursor()
