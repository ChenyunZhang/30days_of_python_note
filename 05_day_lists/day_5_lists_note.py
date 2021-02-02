# List: is a collection which []
# is ordered and changeable(modifiable).
# Allows duplicate members.
# Tuple: is a collection which ()
# is ordered and unchangeable or unmodifiable(immutable).
# Allows duplicate members.
# Set: is a collection which
# is unordered, unindexed and unmodifiable,
# but you can add new items. No duplicate members.
# Dictionary: {}
# is a collection which is unordered, changeable(modifiable)
# and indexed. No duplicate members.

# duplicate: list and tuple
# ordered: list and tuple
# mutable: list and dictionary

# Two ways to create list:
# 1. lst = []
# 3. lst = list()

# use len() to find the length of a list
# list can store different data types

# unpacking list items
# lst = ['item','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
# print(first_item)     # item1
# print(second_item)    # item2
# print(third_item)     # item3
# print(rest)           # ['item4', 'item5']


# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for 
# start = 0, end = len(lst) - 1 (last item), step = 1)

fruits = ["banana", "orange", "mango", "lemon"]
orange_and_lemon = fruits[::2]
print(orange_and_lemon)
print(fruits[-3:-1])
print(fruits[::-1])
# here we used a 3rd argument, step. 
# It will take every 2cnd item - ['orange', 'lemon']

# insert items into list
# insert(index,item)
fruits.insert(3,"watermelon")
print(fruits)

# removing items using del
del fruits[3]
print(fruits)

# clear() empties the list

# It is possible to copy a list by reassigning it to a new variable in the following way: 
# list2 = list1. Now, list2 is a reference of list1, 
# any changes we make in list2 will also modify the original, list2. 
# copy()

lst = ['item1', 'item2']
lst_copy = lst.copy()

# Joining lists
# 1. plus operator
# 2. extend() method

list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

print(fruits.count("peach"))

print("original fruit list",fruits)
print("reversed fruit list",fruits[::-1])

# To sort lists we can use sort() method 
# or sorted() built-in functions. 
# The sort() method reorders the list items in ascending order and modifies the original list. 
# If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
print("original fruit list",fruits)
print("original fruit list",fruits.sort(reverse=True))
print("original fruit list",sorted(fruits))