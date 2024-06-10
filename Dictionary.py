#Dictionary Methods
ceo = {"Microsoft": "Satya Nadella", 
       "Apple": "Tim Cook",
       "Google": "Sundar Pichai"}

print("Ceo names : ", ceo.values()) #Output: "Ceo names : dict_values(['Satya Nadella', 'Tim Cook', 'Sundar Pichai'])"
print("Company names : ", ceo.keys()) #Output: "Company names : dict_keys(['Microsoft', 'Apple', 'Google'])"
print("Company-CEO pairs : ", ceo.items()) #Output: "Company-CEO pairs :  dict_items([('Microsoft', 'Satya Nadella'), ('Apple', 'Tim Cook'), ('Google', 'Sundar Pichai')])"
print("Microsoft ceo : ", ceo.get("Microsoft")) #Output: "Microsoft ceo :  Satya Nadella"
print("Tesla ceo : ", ceo.get("Tesla", False)) #Output: "Tesla ceo :  False"

removed_ceo = ceo.pop("Apple")
print("Removed ceo : ", removed_ceo+ " and Remaining ceo : ", ceo) #Output: "Removed ceo :  Tim Cook and Remaining ceo :  {'Microsoft': 'Satya Nadella', 'Google': 'Sundar Pichai'}"

new_ceo = ceo.copy()
print("Copied ceo list : ", new_ceo) #Output: "Copied ceo list :  {'Microsoft': 'Satya Nadella', 'Google': 'Sundar Pichai'}"

print("CEO's : ", ceo.clear()) #Output: "CEO's :  None"





#Dictionary Comprehension
student_marks = {"ravi": 48,
                 "raj": 78,
                 "sumit": 90,
                 "suman": 67}

swapping = {value: key for key, value in student_marks.items()}
print(swapping) #Output: {48: 'ravi', 78: 'raj', 90: 'sumit', 67: 'suman'}

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = {i: i**2 for i in num if i % 2 == 0}
print("Pairs are : ", even_squares) #Output: "Pairs are :  {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}"

alphas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
new_pair = {alpha: n for alpha, n in zip(alphas, num)}
print("New pair : ", new_pair) #Output: "New pair :  {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}"

