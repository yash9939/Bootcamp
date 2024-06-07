#Creating Class
class Class:
    pass

object = Class()



#Special Methods
class Cars:
    #__init__ method (Constructor)
    def __init__(self, company, color):
        self.company = company
        self.color = color
    
    #__str__ method
    def __str__(self):
        return f"Your Car company is {self.company} with color {self.color}"
    
    #Deconstructor
    def __del__(self):
        print("The Car company is deleted !")
car1 = Cars("BMW", "Blue")
car2 = Cars("Mercedes", "Black")
print(car1) #Output: "Your Car company is BMW with color Blue"
print(car2) #Output: "Your Car company is Mercedes with color Black"
del car2 #Output: "The car company is deleted !"



class ArithmaticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 // self.num2
    
operations = ArithmaticOperations(12, 6)
print(operations.addition()) #Output: 18
print(operations.subtraction()) #Output: 6
print(operations.multiplication()) #Output: 72
print(operations.division()) #Output: 2