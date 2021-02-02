import math
# 💻 Exercises - Day 3
####################################################################
# 1. Declare your age as integer variable

# Answer:
# age = 100
# print("age: ",age)

####################################################################
# 2. Declare your height as a float variable

# Answer:
# height = 5.6
# print("height: ",height)

####################################################################
# 3. Declare a complex number variable

# Answer:
# print('Multiplying complex numbers: ',(1+1j) * (1-1j))
# print(2+1j)

####################################################################
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

# Answer:
# base = int(input("Enter base: "))
# height = int(input("Enter base: "))
# print("The area of the triangle is "+str(int(base*height*0.5))+".")

####################################################################
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

# Answer:
# side_a = int(input("Enter side a: "))
# side_b = int(input("Enter side b: "))
# side_c = int(input("Enter side c: "))
# print("The perimeter of the triangle is "+str(side_a+side_b+side_c)+".")

####################################################################
# 6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# Answer:
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area = length*width
# perimeter = 2 * (length + width)
# print("area: "+str(area))
# print("perimeter: "+str(int(perimeter)))

####################################################################
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# Answer:
# r = int(input("Enter radius: "))
# area = round(math.pi * r * r,2)
# print("area: ",area)

####################################################################
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Answer:
# x = 0
# y = 2*x - 2
# y = 0
# x = (2+y)//2
# slope_8 = 2
# print(x)

####################################################################
# 9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)

# Answer:
# x1 = 2
# x2 = 6
# y1 = 2
# y2 = 10
# m = (y2-y1)/(x2-x1)
# print("m: ",m)

####################################################################
# 10. Compare the slopes in tasks 8 and 9.

# Answer:
# print(slope_8>m)

####################################################################
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.

# Answer:
# x = -3
# y = x**2 + 6*x + 9

####################################################################
# 12. Find the length of 'python' and 'jargon' and make a falsy comparison statement.

# Answer:
# print("length of python > length of jargon: ",len("python") > len("jargon"))

####################################################################
# 13. Use and operator to check if 'on' is found in both 'python' and 'jargon'

# Answer:
# print('"on" in "python" and "on" in "jargon: "',"on" in "python" and "on" in "jargon")

####################################################################
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

# Answer:
# print('"jargon" is in "I hope this course is not full of jargon: "',"jargon" in "I hope this course is not full of jargon")

####################################################################
# 15. There is no 'on' in both dragon and python

# Answer:
# print('"on" not in "dragon" and "on" not in "python": ',"on" not in "dragon" and "on" not in "python")

####################################################################
# 16. Find the length of the text python and convert the value to float and convert it to string

# Answer:
# print(str(float(len("python"))))

####################################################################
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# Answer:
# if number % 2 == 0, then the number is even

####################################################################
# 18. The floor division of 7 by 3 is equal to the int converted value of 2.7.

# Answer:
# print("The floor division of 7 by 3 is equal to the int converted value of 2.7: ",7//3 == 2.7)

####################################################################
# 19. Check if type of '10' is equal to 10

# Answer:
# print(type("10") == type(10))
# print("10" is 10)

####################################################################
# 20. Check if int('9.8') is equal to 10

# Answer:
# print("int('9.8') is equal to 10: ", int(9.8) == 10)

####################################################################
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

####################################################################
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years

# Enter number of years you have lived: 100

# You have lived for 3153600000 seconds.
# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125