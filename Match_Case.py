# Match Case statements are addition from python 3.10
import os
os.system("python --version")

value = input("Enter your number: ")
if (not value.isnumeric()):
    exit("Please enter a valid number!")

value = int(value)
match value:
    case 0:
        print("This value ({}) is zero".format(value))
    case 7:
        print("Your number is Dhoni's jersey number")
    case _ if value & 1:
        print("This is default case and value ({}) is odd".format(value))
    case _:
        print("Nothing matched!")
