#List Methods
Sports = ["Cricket", "Football", "Tennis", "Badminton"]

Sports.append("Ice Hockey") 
print("After appending, list = ", Sports) #Output: "After appending, list = ["Cricket", "Football", "Tennis", "Badminton", "Ice Hockey"]"

Sports.insert(3, "Table Tennis") 
print("After inserting, list = ", Sports) #Output: "After inserting, list = ["Cricket", "Football", "Tennis", "Table Tennis", "Badminton", "Ice Hockey"]"

Sports.remove("Tennis") 
print("After removing, list = ", Sports) #Output: "After removing, list = ["Cricket", "Football", "Table Tennis", "Badminton", "Ice Hockey"]"

Sports_shallow_copy = Sports.copy()
Sports_shallow_copy.remove("Badminton") 
print("Copied list = ", Sports_shallow_copy+ " and Original list = ", Sports) #Output: "Copied list = ["Cricket", "Football", "Table Tennis", "Ice Hockey"] and Original list = ["Cricket", "Football", "Table Tennis", "Badminton", "Ice Hockey"]"

import copy
Sports_deep_copy = copy.deepcopy(Sports) 
Sports_deep_copy.insert(2, "Rugby")
print("Copied list = ", Sports_deep_copy+ " and Original list = ", Sports) #Output: "Copied list = ["Cricket", "Football", "Rugby", "Table Tennis", "Baadminton", "Ice Hockey"] and Original list = ["Cricket", "Football", "Table Tennis", "Badminton", "Ice Hockey"]"

Sports.append("Football")
Football_count = Sports.count("Football") 
print("After Counting : ", Football_count) #Output: "After Counting : 2"

more_sports = ["Javeline", "Sprint"]
Sports.extend(more_sports)
print("After extending th e original List : ", Sports) #Output:"After extending th e original List : ["Cricket", "Football", "Table Tennis", "Badminton", "Ice Hockey", "Javeline", "Sprint"]"

Sports.sort()
print("After sorting the list = ", Sports) #Output: "After sorting the list = ["Badminton", "Cricket", "Football", "Ice Hockey", "Javeline", "Sprint", "Table Tennis"]"

Sports.reverse()
print("After reversing the list : ", Sports) #Output: "After reversing the list : ["Table Tennis", "Sprint", "Javeline", "Ice Hockey", "Football", "Cricket", "Badminton"]"

Sports.clear()
print("After clearing the list : ", Sports) #Output: "After clearing the list : []"

removed_sport = more_sports.pop()
print("The sports removed is : ", removed_sport+ " from the list : ", more_sports) #Output: "The sports removed is : Sprint from the list : ["Javeline", "Sprint"]"






#List Comprehension
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for_even = [i for i in range(10) if i % 2 == 0]
print("The even numbers are : ", for_even) #Output: "The even numbers are : [0, 2, 4, 6, 8]"

square_pairs = [(i, i ** 2) for i in range(10)]
print("The Square pairs are : ", square_pairs) #Output: "The Square pairs are : [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]"

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = [item for sublist in nested_list for item in sublist]
print("Single list: ", single_list) #Output: "Single list: [1, 2, 3, 4, 5, 6, 7, 8, 9]"




#List Indexing
Sports = ["Cricket", "Football", "Tennis", "Table Tennis", "Badminton", "Ice Hockey"]

print("First element : ", Sports[0]) #Output: "First element : Cricket"
print("Second element : ", Sports[1]) #Output: "Second element : Football"
print("Second-last element : ", Sports[-2]) #Output: "Second-last element : Badminton"
print("Last element : ", Sports[-1]) #Output: "Last element : Ice Hockey"

old_sport = Sports[2]
Sports[2] = "Hockey"
new_sports = Sports[2]
print("New sport : ", new_sports+ "  and Old sport : ", old_sport) #Output: "New sport : Hockey and Old Sport : Tennis"





#List Slicing
Car_brand = ["BMW", "Mercedes", "Audi", "Toyota", "Bugatti", "Ferarri", "Lamborghini", "Bentley", "Tata"]

print("List elements are : ", Car_brand[0:10]) #Output: "List elements are : ["BMW", "Mercedes", "Audi", "Toyota", "Bugatti", "Ferarri", "Lamborghini", "Bentley", "Tata"]"
print("Top 3 names : ", Car_brand[:3]) #Output: "Top 3 names : ["BMW", "Mercedes", "Audi"]"
print("Last 3 names : ", Car_brand[-3:]) #Output: "Last 3 names : []"Lamborghini", "Bentley", "Tata"]"
print("Reverse of the list : ", Car_brand[::-1]) #Output: "Reverse of the list : ["Tata", "Bentley", "Lamborghini", "Ferarri", "Bugatti", "Toyota", "Audi", "Mercedes", "BMW"]"
print("Names at alternate position : ", Car_brand[::2]) #Output: "Names at alternate position : ["BMW", "Audi", "Bugatti", "Lamborghini", "Tata"]"

Car_brand[1:3] = ["Pagani", "Mahindra"]
print("Updated name : ", Car_brand[0:10]) #Output: "Updated name : ["BMW", "Pagani", "Mahindra", "Toyota", "Bugatti", "Ferarri", "Lamborghini", "Bentley", "Tata"]"

del Car_brand[6:8]
print("After deleteing names : ", Car_brand) #Output: "After deleteing names : ["BMW", "Pagani", "Mahindra", "Toyota", "Bugatti", "Ferarri", "Tata"]"

Car_brand[5:5] = ["Aston Martin"]
print("After adding name : ", Car_brand) #Output: "After adding name : ["BMW", "Pagani", "Mahindra", "Toyota", "Bugatti", "Aston Martin", "Tata"]"






#Special Methods
from functools import reduce

max = reduce(lambda x, y: x if x>y else y, num)
print("Maximum number : ", max) #Output: "Maximum number : 9"

even_numbers = list(filter(lambda x: x%2 == 0, num))
print("List of even numbers is : ", even_numbers) #Output:"List of even numbers is : [0, 2, 4, 6, 8]" 

squares = [0, 1, 4, 9, 16, 25, 36, 79, 64, 81]
num_sq_pairs = list(zip(num, squares))
print("The number-sqaure pair is : ", num_sq_pairs) #Output: "The number-sqaure pair is : [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]"