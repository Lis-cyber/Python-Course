# Conditions
# Python makes use of boolean variables to evaluate conditions. When an expression is compared or evaluated, the values returned are either false or true. For example:

x = 2
print x == 2 # TRUE
print x == 3 # FALSE
print x < 3  # TRUE
# Note: to assign values to a variable, the equality operator "=" is used, while to compare variables with each other, two equality signs "==" are used. The operator that inverts the value of comparing two variables is performed with "!=".

# Boolean operators
# The Boolean operators "and " (and) and "or " (or) make it possible to construct complex Boolean expressions, for example:

name = "John"
age = 23
if name == "John" and age == 23:
    print "your name is John, and you are 23 years old."

if name == "John" or name == "Rick":
    print "Your name is John or it can be Rick."
# The "in" operator
# The "in" operator can be used to check if a specific object exists while the same object iterates either in a container or in a list:

if name in ["John", "Rick"]:
    print "His name may be John or Rick."
# Python uses indentation to define blocks of code, rather than braces or parentheses. The standard Python indentation is 4 spaces, although tab and some other spaces will work, as long as they are consistent, that is, they have the same indentation type. Code blocks do not need to be terminated.

# This is an example of how to use the "if" statement in Python using code blocks:

if <statement to evaluate>:
    <lines of code>.
    ....
    ....
elseif <any other statement to evaluate>: # else if
    <lines of code of elseif>.
    ....
    ....
else:
    <code>
    ....
    ....
For example:

x = 2
if x == 2:
    print "x equals two!"
else:
    print "x does not equal two."
# A statement is evaluated as true, if only its iteration or flow is correct: - The true result of a Boolean variable is obtained, or calculated using an expression, as an arithmetic computation. - An object that is not considered "empty" causes the code to continue.

# Here are some examples where objects are considered empty:

# An empty String: ""
# An empty list: []
# The number zero: 0
# The boolean variable false: False
# The "is" operator
# Unlike the double equality operator "==", the "is" operator does not just equate the values of the variables, but equates them to each other. For example

x = [1,2,3]
y = [1,2,3]
print x == y # TRUE
print x is y # FALSE
# The "not" operator
# Using "not" in front of a Boolean expression inverts the equality operator:

print not False # TRUE
print (not False) == (False) # FALSE