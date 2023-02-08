import math


class BigInt:
    def __init__(self, number) -> None:
        self.number = number

    def show(self):
        print(self.number)

    @property
    def logOfNumber(self):
        return math.log(self.number)

    @logOfNumber.setter
    def logOfNumber(self, newNumber):
        self.number = math.exp(newNumber)


big = BigInt(100)
big.show()
print(big.logOfNumber)
big.logOfNumber = 10
print(big.logOfNumber)
big.show()