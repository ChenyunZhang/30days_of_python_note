# list comprehension

# syntax
# note i for i in iterable if expression

# lst = [i for i in "Python"]
# print(lst)

# Generating numbers
# numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
# print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # It is possible to do mathematical operations during iteration
# squares = [i * i for i in range(11)]
# print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # It is also possible to make a list of tuples
# numbers = [(i, i * i) for i in range(11)]
# print(numbers)

even_numbers = [i for i in range(21) if i%2 == 0]
# print(even_numbers)

three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in three_dimen_list for number in row]

# print(flattened_list)

# note lambda function
# x = lambda param1,param2: param1+param2
# print(x(1,2))

# # Named function
# def add_two_nums(a, b):
#     return a + b

# print(2, 3)     # 5
# # Lets change the above function to a lambda function
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2,3))    # 5

# Self invoking lambda function
# (lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console
# square = lambda x : x ** 2
# print(square(3))    # 9
# cube = lambda x : x ** 3
# print(cube(3))    # 27

# # Multiple variables
# multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_variable(5, 5, 3))