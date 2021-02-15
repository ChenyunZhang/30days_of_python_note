# Read this url and find the 10 most frequent words. 
# Romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# *********************************************************************************
import requests

response = requests.get("http://www.gutenberg.org/files/1112/1112.txt")
def find_most_frequently_used_word(txt):
    for i in txt:
        print(i)

find_most_frequently_used_word(response)


# Read the cats api and cats_api = 'https://api.thecatapi.com/v1/breeds' 
# and find the avarage weight of a cat in metric units.
# *********************************************************************************

# Read the countries api and find the 10 largest countries
# *********************************************************************************


# UCI is one the most common places to get data sets for data science and machine learning. 
# Read the content of UCL (http://mlr.cs.umass.edu/ml/datasets.html). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
# # *********************************************************************************