myStr = "Hello World"


print(dir(myStr)) #Directorio de métodos 
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(myStr.upper())  #HELLOOOO
print(myStr.lower())  #helloooo
print(myStr.swapcase())  #hELLOOOO
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

print(f"My name is {myStr}") #My name is Hello World
print("My name is {0}".format(myStr))
