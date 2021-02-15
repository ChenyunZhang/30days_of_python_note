# Read this url and find the 10 most frequent words.
# Romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# *********************************************************************************
import requests

response = requests.get("http://www.gutenberg.org/files/1112/1112.txt")
txt = response.text


def find_most_frequently_used_word(txt, num):
    hash = {}

    for word in txt.split():
        if word.isalnum():
            if hash.get(word):
                hash[word] += 1
            else:
                hash[word] = 1
    sorted_hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
    return sorted_hash[:num]


# print(find_most_frequently_used_word(txt,5))
# *********************************************************************************
# Read the cats api and cats_api = 'https://api.thecatapi.com/v1/breeds'
# and find the avarage weight of a cat in metric units.

response = requests.get("https://api.thecatapi.com/v1/breeds")
cats = response.json()


def find_average_cat_weight(cats):
    for cat in cats:
        arr = []
        cat_name = cat["name"]
        for num in cat["weight"]["metric"]:
            if num.isdigit():
                arr.append(int(num))
        print(f"{cat_name}'s average weight is {sum(arr)/2}.")


# find_average_cat_weight(cats)

# *********************************************************************************
# Read the countries api and find the 10 largest countries
url = "https://restcountries.eu/rest/v2/all"  # countries api
response = requests.get(url)  # opening a network and fetching a data
countries = response.json()


def rank_countries(countries, rank):
    arr = []
    for country in countries:
        if country["area"]:
            arr.append({"country": country["name"], "area": country["area"]})
        else:
            arr.append({"country": country["name"], "area": 0})
    sorted_countries = sorted(arr, key=lambda x: x["area"], reverse=True)
    return sorted_countries[:rank]


# print(rank_countries(countries, 3))

# *********************************************************************************
# UCI is one the most common places to get data sets for data science and machine learning.
# Read the content of UCL (http://mlr.cs.umass.edu/ml/datasets.html). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
