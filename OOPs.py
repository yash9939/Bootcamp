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



#Method overloading
class Calculator:
    def add(self, x=None, y=None):
        if x is None and y is None:
            print("Please provide numbers to add.")
        elif x is None:
            return y
        elif y is None:
            return x
        else:
            return x + y

calc = Calculator()
print(calc.add(5))  # Output: 5 (using default y=None)
print(calc.add(3, 4))  # Output: 7





#Data Encapsulation
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.__area = None  

    def calculate_area(self):
        self.__area = 3.14159 * self.radius**2  

    def get_area(self):
        if self.__area is None:
            self.calculate_area()  
        return self.__area
    
circle1 = Circle(3)
circle1.calculate_area 
print(circle1.get_area()) #Output: 28.27431




#Data Abstraction
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area()")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

sq1 = Square(4)
print(sq1.calculate_area()) #Ouput: 16