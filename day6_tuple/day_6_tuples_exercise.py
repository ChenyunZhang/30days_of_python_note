## 💻 Exercises: Day 6

# 1. Create an empty tuple
tpl = ()
tpl = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters_sibling_tpl = ("Emily","Sara", "Shari", "Eda")
brothers_sibling_tpl = ("Jason", "Kevin", "Panda", "Kyle")

# 3. Join brothers and sisters tuples and assign it to siblings
sibling_tpl = sisters_sibling_tpl+brothers_sibling_tpl

# 4. How many siblings do you have?
print(f"I have {len(sibling_tpl)} siblings.")

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
sibling_list = list(sibling_tpl)
sibling_list.extend(["Cindy","David"])
family_members = tuple(sibling_list)
print(family_members)

# 6. Unpack siblings and parents from family_members
(*siblings,parent_1,parent_2) = family_members
print("siblings",siblings)
print(parent_1)
print(parent_2)

# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("manage","orange")
vegetables = ("carrot","tomato")
animal_products = ("beef","pork")
food_stuff_tp = fruits + vegetables + animal_products

# 8. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp)%2 == 0:
    print(food_stuff_tp[len(food_stuff_tp)//2:len(food_stuff_tp)//2+2])
else:
    print(food_stuff_tp[len(food_stuff_tp)//2])
    
# 10. Slice out the first three items and the last three items from food_staff_lt list
print("first three items: ",food_stuff_lt[:3])
print("last three items: ",food_stuff_lt[-3:])

# 11. Delete the food_staff_tp tuple completely
# del food_staff_tp

# 12. Check if an item exists in  tuple:
print(f"tomato is in food_stuff_tp: {'tomato' in food_stuff_tp}.")