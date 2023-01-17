number = input("Enter a number: ")

if (not number.isnumeric()):
    raise ValueError("Entered number is not a number!!")

print(f"Your number is {number}")

# Defining Custom Exceptions


class CustomError(Exception):
    pass


raise CustomError("This is an amazing error")
