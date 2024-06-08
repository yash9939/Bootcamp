#Single Exception Handling
try:
    num = int(input("Enter your number : "))

    print("The number you have selected is : ", num)

except ValueError:
    print("Invalid Error")



#Multiple Exception Handling
try:
    a = "Yash"
    b = 6

    def add(a, b):
        print(c)
    return a + b

except SyntaxError:
    print("Syntax Error occured")

except TypeError:
    print("Type Error occured")

except IndentationError:
    print("Indentation Error occured")



