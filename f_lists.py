# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets
# List Items - Data Types
demolist = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
number_list = list((1,2,3,4))
print(number_list) #Type List

# Access Items
print(demolist[1])
# Negative Indexing
print(demolist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
rang = list(range(1, 10))
print(rang)
print(demolist[2:5]) # From the first argument to the second
print(demolist[:4]) # From the beginning to one before the number
print(demolist[2:]) # From the number to the end
print(demolist[-4:-1]) #Negative indexing means starting from the end of the list.
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Check if Item Exists
if "hello" in demolist:
  print("Yes, 'hello' is in the list")

# Change Item Value
demolist[3] = False # Change one value
demolist[1:3] = ["mango"] # Change two values per one

# Insert Items
demolist.insert(2, "mango") # Insert by index
# Append Items
demolist.append("orange") # Append in final 
# Extend List
demolist.extend(colors) # Append elements from another list to the current list. Works whit tuples, sets, dictionaries etc.

# Remove 
demolist.remove("banana") # Specified Item
demolist.pop(1) # By index
demolist.pop() # Remove the last item
del demolist[0] # Remove the first item
del demolist # Delete the entire list
demolist.clear() # Clear the List

# Loop Through a List
for x in colors: 
  print(x)
for i in range(len(colors)):
  print(colors[i])

# Using a While Loop
i = 0
while i < len(colors):
  print(colors[i])
  i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in colors] 
newlist = [expression for item in iterable if condition == True]
newlist = [x for x in colors if x != "blue"]
# Look for more info

# Sort List 
colors.sort() # Alphanumerically
colors.sort(reverse = True) # Sort the list descending
colors.sort(reverse = True) # Sort the list descending

# Copy a List
mylist = demolist.copy()
mylist = list(demolist)

# Join Lists
new_list = demolist + colors # Create a new list
for x in colors:
  demolist.append(x) # Add a list inside other
list1.extend(list2) # Append to the final

# ------------------------------------------------------------------------

print(dir(colors))
# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list