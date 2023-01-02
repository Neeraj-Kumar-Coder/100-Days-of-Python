sample_list = ["Apple", "Chicken", 100, 60.25, True]
print(sample_list)

sample_list.append("This is added using list.append()")
print(sample_list)

list_of_numbers = [23, 233, 234, 53, 67, 88, 5, 4, 33]
print(list_of_numbers)

list_of_numbers.sort()
print(list_of_numbers)

list_of_numbers.sort(reverse=True)
print(list_of_numbers)

print(list_of_numbers.index(233))
print(list_of_numbers.count(33))

duplicate = list_of_numbers  # Shallow copy
print(duplicate)
duplicate[0] = "Edited"

print(list_of_numbers, duplicate)

deep_copy = list_of_numbers.copy()
deep_copy[0] = "Edited in the deep copy"
print(list_of_numbers, deep_copy)

print("Original List: {}".format(sample_list))
sample_list.insert(2, "Inserted at index 2")
print("Modified List: {}".format(sample_list))

# sample_list.extend(list_of_numbers) # Modified sample_list
concat_list = sample_list + list_of_numbers
print(concat_list)
print(sample_list)
print(list_of_numbers)
