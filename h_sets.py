# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.

colors = {"Red", "Black", "blue"} 
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Get the Length of a Set
print(len(colors))

# Data Types
set1 = {"abc", 34, True, 40, "male", "banana"}

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# Access Items
for x in thisset: # Loop through the set, and print the values
  print(x)

print("banana" in thisset) # Check if "banana" is present in the set

# !! Once a set is created, you cannot change its items, but you can add new items.
# Add Items
thisset.add("orange")
# Add Sets
thisset.update(colors) # Works with tuples, lists, dictionaries etc.

# Remove Item
thisset.remove("banana")
thisset.discard("banana")
thisset.pop() # Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset.clear() # Empties the set
del thisset # Delete the set completely


# Loop Through a Dictionary
for x in thisset:
  print(x) # Print key names
  
# Join Two Sets
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set2 = set1.union(colors)
set1.update(colors)
# Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates
set1.intersection_update(thisset) # keep only the items that are present in both sets
newset = set1.intersection(thisset) # Return a new set
# Keep All, But NOT the Duplicates
set1.symmetric_difference_update(thisset) # Keep the items that are not present in both sets
# Return a new set, that contains only the elements that are NOT present in both sets
newset2 = set1.symmetric_difference(thisset)

# ------------------------------------------------------

# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others