# Lists are mutable

my_list = [99, "99", 99.0, [99], True]
print(my_list)
print(type(my_list))

print(my_list[1])
print(my_list[-2])  # equivalent to print(my_list[len(my_list) - 2])
print(my_list[len(my_list) - 2])

if (99 in my_list):
    print("99 is present in my_list")
else:
    print("99 is not present in my_list")

print(my_list[0:2])

# List Comprehension: Generate list on the fly
list_on_fly = [number for number in range(10)]
print(list_on_fly)

list_on_fly = [number for number in range(10) if not number & 1]
print(list_on_fly)
