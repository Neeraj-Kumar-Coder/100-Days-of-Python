def factorial(number):
    if (number == 1 or number == 0):
        return 1
    return number * factorial(number - 1)


number = input("Enter the number you want to calculate the factorial of: ")
if (not number.isnumeric()):
    exit("Enter a valid number")

number = int(number)
print(f"The factorial of {number} = {factorial(number)}")


def fibonacci(number):
    if (number == 0 or number == 1):
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


number = input("Enter the number you want to calculate the fibonacci of: ")
if (not number.isnumeric()):
    exit("Enter a valid number")

number = int(number)
print(f"The {number}-th fibonacci number is = {fibonacci(number)}")
