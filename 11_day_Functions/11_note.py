# function note
# note A function is a reusable block of code or programming statements designed to perform a certain task.
# note syntax
# Declaring a function
# def function_name():
#     codes
#     codes
# # Calling a function
# function_name()

# note Function can be declared without parameters.
# note Function can also return values,
# note if a function does not return any, the default value of the function is None.

# note Passing Arguments with Key and Value
# syntax
# Declaring a function
# def function_name(para1, para2):
#     codes
#     codes
# # Calling function
# function_name(para1='John', para2='Doe') # the order of arguments does not matter here

# note If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.
# syntax
# Declaring a function
# def function_name(*args):
#     codes
#     codes
# Calling function
# function_name(param1, param2, param3,..)

# * Example
# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total +=num
#     return total
# print(sum_all_nums(2,3,4))

# Function as a Parameter of Another Function

# def square_number (n):
#     return n * n
# def do_something(f, x):
#     return f(x)
# print(do_something(square_number, 3))