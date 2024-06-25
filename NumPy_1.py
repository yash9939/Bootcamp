# Importing numpy library
import numpy as np

# Displaying the version of numpy library
print(np.__version__)

# Numpy Array and Attributes
# shape Attributes
# 1-Dimensional Array
cars1 = np.array(["BMW", "Mercedes", "TATA", "Bugatti", "Ferarri"])
print(cars1) #Output: ['BMW' 'Mercedes' 'TATA' 'Bugatti' 'Ferarri']
print(cars1.shape) #Output: (5,)

# 2-Dimensional Array
cars2 = np.array([["BMW"], ["Mercedes"]])
print(cars2) #Output: [['BMW']
#                        ['Mercedes']]
print(cars2.shape) #Output: (2, 1)

# 3-Dimensional Array
cars3 = np.array([[["BMW"]], [["Mercedes"]], [["TATA"]]])
print(cars3) #Output:[['BMW']]
#                    [['Mercedes']]
#                    [['TATA']]]
print(cars3.shape) #Output: (3, 1, 1)

# size Attributes
print(cars1.size) #Output: 5

# dtype Attribute
num = np.array([1,2,3,4])
print(num.dtype) #Output: int64

alpha = np.array(["A", "B", "C"])
print(alpha.dtype) #Output: <U1

complex = np.array([1+2j, 6+4j])
print(complex.dtype) # Output: complex128

bool = np.array([True, False])
print(bool.dtype) #Output: bool

num2 = np.array([10, 20, 30, 40], dtype=np.int64)
print(num2) #Output: [10 20 30 40]
print(num.dtype) #Output: int64

#alpha2 = np.array(["x", "y", "z"], dtype=np.int64)
#print(alpha2) # Output: ValueError: invalid literal for int() with base 10: 'x'
#print(alpha2.dtype) #Output: ValueError: invalid literal for int() with base 10: 'x'


# NumPy Functions
# numpy.array() Function
# From List
athelet = np.array(["V18", "MSD7", "CR7"])
print(athelet) #Output: ['V18' 'MSD7' 'CR7']

# From tuple
fruits = np.array(("Apple", "Banana", "Grapes"))
print(fruits) #output: ['Apple' 'Banana' 'Grapes']

# numpy.asarray Function
a = [3, 6, 9, 12]
b = np.asarray(a)
print(b) #Output: [ 3  6  9 12]

heros = ("Batman", "Superman", "Flash")
hero = np.asarray(heros)
print(hero) #Ouput: ['Batman' 'Superman' 'Flash']

# numpy.ones Function
one = np.ones(8)
print(one) #Output: [1. 1. 1. 1. 1. 1. 1. 1.]

two = np.ones((2,2))
print(two) #Output: [[1. 1.]
#                    [1. 1.]]

# numpy.empty Function
l = np.empty(3)
print(l) #Output: [2.05833592e-312 2.31297541e-312 2.33419537e-312]

m = np.empty((2,4))
print(m) #Output: [[1. 1. 1. 1.]
#                  [1. 1. 1. 1.]]

# numpy.arange Function
p = np.arange(7)
print(p) #Output: [0 1 2 3 4 5 6]

q = np.arange(3, 18, 3)
print(q) #Output: [ 3  6  9 12 15]

# numpy.eye Function
sq1 = np.eye(2)
print(sq1) #Output: [[0. 1.]
#                   [1. 0.]]

sq2 = np.eye(3)
print(sq2) #Output: [[1. 0. 0.]
#                    [0. 1. 0.]
#                    [0. 0. 1.]]


# Operations in NumPy

n1 = np.array([1, 2, 3])
n2 = np.array([2, 4, 6])
# Adddition Operation
sum = n1 + n2
print(sum) #Output:  [3 6 9]

#Subtration Operation
diff = n1 - n2
print(diff) #Output: [1 2 3]

# Multiplication Operation
product = n1 * n2
print(product) #Output: [ 2  8 18]

# Division Operation
div = n2 / n1
print(div) #Output: [2. 2. 2.]

# Scalar Operation
sc1 = n1 * 3
sc2 = n2 / 2
print(sc1) #Output: [3 6 9]
print(sc2) #Output: [1. 2. 3.]
