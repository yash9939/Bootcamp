#Creating Tuple
cars = ("BMW", "Mercedes", "Audi", "Bugatti", "Tata")



#Tuple is Immutable
cars[2] = "Aston Martin"
print("Third car is : ", cars[2]) #Output: TypeError: 'tuple' object does not support item assignment





#Accessing elements through indexing
print("First car name is : ", cars[0]) #Output: "First car name is :  BMW"

print("Last car name : ", cars[-1]) #Output: "Last car name :  Tata"

print("First 3 car names : ", cars[0:3]) #Output: "First 3 car names :  ('BMW', 'Mercedes', 'Audi')"

print("Last 3 car names : ", cars[-3:]) #Output: "Last 3 car names :  ('Audi', 'Bugatti', 'Tata')"

print("Car names at alternate positions : ", cars[::2]) #Output: "Car names at alternate positions :  ('BMW', 'Audi', 'Tata')"



#Using Asterisk *
(Outstanding, Excellent, *Good) = cars

print(Outstanding) #Output: BMW

print(Excellent) #Output: Mercedes

print(Good) #Output: ['Audi', 'Bugatti', 'Tata']


#Joining 2 Tuples
cars2 = ("Pagani", "Lamborghini", "Mahindra", "Toyoyta")

cars3 = cars + cars2

print("Combined car names are : ", cars3) #Output: "Combined car names are :  ('BMW', 'Mercedes', 'Audi', 'Bugatti', 'Tata', 'Pagani', 'Lamborghini', 'Mahindra', 'Toyoyta')"