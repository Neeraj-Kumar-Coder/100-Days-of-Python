import math


class Shape:
    def __init__(self) -> None:
        self.closed = True

    def area(self):
        print("Provides the area of a well defined shape")

    def perimeter(self):
        print("Provides the perimeter of a well defined shape")


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def __str__(self) -> str:
        return f"Circle with a radius of {self.radius} units"

    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


my_circle = Circle(5)
print(my_circle.area())
print(my_circle)
print(repr(my_circle))
