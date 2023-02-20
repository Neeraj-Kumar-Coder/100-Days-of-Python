# super() is used to call a method of current class parent (including constructors)

class Organism:
    def __init__(self) -> None:
        self.living = True
        self.mortal = True

    def showOrganismicDetails(self):
        print(f"Living = {self.living}\nMortal = {self.mortal}")

    def overloadedFunction(self):
        print("This is parent class method")


class Human(Organism):
    def __init__(self) -> None:
        super().__init__()
        self.legCount = 2
        self.handCount = 2
        self.intelligent = True

    def showHumanDetails(self):
        print(
            f"Leg Count = {self.legCount}\nHand Count = {self.handCount}\nIntelligent = {self.intelligent}")

    def showDetails(self):
        super().showOrganismicDetails()
        self.showHumanDetails()

    def overloadedFunction(self):
        super().overloadedFunction()
        print("This is child class method")


neeraj = Human()

neeraj.showOrganismicDetails()
neeraj.showHumanDetails()

print(end="\n")
neeraj.showDetails()

neeraj.overloadedFunction()
