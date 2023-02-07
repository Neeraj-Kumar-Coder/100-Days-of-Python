# Decorators in python

def decorator_function(function):
    def modified_function():
        print("Good Morning!")
        function()
        print("Thanks for using this function")

    return modified_function


@decorator_function
def whichUser():
    print("Neeraj Kumar is the user of this Laptop")


# Using decorator is same as: decorator_function(whichUser)()
whichUser()


# PRACTICAL USECASE: Logging
log = []


def logger(function):
    def modified_function(*args, **kwargs):
        log.append(
            f"{function.__name__} is called with arguments {args} and {kwargs}")
        result = function(*args, **kwargs)
        log.append(f"{function.__name__} returned the value {result}")
        return result
    return modified_function


@logger
def add(first_number, second_number):
    return first_number + second_number


add(1, 2)
add(14, 12)
add(24, 35)

print(log)
