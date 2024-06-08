#Inheritance Introduction 
#Single Inheritance
class Car:
    def __init__(self):
        pass
    
    def move_forward(self):
        print("Car is moving forward")
    
    def move_backward(self):
        print("Car is taking reverse")

    def brake(self):
        print("The Car is stopped")


class BMW(Car):
    def __init__(self, color):
        self.color = color
    
    def appearance(self):
        print("It's appearance is Outstanding")

    def handling(self):
        print("It's handling is Superb")

Rolls_Royce = BMW("White")
Rolls_Royce.move_forward() #Output: "Car is moving forward"
Rolls_Royce.move_backward() #Output: "Car is taking reverse"
Rolls_Royce.brake() #Output: "The Car is stopped"
Rolls_Royce.appearance() #Output: "It's appearance is Outstanding"
Rolls_Royce.handling() #Output: "It's handling is Superb"




#Method Resolution Order (MRO)
#Multiple Inheritance
#Hierarchical Inheritance
class Arithmatic:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2
    
    def diff(self, num1, num2):
        return num1 - num2
    
class ComputerCal(Arithmatic):
    def add(self, num3, num4):
        return num3 + num3
    
class NormalCal(Arithmatic):
    def diff(self, num5, num6):
        return num5 - num6
    
cal1 = ComputerCal()
cal2 = NormalCal()

print(cal1.add(2, 3)) #Output: 5
print(cal1.diff(3, 2)) #Output: 1
print(cal2.add(4, 5)) #Ouput: 9
print(cal2.diff(5, 4)) #Output: 1




#Method Overriding
class Father:
    def __init__(self, hair_color, skin_color):
        self.hair_color = hair_color
        self.skin_color = skin_color
    
    def job(self):
        print("He is an Goverment Employee")

class Son(Father):
    def job(self):
        print("He is an Entrepreneur")

class Daughter(Father):
    def job(self):
        print("She is an Doctor")

Ramesh = Father("Brown", "White")
Krish = Son("Black", "White")
Soniya = Daughter("Black", "White")

print(Ramesh.hair_color) #Output: Brown
print(Krish.hair_color) #Output: Black
print(Soniya.skin_color) #Output: White
Ramesh.job() #Output: "He is an Goverment Employee"
Krish.job() #Output: "He is an Entrepreneur"
Soniya.job() #Output: "She is an Doctor"




#Super() Method
class Car:
    def __init__(self, model):
        self.model = model
    
    def move_forward(self):
        print("Car is moving forward")
    
    def move_backward(self):
        print("Car is taking reverse")

    def brake(self):
        print("The Car is stopped")


class BMW(Car):
    def __init__(self, model, color):
        super().__init__(model)
        self.model = model
        self.color = color
    
    def appearance(self):
        print("It,s appearance is Outstanding")

    def handling(self):
        print("It's handling is Superb")

M5 = BMW("Sedan", "Dark Blue")
print("Car color is : ", M5.color) #Output: "Car color is : Dark Blue"
print("Car model is : ", M5.model) #Output: "Car model is : Sedan"