import string
import random

# ## 💻 Exercises: Day 12

# * 1. Writ a function which generates a six digit/character random_user_id.
#    ```py
#      print(random_user_id());
#      '1ee33d'
#    ```

# def random_user_id():
#     temp = string.digits + string.ascii_lowercase
#     i = 0
#     result = ""
#     while i < 6:
#         result += temp[random.randint(0, 35)]
#         i += 1
#     return result

# print(random_user_id())

# * 2. Modify the previous task. Declare a function named user_id_gen_by_user.
# * It doesn’t take any parameters but it takes two inputs using input().
# * One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

#    ```py
# user_id_gen_by_user() # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

# user_id_gen_by_user() # 16 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr
#    ```

# def user_id_gen_by_user():
#     length = int(input("Enter the length of the id: "))
#     quantity= int(input("How many user_id you need: "))
#     temp = string.digits + string.ascii_letters
#     i = 0
#     j = 0
#     while j < quantity:
#         result = ""
#         i = 0
#         while i < length:
#             result += temp[random.randint(0, 35)]
#             i += 1
#         print(result)
#         j+=1

# user_id_gen_by_user()

# * 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
#    ```py
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
#    ```
# def rgb_color_gen():
#     x = random.randint(0,255)
#     y = random.randint(0,255)
#     z = random.randint(0,255)
#     return f"rgb({x},{y},{z})"

# print(rgb_color_gen())

# * 4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# * (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
# * 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# def list_of_hexa_colors():
#     quantity = int(input("How many hexadecimal colors you want to generate?: "))
#     temp = string.digits+"abcdef"
#     arr = []
#     j = 0
#     while j < quantity:
#         i = 0
#         temp_string = ""
#         while i < 6:
#             rand = random.randint(0,len(temp)-1)
#             temp_string+=temp[rand]
#             i+=1
#         arr.append(temp_string)
#         j+=1
#     return arr

# print(list_of_hexa_colors())

# * 5. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# def list_of_rgb_colors():
#     arr = []
#     quantity = int(input("How many RGB colors you want to generate?: "))
#     while quantity>0:
#         arr.append(rgb_color_gen())
#         quantity-=1
#     return arr
# print(list_of_rgb_colors())

# * 6. Write a function generate_colors which can generate any number of hexa or rgb colors.

#    ```py
#     generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#     generate_colors('hexa', 1) # ['#b334ef']
#     generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#     generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
#     ```
# def generate_colors():
#     answer = input("hexa or rgb? ")
#     if answer.lower() == "hexa":
#         return list_of_hexa_colors()
#     elif answer.lower() == "rgb":
#         return list_of_rgb_colors()
#     else:
#         print("Please enter valid input")
#         generate_colors()

# print(generate_colors())

import numpy

# * 7. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# def shuffle_list(lis):
#     random.shuffle(lis)
#     return lis

# print(shuffle_list([1,2,3,3,6,8,0]))

# * 8. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
# def array_of_seven_random_unique_number():
#     arr = []
#     while len(arr) < 7:
#         x = random.randint(0,9)
#         if x not in arr:
#             arr.append(x)
#     return arr
# print(array_of_seven_random_unique_number())