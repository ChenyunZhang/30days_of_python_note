# ## 💻 Exercises: Day 9

# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```

# age = input("Enter your age: ")
# if int(age) >= 18:
#     print("You are old enough to drive.")
# else:
#     print(f"You need {18-int(age)} more years to learn to drive.")


# 2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```

# my_age = 90
# your_age = int(input("Enter your age: "))
# if my_age < your_age:
#     print(f"You are {your_age-my_age} years older than me.")
# elif my_age == your_age:
#     print("We are the same age")
# else:
#     print(f"You are {my_age - your_age} years youger than me.")

# 3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#     ```sh
#     Enter number one: 4
#     Enter number two: 3
#     4 is greater than 3
#     ```

import random as rn
number_one = rn.randint(0,10)
number_two = rn.randint(0,10)
if number_one>number_one:
    print(f"{number_one} is greater than {number_two}")
elif number_one == number_two:
    print(f"{number_one} is equal to {number_two}")
else:
    print(f"{number_one} is less than {number_two}.")

# 4.  Write a code which gives grade to students according to theirs scores:
#     ```sh
#     80-100, A
#     70-89, B
#     60-69, C
#     50-59, D
#     0-49, F
#     ```

# 5.  Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

# 6.  The following list contains some fruits:
#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


# 7. Here we have a person dictionary. Feel free to modify it!
#     ```py
person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}
#     ```
#         * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if person.get("skills"):
    temp = person["skills"]
    print(temp[len(temp)//2])
    
#         * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if person.get("skills"):
    print("python is in the skill set:", "Python" in person["skills"])
#         * If a person skills has only JavaScript and React, 
#         * print('He is a front end developer'), 
#         * if the person skills has Node, Python, MongoDB, 
#         * print('He is a backend developer'), 
#         * if the person skills has React, Node and MongoDB, 
#         * Print('He is a fullstack developer'), else print('unknown title') - 
#         * for more accurate results more conditions can be nested!
#         * If the person is married and if he lives in Finland, print the information in the following format:
#     ```py
#         Asabeneh Yetayeh lives in Finland. He is married.
#     ```