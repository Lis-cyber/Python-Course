# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
myStr = "Hello World"

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# Or three single quotes

# Slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5]) # Slice From the Start
print(b[2:]) # Slice To the End
print(b[-5:-2]) # Negative Indexing, start the slice from the end of the string

# Methods
print(myStr.upper())  #HELLOOOO
print(myStr.lower())  #helloooo
print(myStr.swapcase())  #hELLOOOO
print(myStr.strip()) #Removes any whitespace from the beginning or the end
print(myStr.capitalize())  #Helloooo
print(myStr.replace("Hello", "bye"))  #bye world
print(myStr.count(" ")) #1
print(myStr.startswith("he")) #False
print(myStr.endswith("world")) #False
print(myStr.split("o")) #['Hell', ' W', 'rld']
print(myStr.find("z")) #---
print(len(myStr)) #11
print(myStr.index("e")) #1
print(myStr.isnumeric()) #false
print(myStr.isalpha()) #false
print(myStr[4])  #o
print(myStr[-4]) #o

# String Format
# We can combine strings and numbers
print(f"My name is {myStr}") #My name is Hello World
print("My name is {0}".format(myStr))
# The format() method takes unlimited number of arguments, and are placed into the respective

# Escape Character
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# ------------------------------------------------------------------------

# Escape Characters
# Other escape characters used in Python:

# Code	Result	
# \'	  Single Quote	
# \\	  Backslash	
# \n	  New Line	
# \r	  Carriage Return	
# \t	  Tab	
# \b	  Backspace	
# \f	  Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# ------------------------------------------------------------------------

# String Methods
# Python has a set of built-in methods that you can use on strings.
print(dir(myStr))

# Note: All string methods returns new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
