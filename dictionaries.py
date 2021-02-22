# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:
# String, int, boolean, and list data types:
products = [
  {
    "name": "The Book",
    "quantity": 0,
    "price": 5.99,
    "available": False,
    "year": 1954,
    "colors": ["red", "white", "blue"]
  },
  {
    "name": "The Books",
    "quantity": 3,
    "price": 4.99,
    "available": True,
    "year": 1964,
    "colors": ["red", "white", "blue"]
  }
] 
# type() -> dict
# Dictionary Length
print(len(products))

# Accessing Items
x = products[0]["year"]
# Get Keys
x = products[0].keys()
# Get Values
x = products[0].values()
# Get Items
x = products[0].items()
# Check if Key Exists
if "price" in products:
  print("Yes, 'price' is one of the keys in the products dictionary")

# Update Dictionary
products[1].update({"year": 2020})

# Removing Items
products[1].pop("model") # Remove Key
products[1].popitem() # Remove lastone
del products[1]["model"] # Remove item
del products # Remove the dictionary
products.clear() # Empties the dictionary

# Loop Through a Dictionary
for x in products:
  print(x) # Print key names
  print(products[x]) # Print values name --> This work to for keys and intems-> for x in thisdict.values()

# Copy a Dictionary
mybook = products.copy()
mybook = dict(products)

# ------------------------------------------------------

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary