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


import mysql.connector
engine = mysql.connector.connect(host="localhost", user="root", password="yash@7940", database="apna")
cur = engine.cursor()
if engine.is_connected():
    print("Succesful") #Output:succesful
else:
    print("Unsucessful")
d1 = pd.read_sql_query("SELECT * FROM user", engine)
print(d1)

# data = pd.read_sql("C:\Users\nitin\Documents\MySQL Projects\BYJUS.sql")
# d = pd.DataFrame(data)
# print(d)