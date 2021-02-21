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

