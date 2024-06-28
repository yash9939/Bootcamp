# Importing the matplotlib that I installed
import matplotlib as mpt

# Importing the pylot attribute(Library) from matplotlib
import matplotlib.pyplot as plt

# Importing every other features(functions, methods and etc.) of marplotlib library
from matplotlib import *

# Pie Chart

plt.title("Top Goal Scorer's") #Provinding the title
foot = ["Cristiano", "Messi", "Chhetri", "Neymar"] #Label
goals = [895, 835, 273, 476] #X values
exp = [0, 0, 0, 0] #Explode
colors = ["Red", "Lightblue", "Blue", "Yellow"] #Colors for pie
pc = plt.pie(goals, labels=foot, colors=colors, explode=exp, shadow=True, autopct="%1.0f%%", wedgeprops={"edgecolor":"Orange", "linewidth":4})
plt.show(pc) #Displaying the pie on the basis of above information

# Line Chart

# Line graph for x**2 Graph
import numpy as np 
plt.title("x^2 Graph")
x=np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]) #x-coordinate
y=x**2   #y-coordinate
plt.xlabel("x-axis") #to set the label of x axis
plt.ylabel("y-axis") #to set the label of y axis
lc = plt.plot(x,y) #plotting the graph with the provided inputs
plt.show(lc) #displying the graph

# Multi-Line graph
plt.title("Multi-Line Graph")
# Graph-I
x1 = np.array([1, 2, 3, 4, 5]) #x-coordinates for Graph-I
y1 = x1**2 #y-coordinates for Graph-I
plt.plot(x1, y1, label="Graph-I", linestyle="--", marker="s") #plotting the  Graph-I

# Graph-II
x2 = np.array([2, 4, 6, 8, 10]) #x-coordinates for Graph-II
y2 = np.array([1, 3, 5, 7, 9]) #y-coordinates for Graph-II
plt.plot(x2, y2, label="Graph-II", linestyle=":", marker=">") #plotting the Graph-II

plt.xlabel("x-axis") #to set the label of x axis
plt.ylabel("y-axis") #to set the label of y axis
plt.legend() #Calling the legend function
plt.grid(True)
plt.show() #displying the graph

# Subplots
plt.subplot(3,3,3)
plt.plot(x1,y1,"y")

plt.subplot(3,3,3)
plt.plot(x2,y2,"b")

plt.show()


# Bar Chart
plt.title("Number of Cars in each Country")
car_comp = ["USA", "UK", "China", "Germany", "France", "Italy", "Japan"]
cars = [231, 157, 124, 114, 72, 61, 24]
bc = plt.bar(car_comp, cars, color="blue", label="no. of cars")
plt.xlabel("Car Company's")
plt.ylabel("Number of Cars")
plt.legend()
plt.grid(True)
plt.show(bc)

# Bar Chart with Line graph

plt.title("Bar Graph with Line Graph")

# Line Graph-I
a1 = np.array([1, 2, 3, 4, 5]) #x-coordinates for Graph-I
b1 = np.array([2, 4, 6, 8, 10]) #y-coordinates for Graph-I
plt.plot(a1, b1, color="yellow", label="Graph-I", linestyle="--", marker="s") #plotting the  Graph-I

# Line Graph-II
b2 = np.array([1, 3, 5, 7, 9]) #y-coordinates for Graph-II
plt.plot(a1, b2, color="red", label="Graph-II", linestyle=":", marker="o") #plotting the Graph-II

# Bar Chart
b3 = np.array([1, 2, 3, 5, 7]) #y-coordinates for Graph-III
plt.bar(a1, b3, color="blue", label="Graph-III") #plotting the Graph-III

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Multi Bar Chart

plt.title("Multi Bar Chart")

x_indexes = np.arange(len(a1))  # numpy array with range from (0,m)
width = 0.25

plt.bar(x_indexes-width, b1, color="Blue", label="Bar Char-I")

plt.bar(x_indexes, b2, color="Black", label="Bar Chart-II")

plt.bar(x_indexes+width, b3, color="Red", label="Bar Char-III")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xticks(ticks=x_indexes, labels=a1)
plt.legend()
plt.grid(True)
plt.show()


# Scatter Plot
plt.title("Scatter plot")

# Graph-I
x1 = np.array([1, 2, 3, 4, 5]) #x-coordinates for Graph-I
y1 = x1**2 #y-coordinates for Graph-I
plt.scatter(x1, y1, color="Blue", marker="s", edgecolors="black")

x2 = np.array([2, 4, 6, 8, 10]) #x-coordinates for Graph-II
y2 = np.array([1, 3, 5, 7, 9]) #y-coordinates for Graph-II
plt.scatter(x2, y2, color="Red", marker="o", edgecolors="black")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(["Graph-I", "Graph-II"], loc="upper right")
plt.grid(True)
plt.show()