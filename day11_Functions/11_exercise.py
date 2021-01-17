import math
import cmath
from countries_data import data
# ## 💻 Exercises: Day 11

# * 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
# def add_two_numbers(num_1, num_2):
#     return num_1+num_2

# * 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
# def area_of_circle(r):
#     area = math.pi * r * r
#     return area

# * 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# def add_all_nums(*args):
#     sum_all_num = 0
#     for i in args:
#         if isinstance(i,int):
#             sum_all_num+=i
#         else:
#             print(f"{i} is not a number")
#     return sum_all_num

# print(add_all_nums(1,2,3,4,4,"p"))

# * 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celcius_to-fahrenheit_.
# def convert_celcius_to_fahrenheit(celcius):
#     fahrenheit = (celcius * 9/5)+32
#     return fahrenheit

# * 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# def check_season(month):
#     if month.lower() == "march" or month.lower() == "april" or month.lower() == "may":
#         return "Spring"
#     if month.lower() == "june" or month.lower() == "july" or month.lower() == "august":
#         return "Summer"
#     if month.lower() == "september" or month.lower() == "october" or month.lower() == "november":
#         return "Autumn"
#     if month.lower() == "december" or month.lower() == "january" or month.lower() == "febuary":
#         return "Winter"

# * 6. Write a function called calculate_slope which return the slope of a linear equation
# def calculate_slope(x1,y1,x2,y2):
#     slope = (y2-y1)/(x2-x1)
#     return slope

# * 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
# def solve_quadratic_eqn(a,b,c):
#     d = (b**2) - (4*a*c)
#     sol1 = (-b-cmath.sqrt(d))/(2*a)
#     sol2 = (-b+cmath.sqrt(d))/(2*a)
#     return 'The solution are {0} and {1}'.format(sol1,sol2)
# print(solve_quadratic_eqn(1,2,3))

# * 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# def print_list(lis):
#     for i in lis:
#         print(i)
# print(print_list([1,2,3]))

# * 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# ```
# def reverse_list(arr):
#     # return arr[::-1]
#     reverse_arr = []
#     for i in range(len(arr)-1,-1,-1):
#         reverse_arr.append(arr[i])
#     return reverse_arr

# print(reverse_list([1,2,3]))

# * 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# def capitalize_list_items(lis):
#     cap_list = []
#     for i in lis:
#         cap_list.append(i.capitalize())
#     return cap_list
# print(capitalize_list_items(["a","b","COAasd"]))

# * 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# ```
# def add_item(lis,add_item):
#     lis.extend([add_item])
#     return lis
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))

# * 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```
# def remove_item(lis,item_to_be_removed):
#     if item_to_be_removed not in lis:
#         return f"{item_to_be_removed} is not in {lis}"
#     else:
#         lis.remove(item_to_be_removed)
#     return lis

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];

# * 13.  Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050

# ```
# def sum_all_numbers(nums):
#     sum = 0
#     for num in range(nums+1):
#         sum+=num
#     return sum

# print(sum_all_numbers(10))

# * 14.  Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# def sum_of_odds(num):
#     sum = 0
#     for i in range(num+1):
#         if i % 2 != 0:
#             sum+=i
#     return sum
# print(sum_of_odds(3))

# * 15.  Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# def sum_of_even(num):
#     sum = 0
#     for i in range(num+1):
#         if i % 2 == 0:
#             sum+=i
#     return sum
# print(sum_of_even(3))

# * 16.  Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ```
# def evens_and_odds(positive_number):
#     count_even = 0
#     count_odd = 0
#     for i in range(positive_number+1):
#         if i%2 == 0:
#             count_even+=1
#         else:
#             count_odd+=1
#     return f"The number of odds is {count_odd}.\nThe number of evens is {count_even}."

# print(evens_and_odds(100))
# * 17. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# def factorial(number):
#     if number < 3:
#         return number

#     return number * factorial(number-1)

# print(factorial(3))

# * 18. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
# def is_empty(lis):
#     if len(lis) == 0:
#         return True
#     else:
#         return False

# * 19. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# def calculate_mean(lis):
#     return sum(lis)/len(lis)

# def calculate_median(lis):
#     if len(lis) % 2 != 0:
#         return lis[len(lis)//2]
#     else:
#         return sum(lis[len(lis)//2,len(lis)//2+2])/2

# def calculate_mode(lis):
#     mode = 0
#     for i in lis:
#         mode = max(lis.count(i), mode)
#     for i in lis:
#         if mode == lis.count(i):
#             return i

# def calculate_range(lis):
#     return max(lis)-min(lis)

# def calculate_variance(lis):
#     sum_of_square = 0
#     mean = sum(lis)/len(lis)
#     for i in lis:
#         sum_of_square+= (i - mean) ** 2
#     return sum_of_square/(len(lis))

# print(calculate_variance([1,2,3,4]))

# def calculate_std(lis):
#     return math.sqrt(calculate_variance(lis))

# print(calculate_std([10, 12, 23, 23, 16, 23, 21, 16]))

# * 20. Write a function called is_prime, which checks if a number is prime.
# def is_prime(num):
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(1,int(math.sqrt(num))+1):
#         if num % i ==0:
#             return False
#     return True

# print(is_prime(9))

# * 21. Write a functions which checks if all items are unique in the list.
# def check_uniq(lis):
#     return len(set(lis)) == len(lis)

# print(check_uniq([1,2,2,4]))

# * 22. Write a function which checks if all the items of the list are of the same data type.
# def check_data_type(arr):
#     i = 0
#     while i < len(arr)-1:
#         if type(arr[i]) != type(arr[i+1]):
#             return False
#         i+=1
#     return True
# print(check_data_type([1,2,3,4,5,6,[]]))

# * 23. Write a function which check if provided variable is a valid python variable
# def check_valid_var(variable):
#     txt = variable
#     return txt.isidentifier()
# print(check_valid_var("asd"))

# * 24. Go to the data folder and access the countries-data.py file.
# * Create a function called the most_spoken_languages in the world. 
# * It should return 10 or 20 most spoken languages in the world in descending order
# def most_spoken_languages(data):
#     dict = {}
#     for country in data:
#         for lan in country["languages"]:
#             if lan in dict:
#                 dict[lan]+=1
#             else:
#                 dict[lan]=1
#     arr = list(dict.values())
#     arr.sort(reverse=True)
#     arr = arr[:10]
#     result = []
#     for i in arr:
#         for key in dict:
#             if i == dict[key]:
#                 result.append(key)
#     return list(set(result))[:10]
    
# print(most_spoken_languages(data))

# * Create a function called the most_populated_countries. 
# * It should return 10 or 20 most populated countries in descending order.
# def most_populated_countries(data):
#     dict = {}
#     arr = []
#     for i in data:
#         arr.append(i["population"])
#     arr.sort(reverse=True)
#     arr = arr[:10]
#     result = []
#     for i in arr:
#         for j in data:
#             if i == j["population"]:
#                 result.append(j["name"])
#     return result
# print(most_populated_countries(data))