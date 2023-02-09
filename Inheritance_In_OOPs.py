class Organism:
    def __init__(self) -> None:
        self.living = True
        self.isMortal = True
        self.heartRateAverage = 100

    def showOrganismicDetails(self) -> None:
        print(
            f"Living: {self.living}\nMortal: {self.isMortal}\nAverage Heart Rate: {self.heartRateAverage}")


class Human(Organism):
    def __init__(self) -> None:
        super().__init__()
        self.legsCount = self.handsCount = 2
        self.averageLiving = 90

    def showHumanDetails(self) -> None:
        print(
            f"Number of legs: {self.legsCount}\nNumber of hands: {self.handsCount}\nAverage Living (in years): {self.averageLiving}")


neeraj = Human()
neeraj.showOrganismicDetails()
neeraj.showHumanDetails()
