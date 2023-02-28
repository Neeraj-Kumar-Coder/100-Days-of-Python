class Dada:
    def __init__(self) -> None:
        self.gene = 1221

    def show_details(self):
        print(f"I am DADA with gene: {self.gene}")


class Papa(Dada):
    def __init__(self) -> None:
        super().__init__()
        self.gene += 23

    def show_details(self):
        super().show_details()
        print(f"I am PAPA with gene: {self.gene}")


class Beta(Papa):
    def __init__(self) -> None:
        super().__init__()
        self.gene %= 13

    def show_details(self):
        super().show_details()
        print(f"I am BETA with gene: {self.gene}")


baccha = Beta()
baccha.show_details()
print(Beta.mro())
