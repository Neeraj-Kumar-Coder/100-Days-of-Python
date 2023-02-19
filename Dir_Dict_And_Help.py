my_list = [1, 2, 3, 4, 5]
print(dir(my_list))


class Person:
    def __init__(self) -> None:
        self.name = "Neeraj"
        self.age = 22


p = Person()
print(p.__dict__)
print(help(Person))
