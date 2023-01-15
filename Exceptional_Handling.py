number = 0

try:
    number = int(input("Enter a number: "))
    print(f"Your number is {number}")
except Exception as e:
    print(e)


try:
    number = int(input("Enter your number: "))
    number /= 0
    print(f"Number after dividing by zero: {number}")
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)

print("End of program...")
