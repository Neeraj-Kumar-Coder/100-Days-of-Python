# Sets are immutable in python

s = {6, 3, 2, 3}
print(s)
print(type(s))

# It will not create an empty set (it will show <class 'dict'>)
new_set = {}
print(type(new_set))

# Correct method to create an empty set
empty_set = set()
print(type(empty_set))

for item in s:
    print(f"This item is: {item}")
