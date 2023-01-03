# Tuples are immutable in python
tup = (1, 2, 3, 4, 5)
print(type(tup))
print(tup)

# Creating tuple of 1 element
one_element_tuple = (1,)
print(type(one_element_tuple))
print(one_element_tuple)

if (3 in tup):
    print("Hard Work")
else:
    print("Be focused")

# Slicings and all are similar here
sliced_tuple = tup[-3:-1:1]
print(sliced_tuple)

print("Iterating a tuple: ", end='')
for value in tup:
    print(value, end=', ')
print()
