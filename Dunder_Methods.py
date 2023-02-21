# Dunder / Magic methods in python

class Organism:
    def __init__(self, type) -> None:
        self.note = "Organism are the boons and bans"
        self.type = type
        self.isLiving = True
        self.isMortal = True

    def __str__(self) -> str:
        return f"Note: {self.note}\nOrganism Type: {self.type}\nLiving: {self.isLiving}\nMortal: {self.isMortal}\n"

    def __repr__(self) -> str:
        return f"Organism('{self.type}')"

    def __call__(self):
        print(f"Hey I am a {self.type}!")

    def __len__(self):
        return len(self.__str__())


neeraj = Organism("Human")

print(neeraj)
neeraj()
print(repr(neeraj))
print(len(neeraj))
