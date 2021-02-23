# Python Numbers
# There are three numeric types in Python:
  # int
  # float
  # complex
# Variables of numeric types are created when you assign a value to them:

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
print(type(9)) # Int

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
print(type(10.1)) # Float

# Complex numbers are written with a "j" as the imaginary part:
print(type(2j)) # Complex

age = input("Insert your age: ")
new_age = int(age) + 5 
print(new_age)

# ------------------------------
#Type Conversion
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
# You cannot convert complex numbers into another number type.

# ------------------------------
# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
