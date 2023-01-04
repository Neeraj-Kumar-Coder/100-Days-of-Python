# Tuples are immutable data items and if we want to change the tuple we must convert it to list first

sample_tuple = ("Hard Work",  7, True, 99.99)
print(sample_tuple)

temp_list = list(sample_tuple)
temp_list.append("This is appended (list)")
temp_list.pop(2)
sample_tuple = tuple(temp_list)
print(sample_tuple)


# However we can concatinate two tuples directly without converting them to list
tuple_1 = ("This is item of tuple 1 (start)", 777, 12,
           False, 23.23, "This is item of tuple 1 (end)")
tuple_2 = ("This is item of tuple 2 (start)", 77, 12,
           True, 23.23, "This is item of tuple 2 (end)")

merged_tuple = tuple_1 + tuple_2
print(merged_tuple, type(merged_tuple))

print("The count of 12 in merged tuple is {}".format(merged_tuple.count(12)))
print("The index of first occurence of 12 in merged tuple is {}".format(
    merged_tuple.index(12)))
