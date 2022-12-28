# For-loop loops over iterable objects in python

name = "Neeraj Kumar"
for character in name:
    print(character, end=", ")

print()

colors = ["Red", "Green", "Yellow", "Blue"]
for color in colors:
    print(color, end=": ")
    for char in color:
        print(char, end=", ")
    print()

print(range(10))

for count in range(10):
    print(count)

for value in range(1, 10):
    print(value)

for idx in range(1, 10, 2):
    print(idx)

limit = input(
    "Enter the value upto which you want a program to print natural numbers without loops: ")
if (not limit.isnumeric()):
    exit("Enter a valid limit!")

limit = int(limit)
for _ in range(1, limit + 1, 1):
    print("print(\"The Value Is: {}\")".format(_))
