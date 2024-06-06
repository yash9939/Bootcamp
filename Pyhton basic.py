#Input and Output
your_name = input("Enter your name : ") #Input: "Yash Bhardwaj" 
your_age = int(input("Enter your age : ")) #Input: "20"

print("Hello, My name is ", +your_name+ " My age is ", +your_age) #Output: "Hello, My name is Yash Bhardwaj ! My 


#Operators
a = 20
b = 9
#Arithmatic Operators
print(a + b) #Output: 29
print(a - b) #Output: 11
print(a * b) #Ouput: 180
print(a / b) #Output: 2.2222...(Float value)
print(a // b) #Output: 2(floor int value)
print(a % b) #Output: 2 (gives remainder)
print(a ** b) #Ouput: 512000000000 (exponential)

#Comparison Operator
print(a == b) #Output: False
print(a != b) #Output: True
print(a > b) #Ouput: True
print(a < b) #Output: False
print(a >= b) #Output: True
print(a <= b) #Output: False

#Logical Operators
print(a > 5 and b > 5) #Outout: True
print(a > 10 or b > 10) #Output: False
print(not(a > 5 and b > 5)) #Output: False


#Type Casting
# Type Casting
int_from_float = int(7.32)
float_from_int = float(89)
string_from_int = str(100)
list_from_string = list("Yash")
tuple_from_list = tuple([2, 5, 3, 8, 5])
set_from_list = set([3, 2, 3, 4, 9])

print(int_from_float) #Output: 7
print(float_from_int) #Output: 89.00
print(string_from_int) #Output: "10"
print(list_from_string) #Output: ["Y", "a", "s", "h"]
print(tuple_from_list) #Output: (2, 5, 3, 8, 5)
print(set_from_list) #Output: {3, 2, 4, 9}


# Conditional Statements
age = 10

if age >= 18:
    print("He is Adult")
elif 12 <= age < 18:
    print("He is a Teenager")
else:
    print("He is a kid")



# Looping Statements
# For loop
cars = ["Mercedes", "BMW", "Audi"]
for car in cars:
    print(car)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1




# Special Functions
carss = ["Mercedes", "BMW", "Audi"]

# len()
print(len(cars))  # Output: 3

# id()
print(id(cars))  # Output: Unique ID of the list object

# type()
print(type(cars))  # Output: <class 'list'>

# range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4