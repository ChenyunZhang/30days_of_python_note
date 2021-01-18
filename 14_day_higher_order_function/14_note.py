# Higher Order Functions

# In python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable


# def sum_numbers(nums):  # normal function
#     return sum(nums)    # a sad function abusing the built-in sum function :<

# def higher_order_function(f, *args):  # function as a parameter
#     summation = f(*args)
#     return summation

# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)       # 15

def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

