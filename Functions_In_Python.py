import math


def getGeometricMean(first_number, second_number):
    return math.sqrt(first_number * second_number)


def thisFunctionWillBeDefinedLater(number1, number2):
    pass


print(callable(getGeometricMean))
print(callable(thisFunctionWillBeDefinedLater))
print(getGeometricMean(1, 2))
print(getGeometricMean(12, 10))
