# Importing the Pandas, Matplotlib and Seaborn Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading and dislplaying a csv file
data = pd.read_csv("D:\Downloads\Practice.csv")
data.head(7)

# Getting Null values
# .isnull function
data.isnull()
data.isnull().sum() #gives sum of null values in a specific column

# .info() function
data.info()

# Handling Null Values

# Constant value + add indicator for Missingness
d1 = data.fillna(value=1)
print(d1)

# pad and bfill method
d2 = data.fillna(method="pad", axis=1)
print(d2)

d3 = data.fillna(method="bfill")
print(d3)

# Filling column wise
d4 = data.fillna({"Role":"Don't Know", "Income":"Don't Know","Manager":"Don't Know"})
print(d4)

# Median Function
d5 = data["Age"].median()
print(d5)

d6 = data["Age"].fillna(value=data["Age"].median())
print(d6)
