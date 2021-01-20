countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * 1. Explain the difference between map, filter, and reduce.
# map returns the same length processed array back
# filter returns only the elements that satisfy the condition
# reduce returns a  single value, such as sum or product of an list

# * 2. Explain the difference between higher order function, closure and decorator
# note higher order function
# note takes function as parameter, assign function to an variable
# note closure
# note python allows a nested function to access the outer scope of the enclosing function.
# note decorator
# note a decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying it structure.

# * 3. Define a call function before map, filter or reduce, see examples.
def sum_arr(i):
    return i*2

sum_up = map(sum_arr,[1,2,3])

print(list(sum_up))

# * 4. Use for loop to print each country in the countries list.

# * 5. Use for to print each name in the names list.

# * 6. Use for to print each number in the numbers list.

# * 7. Use map to create a new list by changing each country to uppercase in the countries list

# * 8. Use map to create a new list by changing each number to its square in the numbers list

# * 9. Use map to change each name to uppercase in the names list

# * 10. Use filter to filter out countries containing 'land'.

# * 11. Use filter to filter out countries having exactly six characters.

# * 12. Use filter to filter out countries containing six letters and more in the country list.

# * 13. Use filter to filter out countries starting with an 'E'

# * 14. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# * 15. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

# * 16. Use reduce to sum all the numbers in the numbers list.

# * 17. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# * 18. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

# * 19. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

# * 20. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

# * 21. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# * 23. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.