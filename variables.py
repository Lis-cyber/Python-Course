# Variables
# Variables are containers for storing data values.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Variable Names
book_name = "" # Snake Case
bookName = "" # Camel Case
BookName = "" # Pascal Case
PI = 3.1416 # Constant

# Many Values to Multiple Variables
x, book = 100, "I Robot"
print(x, book)

# One Value to Multiple Variables
x = y = z = "Orange"

# Variable names are case-sensitive.

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x) # fantastic

myfunc()
print("Python is " + x) # awesome

# The global Keyword
# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
# Also, use the global keyword if you want to change a global variable inside a function.

# ------------------------
bill = int(input())
tip = bill * 20/100
print(tip)
