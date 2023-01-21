my_list = ["My", "name", "is", "Neeraj", "Kumar"]

print(enumerate(my_list))

for index, element in enumerate(my_list):
    print(index, element)


my_string = "This is a sample string"

for index, character in enumerate(my_string, start=1):
    print(index, character, sep="->", end=" ")
