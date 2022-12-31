# There are 4 types of function arguments in python

# 1. Required Arguments
def getAverage(first_number, second_number):
    return (first_number + second_number) / 2


print(getAverage(5, 15))


# 2. Default Arguments (Note: Non-default argument must not follows default argument)
def getAverageWithDefault(first_number=0, second_number=0):
    return (first_number + second_number) / 2


print(getAverageWithDefault())


# 3. Keyword Arguments (Order doesn't matter when passing)
def printArguments(first_argument, second_argument, third_argument):
    print("The first argument is: {}\nThe second argument is: {}\nThe third argument is: {}".format(
        first_argument, second_argument, third_argument))


printArguments(second_argument=12, third_argument=11, first_argument=34)


# 4. Varible length argument (Note: It takes arguments as a tuple)
def variableFunction(*arguments):
    for _ in arguments:
        print(_)


variableFunction(12, 12, 23, 34, 35, 23, 45)


# 5. Taking argument as dictionary
def takeArgsAsDict(**arguments):
    print("First Name: {}\nLast Name: {}".format(
        arguments["first_name"], arguments["last_name"]))


takeArgsAsDict(first_name="Neeraj", last_name="Kumar")
