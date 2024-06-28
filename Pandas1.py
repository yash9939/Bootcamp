# Importing the newly installed pandas library
import pandas as pd

# Checking if the pandas library is installed or not
print("Library imported") #Output: Library imported
print("With Version : ", pd.__version__) #Output: With Version :  2.2.2

# Creating Series

# From List
a1 = [1, 2, 3, 4, 5]
s_from_l = pd.Series(a1, index=["l", "m", "n", "o", "p"])
print("Series from List : ")
print(s_from_l) #Output: Series from List : 
#                        l    1
#                        m    2
#                        n    3
#                        o    4
#                        p    5
#                        dtype: int64

# From Array
# Importing numpy library
import numpy as np
a2 = np.array([1.1, 2.2, 3.3, 4.4])
s_from_a = pd.Series(a2, index=["w", "x", "y", "z"])
print("Series from Array : ")
print(s_from_a) #Output: Series from Array : 
#                        w    1.1
#                        x    2.2
#                        y    3.3
#                        z    4.4
#                        dtype: float64

# From Dictionary
a3 = {"Cristiano Ronaldo": 130, "Lionel Messi": 108, "Sunil Chhetri": 94, "Neymar Jr.": 79}
s_from_d = pd.Series(a3)
print("Series from Dictionary : ")
print(s_from_d) #Output: Series from Dictionary : 
#                        Cristiano Ronaldo    130
#                        Lionel Messi         108
#                        Sunil Chhetri         94
#                        Neymar Jr.            79
#                        dtype: int64

# Pandas Dataframe

# Importing the mysql connector
import mysql.connector

# Definig and establishing a object to the preferd database
engine = mysql.connector.connect(host="localhost", user="root", password="yash@7940", database="apna")

# Checking if the database is connected or not
if engine.is_connected():
    print("Succesful") #Output:succesful
else:
    print("Unsucessful")

#initialising the cursor
cur = engine.cursor()

# Reading and decoding queries to display the table data
d1 = pd.read_sql_query("SELECT * FROM user", engine)

# Initialising the data frame
d2 = pd.DataFrame(d1)
print(d2)

# Dataframe from Dictionary
foot = {"Footballer_ID": ["F-101", "F-102", "F-103", "F-104", "F-105", "F-106", "F-107"],
        "Name": ["Cristiano Ronaldo", "Sunil Chhetri", "Lionel Messi", "Neymar Jr.", "Kevin De Bryune", "Mesut Ozil", "Sergio Ramos"],
        "Age": [39, 39, 37, 32, 32, 35, 38],
        "Goals_Scored": [895, 273, 835, 476, 137, 114, 117],
        "Club": ["Al-Nassr FC", "Bengaluru FC", "Inter- Miami", "Al Hilal", "Manchester City FC", "Fenerbehce FC", "Sevilla FC"],
        "Country": ["Portugal", "India", "Argentina", "Brazil", "Belgium", "Germany", "Spain"]}

d3 = pd.DataFrame(foot, index=[1, 2, 3, 4, 5, 6, 7])
print(d3)