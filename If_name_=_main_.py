import custom_module

print(dir(custom_module))

try:
    count_of_inputs = int(
        input("Enter the number of values you want to input: "))
    collection = list(range(count_of_inputs))
    for index in range(0, count_of_inputs, 1):
        collection[index] = int(input(f"Enter the input number {index + 1}: "))

    print(f"Maximum among {collection} = {custom_module.max(collection)}")
    print(f"Minimum among {collection} = {custom_module.min(collection)}")
except Exception as e:
    print(e)


print("End of the program")
