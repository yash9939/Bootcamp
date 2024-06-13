#Importing MySQL through Connector
import mysql.connector

#Importing everything else (like- connect, execute, etc...) from Connector
from mysql.connector import *

#Defining an object for MySQL
mydb = mysql.connector.connect(host="localhost", user="root", password="********", database="byjus")

#Printing if connection is succesfully established
if mydb.is_connected():
    print("Connection Succesfuly established")
else:
    print("Connection is not established")

#Initialising a Cursor-> It is the object that entirely communicates with the entire MySQL server
mycursor = mydb.cursor()

#Executing an my MySQL statement (Showing all tables)
mycursor.execute("SHOW TABLES")

#Printing all the tables in the database - byjus
for tb in mycursor:
    print(tb)