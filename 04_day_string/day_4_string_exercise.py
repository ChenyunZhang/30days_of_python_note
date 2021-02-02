# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
print(string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string = "Coding " + "For " + "All."
print(string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to capital letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.title())
print(company.capitalize())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company.split(" ")[0])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.find("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", ""))

# Change Python for Everyone to Python for All using the replace method or other methods.
print("Python for Everyone".replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
name = "Python For Everyone"
company = "Coding For All"


def abbreviation(s):
    final = ""
    for i in name:
        if i.isupper():
            final += i
    return final


print(abbreviation(company))
print(abbreviation(name))

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace("because because because", ""))

# Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("Coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# Which one of the following variables return True when we use the method isidentifier():
# challenge = '30DaysOfPython'
# print(challenge.isidentifier())

# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier())

# 30DaysOfPython

# thirty_days_of_python

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
# Use a tab escape sequence to write the following lines.
# Name      Age     Country
# Asabeneh  250     Finland
# Use the string formating method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a cricle with radius 10 is 314 meters square.
# Make the following using string formating methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144