class Parent:
    def __init__(self) -> None:
        self.gene = 'x'
        self.mortality = 100

    def show_gene(self):
        print(self.gene)


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()

    def my_func(self):
        print("This is child class method")

    def show_gene(self):
        print(self.gene)

    def alter_gene(self):
        self.gene = 'x' if self.gene == 'y' else 'y'


p = Parent()
c = Child()

p.show_gene()
c.show_gene()

c.alter_gene()
c.show_gene()
