# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#    a) Read obama_speech.txt file and count number of lines and words
#    b) Read michelle_obama_speech.txt file and count number of lines and words
#    c) Read donald_speech.txt file and count number of lines and words
#    d) Read melina_trump_speech.txt file and count number of lines and words
import os
import re
import json
import pprint
import math
# def count_lines(doc_path,filename):
#     with open(doc_path) as f:
#         lines = f.read()
#         count_line = lines.splitlines()
#         count_word = lines.split()

#     print(f"There are {len(count_line)} lines in {filename},{len(count_word)} words in {filename}")

# count_lines("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/obama_speech.txt","obama_speech.txt")
# count_lines("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/michelle_obama_speech.txt","michelle_obama_speech.txt")
# count_lines("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/donald_speech.txt","donald_speech.txt")
# count_lines("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/melina_trump_speech.txt","melina_trump_speech.txt")

# * ######################################################################################################################################
pp = pprint.PrettyPrinter(indent=4)

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
#    ```py
#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 10))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic'),
#    (24, 'Spanish'),
#    (9, 'Russian'),
#    (9, 'Portuguese'),
#    (8, 'Dutch'),
#    (7, 'German'),
#    (5, 'Chinese'),
#    (4, 'Swahili'),
#    (4, 'Serbian')]

#    # Your output should look like this
#    print(most_spoken_languages(filename='./data/countries_data.json', 3))
#    [(91, 'English'),
#    (45, 'French'),
#    (25, 'Arabic')]
#    ```

# def most_spoken_languages(file_path,rank_num):
#     dict = {}
#     final =[]
#     with open(file_path) as f:
#         countries = json.loads(f.read())
#         for i in countries:
#             for language in i["languages"]:
#                 if dict.get(language):
#                    dict[language]+=1
#                 else:
#                     dict[language]=1
#     # dict_val = sorted(dict.values(),reverse=True)
#     # rank_arr = dict_val[:rank_num]
#     sort_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
#     for i in sort_dict[:rank_num]:
#         final.append((i[1],i[0]))
#     return final

# print(most_spoken_languages("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/countries_data.json", 3))

# * #######################################################################################################################################

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

#    ```py
#    # Your output should look like this
#    print(most_populated_countries(filename='./data/countries_data.json', 10))

#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000},
#    {'country': 'Indonesia', 'population': 258705000},
#    {'country': 'Brazil', 'population': 206135893},
#    {'country': 'Pakistan', 'population': 194125062},
#    {'country': 'Nigeria', 'population': 186988000},
#    {'country': 'Bangladesh', 'population': 161006790},
#    {'country': 'Russian Federation', 'population': 146599183},
#    {'country': 'Japan', 'population': 126960000}
#    ]

#    # Your output should look like this

#    print(most_populated_countries(filename='./data/countries_data.json', 3))
#    [
#    {'country': 'China', 'population': 1377422166},
#    {'country': 'India', 'population': 1295210000},
#    {'country': 'United States of America', 'population': 323947000}
#    ]
#    ```

# def most_populated_countries(file_path,rank_num):
#     arr =[]
#     with open(file_path) as f:
#         countries = json.loads(f.read())
#         for country in countries:
#             arr.append({"country":country["name"], "population": country["population"]})
#     sort_dict = sorted(arr, key=lambda x: x["population"], reverse=True)
#     return sort_dict[:rank_num]

# print(most_populated_countries("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/countries_data.json", 3))

# * ######################################################################################################################################

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def extract_email_address(doc_path):
    with open(doc_path) as f:
        lines = f.read()
        emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines))
        with open("emails.txt", "a") as t:
            for email in emails:
                t.write(str(email))
                t.write("\n")
        # pp.pprint(set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines)))
        return re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines)


# * ######################################################################################################################################
extract_email_address(
    "/Users/chenyunzhang/projects/30day/30days_of_python_note/data/email_exchanges_big.txt"
)


# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

# ```py
#     # Your output should look like this

#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
# ```

# def find_most_common_words(doc_path,num):
#     hash = {}
#     with open(doc_path) as f:
#         a = f.read()
#         for i in a.split():
#             if hash.get(i):
#                 hash[i]+=1
#             else:
#                 hash[i]=1
#     sorted_hash = sorted(hash.items(), key=lambda x: x[1] ,reverse=True)
#     return sorted_hash[:num]

# print(find_most_common_words("example.txt",10))
# * ######################################################################################################################################

# 6. Use the function, find_most_frequent_words to find:
#    a) The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
#    b) The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
#    c) The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
#    d) The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
# * ######################################################################################################################################
# skip

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and 
# [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. 
# You may need a couple of functions, function to clean the text(clean_text), 
# function to remove support words(remove_support_words) 
# and finally to check the similarity(check_text_similarity).
# List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory


import sys
sys.path.append('/Users/chenyunzhang/projects/30day/30days_of_python_note/data')
from stop_words import stop_words

def clean_text(doc_path):
    final =[]
    with open(doc_path) as f:
        a = f.read()
        data = a.split()
    for word in data:
        if word.isalpha():
            final.append(word)
    return final

def remove_support_words(txt):
    clean_txt = clean_text(txt)
    final = []
    with open("/Users/chenyunzhang/projects/30day/30days_of_python_note/data/stop_words.py") as f:
        a = f.read()
    for word in clean_txt:
        if word.lower() not in stop_words:
            final.append(word)
    return final

def check_text_similarity(txt_1,txt_2):
    txt1_set = set(remove_support_words(txt_1))
    txt2_set = set(remove_support_words(txt_2))
    return f"The similarity of {txt_1} and {txt_2} is: {math.floor(len(txt2_set.intersection(txt1_set))/len(txt1_set)*100)}%"

# * ######################################################################################################################################
print(check_text_similarity("melina_trump_speech.txt","michelle_obama_speech.txt"))

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt

# * ######################################################################################################################################

# 9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
#    a) Count the number of lines containing python or Python
#    b) Count the number lines containing JavaScript, javascript or Javascript
#    c) Count the number lines containing Java and not JavaScript
