#Function 
def your_name(name):
    print("Your Name is : ", name)

your_name("Yash") #Output: "Your name is : Yash"



#Positional Argument
def addition(a, b):
    return a + b

sum = addition(7, 2)
print(sum) #Output: 9



#Keyword Argument
def area_of_rectangle(l, b):
    return l * b

rectangle = area_of_rectangle(l=12, b=6)
print(rectangle)



#Lambda Function
multiply = lambda a, b: a * b

result = multiply(9, 12)
print(result) #Output: 108