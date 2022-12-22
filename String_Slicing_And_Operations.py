items = "Apple,Orange,Guava,Banana"
print(items[0:5])
print(items[:9])  # ~items[0:9]
print(items[:])  # ~items[0:len(items)]

# Negative values are handled by python interepreter by adding it with the length of the string
print(items[0:-4])  # ~items[0:len(items)-4]
print(items[-12:-3])  # ~items[len(items)-12:len(items)-3]
