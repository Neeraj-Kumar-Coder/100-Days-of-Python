class Person:
    name = ""
    age = 0
    gender = ""

    def info(self):
        return f"{self.name} is a {self.gender} of {self.age} years"


if __name__ == "__main__":
    neeraj = Person()
    neeraj.name = "Neeraj"
    neeraj.age = 22
    neeraj.gender = "Male"

    print(neeraj.info())
