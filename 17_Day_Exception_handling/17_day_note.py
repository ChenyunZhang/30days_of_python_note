# try:
#     a = int("a")
# except:
#     print(f"int can't convet 'a'")
# else:
#     print(a)
# finally:
#     print("bye")
    
# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong

# try:
#     name = input('Enter your name:')
#     year_born = int(input('Year you were born:'))
#     age = 2019 - year_born

#     print(f'You are {name}. And your age is {age}.')
# except:
#     print('Something went wrong')
    
    
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

# note packing and unpacking argument in python
# note * for tuples
# note ** for dictionaries

# When we run the this code, it raises an error, 
# because this function takes numbers (not a list) as arguments. 

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1,2,3,4,5]
# print(sum_of_five_nums(*lst))

# numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers)) # [2, 3, 4, 5, 6]
# args = [2, 7]
# numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers) 


# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# def unpacking_person_info(name, country, city, age):
#     return '{name} lives in {country}, {city}. He is {age} year old.'
# dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6,7]
# lst = [0, *list_one, *list_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)        ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


