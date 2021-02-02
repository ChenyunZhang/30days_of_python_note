# A tuple is a collection of different data types 
# which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, (). 
# Once a tuple is created, we cannot change its values. 
# We cannot use add, insert, remove methods in a tuple 
# because it is not modifiable (mutable). 
# Unlike list, tuple has few methods. 

# Methods related to tuples:
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

# create empty tuple:
empty_tuple = ()
empty_tuple = tuple()

tpl = ("item1","item2","item3")
tpl1 = (1,2,3)
print(len(tpl))
print(tpl[0])
print(f"item1 is in tpl: {'item1' in tpl}")
print(tpl+tpl1)
del tpl
print(tpl)