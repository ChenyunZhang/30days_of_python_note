dict = {}

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name


# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.