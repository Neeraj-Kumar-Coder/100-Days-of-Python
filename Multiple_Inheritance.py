class Brain:
    def __init__(self) -> None:
        self.intelligent = True

    def who_are_you(self):
        return f"I am a Brain"


class Organ:
    def __init__(self) -> None:
        self.function = "Many"

    def who_are_you(self):
        return f"I am an Organ"


class Human(Brain, Organ):
    def __init__(self) -> None:
        super().__init__()
        self.organism = "Human"

    def get_details(self):
        return f"I am a Human"


neeraj = Human()
print(neeraj.who_are_you())
print(neeraj.get_details())
print(neeraj.intelligent, neeraj.organism, sep=", ")
print(f"Human mro: {Human.mro()}")
print(f"Brain mro: {Brain.mro()}")
print(f"Organ mro: {Organ.mro()}")
