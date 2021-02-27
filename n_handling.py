# Open a TXT File
f = open("n_test.txt", "r")
print(f.read())

# Rewrite a TXT file
w = open("n_test.txt", "w")
w.write("This text will overwrite the content of our file")
# Rewrite this text to see the change

w = open("n_test.txt", "r")
print(w.read())

# Appending a text
a = open("n_test.txt", "a")
a.write("\nThis text will be appended to the file")
a = open("n_test.txt", "r")
print(a.read())

# Create a new file
# f = open("n_test2.txt", "x")