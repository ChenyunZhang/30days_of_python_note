# ## 💻 Exercises: Day 13

# * 1. Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# x = [i for i in numbers if i < 1]
# print(x)

# * 2. Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# x = [num for num_row in [number for row in list_of_lists for number in row] for num in num_row]
# # y = [number for row in x for number in row]
# print(x)

# * 3. Using list comprehension create the following list of tuples:
#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),  2^3
#    (3, 1, 3, 9, 27, 81, 243), 3^3
#    (4, 1, 4, 16, 64, 256, 1024), 4^3
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```
# def create_tuple():
#     arr = []
#     for i in range(11):
#         temp = (i,1,i,i**2,i**3,i**4)
#         arr.append(temp)
#     return arr
# x = [(i,1,i,i**2,i**3,i**4) for i in range(11)]
# print(x)

# * 4. Flatten the following list to a new list:
#    ```py
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# #    output:
# #    ['FINLAND', 'HELSINKI', 'SWEDEN', 'STOCKHOLM', 'NORWAY', 'OSLO']
# #    ```
# y = [i for row in [i for row in countries for i in row] for i in row]
# print(y)

# * 5. Change the following list to a list of dictionaries:
#    ```py
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```
# key = ["country","city"]
# x = [i for row in countries for i in row]
# arr = []

# for i in x:
#     dict ={}
#     dict["country"] = i[0]
#     dict["city"] = i[1]
#     arr.append(dict)
# print(arr)


# * 6. Change the following list of lists to a list of concatenated strings:
#    ```py
# names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```
# x = [j for j_row in [i for row in names for i in row] for j in j_row]
# print(x)

# * 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# x = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
# print(x(1,2,3,4))