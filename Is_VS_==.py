list_1 = [1, 2, 3]
list_2 = [1, 2, 3]

print(list_1 is list_2)
print(list_1 == list_2)

# Any immutable object is created once in memory
num1 = 12
num2 = 12
print(num1 is num2)
print(num1 == num2)

num1 = None
num2 = None
print(num1 is num2)
print(num1 == num2)
print(num1 is None)
print(num2 is None)
