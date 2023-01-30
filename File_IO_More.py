with open("File_IO_More.txt", "w") as file_descriptor:
    print(f"Position before writing is {file_descriptor.tell()}")
    file_descriptor.write("This is now written using python code!")
    print(f"Position after writing is {file_descriptor.tell()}")

with open("File_IO_More.txt", "r") as file_descriptor:
    print(f"Position before reading is {file_descriptor.tell()}")
    file_descriptor.read(10)
    print(f"Position after reading is {file_descriptor.tell()}")

print("\nNow using seek to read some characters of specific positions\n")
with open("File_IO_More_2.txt", "r+") as file_descriptor:
    print(f"Current position of file pointer is at {file_descriptor.tell()}")
    print("Moving file pointer 13 bytes ahead")
    file_descriptor.seek(13)
    print(f"Now current position is {file_descriptor.tell()}")
    print(f"20 bytes from this position is: {file_descriptor.read(20)}")
    file_descriptor.truncate(100)
    file_descriptor.seek(0)
    print(f"Trucated to 100 bytes {file_descriptor.read()}")
