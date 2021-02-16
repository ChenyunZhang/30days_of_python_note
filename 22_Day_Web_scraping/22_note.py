import requests
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs"
response = requests.get(url)
# lets check the status
status = response.status_code
# print(status)

content = response.content  # we get all the content from the website
soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.body)

test = soup.findAll("li", {"app-store"})
print(test)
