import re
# re.match(substring,string,re.I)
# re.I is case ignore

# re.search()
# re.findall()
# re.split()
# re.sub()

# txt = 'I love to teach python and javaScript'
# match = re.match("I love to teach",txt,re.I)
# search = re.search("a",txt)
# print(search)
# # print(match)
# span = search.span()
# start,end = span
# print(txt[start:end])

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']l



# []: A set of characters
# [a-c] means, a or b or c
# [a-z] means, any letter from a to z
# [A-Z] means, any character from A to Z
# [0-3] means, 0 or 1 or 2 or 3
# [0-9] means any number from 0 to 9
# [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# \d means: match where the string contains digits (numbers from 0-9)
# \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
# r'^substring' eg r'^love', a sentence that starts with a word love
# r'[^abc] means not a, not b, not c.
# $: ends with
# r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
# r'[a]*' means a optional or it can occur many times.
# +: one or more times
# r'[a]+' means at least once (or more)
# ?: zero or one time
# r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
# r'apple|banana' means either apple or a banana
# (): Capture and group