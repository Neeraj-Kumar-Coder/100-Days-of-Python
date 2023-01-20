# result = value_if_true if (condition) else value_if_false

# Above is equivalent to
# if (condition):
#     result = value_if_true
# else:
#     result = value_if_false


def max(first_number, second_number):
    return first_number if (first_number > second_number) else second_number


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    print(
        f"The maximum of {first_number} and {second_number} is = {max(first_number, second_number)}")
except Exception as e:
    print(f"Exception Occured Brother: {e}")


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    relation = ">" if first_number > second_number else "=" if first_number == second_number else "<"
    print(
        f"The relation between {first_number} and {second_number} is {relation}")
except Exception as e:
    print(f"Exception Occured Brother: {e}")
