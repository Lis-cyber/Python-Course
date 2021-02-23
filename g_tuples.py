# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

number_list = (1, 2, 3, 4, 5)

locations = {
  (35, 39): "Tokio"
  (35, 39): "New York"
}

# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Tuple Length
print(len(number_list))

# Create Tuple With One Item
thistuple = ("apple",)

# Data Types
tuple1 = ("abc", 34, True, 40, "male")

# Access Tuple Items
print(thistuple[1])
print(thistuple[-1]) # Negative indexing means start from the end.
print(thistuple[2:5]) # Range of Indexes (Lastone not included)


# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified 
print(number_list[2:5]) # From the first argument to the second
print(number_list[:4]) # From the beginning to one before the number
print(number_list[2:]) # From the number to the end
print(number_list[-4:-1]) #Negative indexing means starting from the end of the list.

# Check if Item Exists
if 4 in number_list:
  print("Yes, '4' is in the list")


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Add Items
# You cannot add items to a tuple:
y = list(x)
y.append("orange")
x = tuple(y)

# Remove Items
# You cannot remove items in a tuple.
y = list(x)
y.remove("apple")
x = tuple(y)
# Or delete the tuple completely
del x

# Unpack Tuples
# Packing a tuple: 
fruits = ("apple", "banana", "cherry")
# Unpacking a tuple: 
fruits = (green, yellow, red) = fruits
# The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.

# Using Asterisk*
(green, yellow, *red) = fruits # Assign the value to the rest of the values 

# Loop Through a Tuple
for x in fruits:
  print(x)

for i in range(len(fruits)):
  print(fruits[i])


# Using a While Loop
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

# Join Two Tuples
newtuple = fruits + thistuple
# Multiply Tuples
myfruits = fruits * 2

# ------------------------------------------------------------------------

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found