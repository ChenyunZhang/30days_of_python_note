import requests
from bs4 import BeautifulSoup
import re


url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

table = soup.select("tbody td b a")

def get_president_list(table):
    arr = []
    final = []
    for i in range(len(table)):
        if table[i].text == 'George Washington':
            arr = table[i:]
    for i in range(len(arr)):
        if arr[i].text == 'Joe Biden':
            arr = arr[:i+1]
            break
    for i in range(len(arr)):
        final.append(f"{i+1}.{arr[i].text}")
    return final

print(get_president_list(table))

# for i in table:
    # print(i.text)


# soup.findAll(id=re.compile("title"))