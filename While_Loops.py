value = 0
while (value < 10):
    print(value)
    value += 1

# whlie-else

count = 5
while (count > 0):
    print(count)
    count -= 1
else:
    print("Loop exited successfully!")

# Emulating do-while loop in python
index = 1
while (True):
    print(index)
    index += 1
    if (index >= 10):
        break
else:
    print("This will never be printed!")
