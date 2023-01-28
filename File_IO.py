# Modes:
# 1. r (read)
# 2. w (write)
# 3. a (append)
# 4. x (create)
# 5. t (open as text file)
# 6. b (open as binary file)

file_descriptor = open("File_Created_With_Python.txt", "w")
file_descriptor.write("This is written using a python program")
file_descriptor.close()

file_descriptor = open("File_Created_With_Python.txt", "rt")
data = file_descriptor.read()
print(data)
file_descriptor.close()


# Using the with keyword

with open("File_Created_With_Python.txt", "a") as file_descriptor:
    data_to_write = input(
        "Enter the data that you want to append to the file: ")
    file_descriptor.write(data_to_write)


copy_program = open("KBC_Copy.txt", "w")
original_program = open("KBC.py", "r")

copy_program.write(original_program.read())
copy_program.close()
original_program.close()

# Reading a binary file
image_file = open("Nature.jpg", "rb")
nature_binary = open("Nature_Binary.txt", "wb")
nature_binary.write(image_file.read())
image_file.close()
nature_binary.close()

print("Program completed...")
