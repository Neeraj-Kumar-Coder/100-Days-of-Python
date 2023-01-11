set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {3, 4, 5, 6, 7, 8}

union_of_set1_and_set2 = set_1.union(set_2)
print(union_of_set1_and_set2)

intersection_of_set1_and_set2 = set_1.intersection(set_2)
print(intersection_of_set1_and_set2)

set_1.update(set_2)
print(set_1)

set_1.intersection_update(set_2)
print(set_1)


set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {3, 4, 5, 6, 7, 8}

print(set_1.symmetric_difference(set_2))
print(set_1.difference(set_2))
print(set_2.difference(set_1))

print(set_1.isdisjoint(set_2))

set_1 = {1, 2}
set_2 = {1, 2}
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))

# It (remove()) throws an error it the item was not originally present in the set
set_1.remove(1)
set_1.discard(1)
print(set_1)

# Remove all elements
set_1.clear()
set_2.clear()
print(set_1, set_2)

# delete entire set
del set_1
del set_2
