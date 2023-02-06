class Player:
    def __init__(self, name, health, armour) -> None:
        self.name = name
        self.health = health
        self.armour = armour

    def details(self) -> None:
        print(
            f"Player {self.name} has health {self.health}% and armour {self.armour}%")


neeraj = Player("Neeraj", 100, 100)
someone = Player("Mr. X", 67, 98)

neeraj.details()
someone.details()
