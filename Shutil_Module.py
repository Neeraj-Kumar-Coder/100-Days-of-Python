import shutil

copy_directory_location = shutil.copytree(
    "./Playing With Shutil", "./Playing With Shutil/folder")

print(copy_directory_location)

copy_destination = shutil.copy("./Playing With Shutil/file.txt",
                               "./Playing With Shutil/folder/file_copy.txt")

print(copy_destination)

shutil.rmtree("./Playing With Shutil/folder")
