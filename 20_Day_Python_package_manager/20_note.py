import numpy
import pandas
import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# for url in url_lists:
#     webbrowser.open_new_tab(url)
    
    
# pip show --verbose pandas

# import requests # importing the request module

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page


# * ################################################################
# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1]) 

# We use json() method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use text.


from mypackage import arithmetics

print(arithmetics.add_numbers(1,2,3,5))