# 1. Create  an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Rex",
    "color": ["turquoise", "red", "greys", "black"],
    "breed": "labrador",
    "legs":  1 }
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 4. Get the length of the student dictionary
print(len(dog))
# 5. Get the value of skills and check the data type, it should be a list
print(dog["color"])
print(type(dog["color"]))
# 6. Modify the skills values by adding one or two skills
dog["color"].extend(["purple", "violet"])
print(dog["color"])
# 7. Get the dictionary keys as a list
print(dog.keys())
# 8. Get the dictionary values as a list
print(dog.values())
# 9. Change the dictionary to a list of tuples using _items()_ method
print(dog.items())
# 10. Delete one of the items in the dictionary
dog.pop("color")
print(dog)
# 11. Delete one of the dictionaries
del dog
print(dog)