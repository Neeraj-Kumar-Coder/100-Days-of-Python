with open("File_IO_Methods.txt", "w") as file_descriptor:
    lines = ["This is line 1\n", "This is line 2\n",
             "This is line 3\n", "This is line 4\n"]
    file_descriptor.writelines(lines)


with open("File_IO_Methods.txt", "r") as file_descriptor:
    while True:
        line = file_descriptor.readline()
        if not line:
            break
        print(line)

with open("File_IO_Methods.txt", "r") as file_descriptor:
    print(file_descriptor.readlines())

with open("File_IO_Methods.txt", "a") as file_descriptor:
    lines = ["This is first line", "This is second line",
             "This is third line", "This is fourth line"]
    for line in lines:
        file_descriptor.write(line + '\n')
