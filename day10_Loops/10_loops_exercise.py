from countries import countries
# import pprint
# ## 💻 Exercises: Day 10

# * 1. Iterate 0 to 10 using for loop, do the same using while loop.
#  for i in range(11):
#    print(i)

# i = 0
# while i<=10:
#     print(i)
#     i+=1

# * 2. Iterate 10 to 0 using for loop, do the same using while loop.
# for i in range(10,-1,-1):
#     print(i)

# i = 10
# while i>=0:
#     print(i)
#     i-=1

# * 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```

# for i in range(1,8):
#     print(i*"#")

# * 4. Use nested loops to create the following:

#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```

# for i in range(1,9):
#     lis = []
#     for j in range(1,9):
#         lis.append("#")
#     string = "".join(lis)
#     print(f"{string}")
        

# * 5. Print the following pattern:

#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```

# for i in range(10):
#     print(f"{i} x {i} = {i * i}")

# * 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# lis = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for lan in lis:
#     print(lan)

# * 7. Use for loop to iterate from 0 to 100 and print only even numbers
# for i in range(101):
#     if i%2 == 0:
#         print(i)
        
# * 8. Use for loop to iterate from 0 to 100 and print only odd numbers
# for i in range(101):
#     if i%2 != 0:
#         print(i)

# * 9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# sum_0_to_100 = 0
# for i in range(101):
#     sum_0_to_100+=i
# print(f"The sum of all numbers is {sum_0_to_100}.")

# * 10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#     ```sh
#     The sum of all evens is 2550. And the sum of all odds is 2500.
#     ```
# even_sum = 0
# odd_sum = 0
# for i in range(101):
#     if i%2 == 0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")

# * 11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word _land_.
# for country in countries:
#     if "land" in country:
#         print(country)

# * 12. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# fruits = ['banana', 'orange', 'mango', 'lemon']
# i = len(fruits)-1
# reversed_fruits = []
# for i in range(len(fruits)-1,-1,-1):
#     reversed_fruits.append(fruits[i])
    
# print(reversed_fruits)