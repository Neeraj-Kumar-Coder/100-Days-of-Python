class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    @classmethod
    def fromString(cls, string):
        tokens = string.split("-")
        return cls(tokens[0], tokens[1])

    def showDetails(self):
        print(self.name, self.salary, sep=", ")


e1 = Employee("Neeraj", 99999)
e1.showDetails()

e2 = Employee.fromString("Neeraj-99999")
e2.showDetails()
