# ### Exercises: Level 1

# 1. Declare an empty list
lst = []
# or lst = list()

# 2. Declare a list with more than 5 items
lst = ["item1","item2","item3","item4","item5","item6"]

# 3. Find the length of your list
print("length of the list: ", len(lst))

# 4. Get the first item, the middle item and the last item of the list
print("first item: ", lst[0])
print("middle item: ", lst[len(lst)//2])
print("last item: ", lst[-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Chenyun", 100, 6.6, "single", "USA"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using _print()_
print("it_companies: ",it_companies)

# 8. Print the number of companies in the list
print(f"there are {len(it_companies)} it_companies")

# 9. Print the first, middle and last company
print(f"first company is {it_companies[0]}")
print(f"middle company is {it_companies[len(it_companies)//2]}")
print(f"last company is {it_companies[-1]}")

# 10. Print the list after modifying one of the companies
it_companies[0] = "Netflix"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Facebook")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,"Snowflake")
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;&nbsp; '
it_companies.extend("#")
print(it_companies)

# 15. Check if a certain company exists in the it_companies list.
print(f"Facebook is in it_companies? {'Facebook' in it_companies}")

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the list
it_companies.pop()
print(it_companies)
if len(it_companies) % 2 == 0:
    print(it_companies[len(it_companies)//2-1:len(it_companies)//2+1])
else:
    print(it_companies[len(it_companies)//2])
          
# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies from the list
if len(it_companies) % 2 == 0:
    del it_companies[len(it_companies)//2-1]
    del it_companies[len(it_companies)//2]
else:
    del it_companies[len(it_companies)//2]
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies
# print(it_companies)

# 26. Join the following lists:
    #  ```py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
    #  ```

front_end.extend(back_end)
print(front_end)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

# ### Exercises: Level 2

# 1. The following is a list of 10 students ages:

# ```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```

# - Sort the list and find the min and max age
ages.sort()
print(f"ages: {ages}")
print(f"min of ages: {min(ages)}")
print(f"max of ages: {max(ages)}")

# - Add the min age and the max age again to the list
ages.insert(0,min(ages))
ages.append(max(ages))
print(f"ages: {ages}")

# - Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    print(ages[len(ages)//2-1])
else:
    print(ages[len(ages)//2])
    
# - Find the average age (sum of all items divided by their number )
mean_val = sum(ages)//len(ages)
print(f'the average age is {mean_val}')

# - Find the range of the ages (max minus min)
max_age = max(ages)
min_age = min(ages)
print(f"the range of the ages is {max_age-min_age}")

# - Compare the value of (min - average) and (max - average), use _abs()_ method
print(f"the difference of the min-mean and max-mean is {abs((max_age-mean_val) - (min_age-mean_val))}")

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print("the country the in the middle is",countries[len(countries)//2])

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half_countries = countries[:len(countries)//2+1]
second_half_countries = countries[len(countries)//2+1:]

print("first_half_countries",first_half_countries)
print("second_half_countries",second_half_countries)
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

lst=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] 
China, Russia, USA, *rest = lst
print(China)
print(Russia)
print(USA)
print(rest)