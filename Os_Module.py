import os

print(f"Operating System dependent module imported is: {os.name}")
print(f"The current working directory is: {os.getcwd()}")

print("Creating a folder using OS module...")

try:
    os.mkdir("./OS_Module_Created")
except Exception as e:
    print(e)

print("Creating nested directories...")
try:
    number_of_directories = 50
    for number in range(1, number_of_directories + 1, 1):
        os.mkdir(f"./OS_Module_Created/Inside {number}")
        os.open(f"./OS_Module_Created/Inside {number}/main.py", os.O_CREAT)
except Exception as e:
    print(e)

list_of_directories = os.listdir("./OS_Module_Created")
print(
    f"List of directories in OS_Module_Created directory:\n{list_of_directories}")

print("Exiting Program...")
