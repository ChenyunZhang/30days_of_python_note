import requests
from bs4 import BeautifulSoup

url = "https://vax4nyc.nyc.gov/patient/s/vaccination-schedule"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())