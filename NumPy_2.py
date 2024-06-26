# NumPY continued From NumPy_1.py

# Importing Numpy library
import numpy as np

# NumPY Broadcasting 
n1 = np.array([1, 2, 3])
n2 = np.array([2, 4, 6])

# 1D Array abd scalar
sc1 = n1 + 8
sc2 = n2 + 28
print(sc1) #Output: [ 9 10 11]
print(sc2) #Output: [30 32 34]

# 2D and 1D Array
n3 = np.array([[4, 8, 12], [5, 10, 15]])
n4 = np.array([8, 9])
sc3 = n3 + n2
sc4 = n1 + n3
sc5 = n4 + n3
sc6 = n4 + n1
print(sc3) #Output: [[ 6 12 18]
#                    [ 7 14 21]]
print(sc4) #Output: [[ 5 10 15]
#                    [ 6 12 18]]
print(sc5) #Output: ValueError: operands could not be broadcast together with shapes (2,) (2,3)
print(sc6) #Output: ValueError: operands could not be broadcast together with shapes (2,) (3,)

# Importing time library
import time

# Create large arrays
a1 = np.random.rand(10000000)
b1 = np.random.rand(10000000)

# Element-wise operations in NumPy
start = time.time()
c1 = a1 + b1
end = time.time()
print(f"NumPy element-wise addition took: {end - start:.6f} seconds") #Output: NumPy element-wise addition took: 0.019819 seconds

# CReating List
a2 = [i for i in range(10000000)]
b2 = [i for i in range(10000000)]

# Element-wise operations in numpy
start = time.time()
c2 = a2 + b2
end = time.time()
print(f"List element-wise addition took: {end - start:.6f} seconds") #Output: List element-wise addition took: 0.099323 seconds

# Indexing and Slicing in NumPy

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([[1,4], [9, 16], [25, 36]])

# Indexing
# Basic Indexing
print(x[2]) #Output: 3
print(y[1, 1]) #Output: 16

# Fancy Indexing
indices = np.array([0, 2, 4])
rows = np.array([1, 0])
cols = np.array([1, 1])
print(x[indices]) #Output: [1 3 5]
print(y[rows, cols]) #Output: [16  4]

# Boolean Indexing
print(x[x>6]) #Output: []
print(y[y>1]) #Output: [ 4  9 16 25 36]

# Slicing
print(x[2:7]) #Output: [3 4 5 6]
print(y[0:1, 0:1]) #Output: [[1]]
print(y[:, 1]) #Output: [ 4 16 36]
print(x[::2]) #Output: [1 3 5]
print(y[::2, ::2]) #Output: [[ 1]
#                            [25]]

# Array Manipulation
p = np.array([2, 4, 6, 8, 10, 12])
q= np.array([[4, 8, 12], [5, 10, 15]])

# Reshaping Arrays
p1 = p.reshape(3,2)
print(p1) #Output: [[ 2  4]
#                   [ 6  8]
#                   [10 12]]

# Flatenning Array
q1 = q.ravel()
print(q1) #Output: [ 4  8 12  5 10 15]

# Stacking and Splitting of Arrays

n1 = np.array([1, 2, 3])
n2 = np.array([2, 4, 6])

# .stack()
e = np.stack((n1, n2))
print(e) #Output: [[1 2 3]
#                  [2 4 6]]

# .hstack()
f = np.hstack((n1, n2))
print(f) #Output: [1 2 3 2 4 6]

# .vstack()
g = np.vstack((n1, n2))
print(g) #Output: [[1 2 3]
#                  [2 4 6]]

w = np.array([[2, 4, 6], [8, 10, 12], [1, 3, 5], [7, 9, 11]])

z = np.split(w, 2)
print(z) #Output: [array([[ 2,  4,  6],
#                         [ 8, 10, 12]]),
#                  array([[ 1,  3,  5],
#                          [ 7,  9, 11]])]

# Methods for adding and removing

cars1 = np.array(["BMW", "Mercedes", "Ferarri", "Bugatti"])
cars2 = np.array([["BMW", "Mercedes"], ["Bugatti", "McLaren"]])

# Append Method
c1 = np.append(cars1, ["Tata", "Toyota"])
c2 = np.append(cars2, [["Tata", "Toyota"]], axis=0)
print(c1) #Output: ['BMW' 'Mercedes' 'Ferarri' 'Bugatti' 'Tata' 'Toyota']
print(c2) #Output: [['BMW' 'Mercedes']
#                   ['Bugatti' 'McLaren']
#                   ['Tata' 'Toyota']]

# Insert Method
c3 = np.insert(cars1, 3, ["Tata", "Toyota"])
c4 = np.insert(cars2, 1, ["Tata", "Toyota"], axis=1)
print(c3) #Output: ['BMW' 'Mercedes' 'Ferarri' 'Tata' 'Toyota' 'Bugatti']
print(c4) #Output:[['BMW' 'Tata' 'Mercedes']
#                  ['Bugatti' 'Toyota' 'McLaren']]

# Delete Method
c5 = np.delete(cars1,"Ferarri")
c6 = np.delete(cars2, ["Mercedes"], axis=1)
print(c5) #Output: IndexError: arrays used as indices must be of integer (or boolean) type
print(c6) #Output: IndexError: arrays used as indices must be of integer (or boolean) type