#  Set Operations
cars1 = {"BMW", "Mercedes", "Ferarri", "Toyota"}
cars2 = {"Audi", "Mercedes", "Toyota", "Bugatti"}

print("Merged cars is : ", cars1 | cars2) #Output: "Merged set is :  {'BMW', 'Bugatti', 'Mercedes', 'Toyota', 'Audi', 'Ferarri'}"
print("Common cars : ", cars1 & cars2) #Output: "Common cars :  {'Mercedes', 'Toyota'}"
print("Differennce between the 2 sets are : ", cars1 - cars2) #Output: "Differennce between the 2 sets are :  {'Ferarri', 'BMW'}"
print("Symmetric set of cars : ", cars1 ^ cars2) #Output: "Symmetric set of cars :  {'Bugatti', 'Ferarri', 'Audi', 'BMW'}"




#Set Methods
num = {0, 1, 2, 3, 4, 5, 6}

num.add(7)
print("New set : ", num) #Output: "New set :  {0, 1, 2, 3, 4, 5, 6, 7}"

num.remove(3)
print("After removing : ", num) #Output: "After removing :  {0, 1, 2, 4, 5, 6, 7}"

num.discard(5)
print("After discarding : ", num) #Output: "After discarding :  {0, 1, 2, 4, 6, 7}"

popped_value = num.pop()
print("After popping, the popped value is : ", popped_value) #Output: "After popping, the popped value is :  0"

copied_set = num.copy()
print("After copying, the copied set is : ", copied_set) #Output: "After copying, the copied set is :  {1, 2, 4, 6, 7}"

updated = num.update([8, 9])
print("After updating, the num is : ", num) #Output: "After updating, the num is :  {1, 2, 4, 6, 7, 8, 9}"

num2 = {2,3,4,7,8}
print(num2.issubset(num)) #Output: False

print(num.issuperset(num2)) #Output: False

print(num.isdisjoint(num2)) #Output: False





#Set Comprehension
squares = {i ** 2 for i in range(1,10)}
print("The set of squares are : ", squares) #Output: "The set of squares are :  {64, 1, 4, 36, 9, 16, 49, 81, 25}"

cars_features = {
    "BMW": {"looks", "speed", "comfort"},
    "Tata": {"safety", "looks"},
    "Bugatti": {"looks", "price", "comfort"}
    }
unique_features = {feature for features in cars_features.values() for feature in cars_features}
print("List of unique features : ", unique_features)





#Advanced Set Operations
#Cartesian Product
set1 = (1, 2)
set2 = (7, 8, 9)
product = {(x, y) for x in set1 for y in set2}
print(product) #Output: {(2, 7), (1, 8), (2, 9), (1, 7), (1, 9), (2, 8)}


#Power Set
def power_set(s):
    if len(s) == 0:
        return {frozenset()}
    element = s.pop()
    subsets = power_set(s)
    return subsets.union({subset.union({element}) for subset in subsets})

new_set = {0, 2, 4, 6, 8}
power_set(new_set)


#Frozen Set
new_set = {0, 2, 4, 6, 8}
frozen_set = frozenset(new_set)
print(frozen_set) #Output: frozenset({0, 2, 4, 6, 8})