weight = float(input())
height = float(input())**2
r = weight/height

# print("Soy h: ", height, r)

if r < 18.5:
  print("Underweight")
elif r >= 18.5 and r < 25:
  print("Normal")
elif r >= 25 and r < 30:
  print("Overweight")
elif r > 30:
  print("Obesity")

# 52, 1.85
# 50, 1.6(2.56)
# 65, 1.6
# 80, 1.6

# --------------------------------
number = int(input())
count = 0

for n in range(0 , number + 1):
  count = n + count
print(count)

# --------------------------------

print("Hello World!")
range(2,20)
str(12)
range(10,20,3)

nums = [1,3,5,2,4]
print(len(nums)) #5

letters = ["a", "b", "c"]
letters += ["d"]
print(len(letters)) #4
## --------------- ## --------------

nums.append(4)
print(nums) # [1, 3, 5, 2, 4, 4]
## --------------- ## --------------
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print("Wordss: ", words) # ['Python', 'is', 'fun']
## --------------- ## --------------
print(letters.index("c"))

print(dir(letters))
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

## --------------- ## --------------
nums = [4,5,6]
msg = "Holis: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
## --------------- ## --------------
a = "{x}, {y}".format(x=5, y=12)
print("Soy a: ", a)
## --------------- ## --------------

text = input()
word = input()

def search(text, word):
  if text.__contains__(word):
    print("Word Found") 
  else:
    print("Word not Found")
search(text, word)
