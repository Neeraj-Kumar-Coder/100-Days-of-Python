class Vector:
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x})i + ({self.y})j + ({self.z})k"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(
                f"The operands must be of same type {type(Vector)}")

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(
                f"The operands must be of same type {type(Vector)}")
        return Vector(self.y*other.z - self.z*other.y, -1 * (self.x*other.z - self.z*other.x), self.x*other.y - self.y*other.x)

    def __truediv__(self, value):
        return Vector(self.x / value, self.y / value, self.z / value)

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError(
                f"The operands must be of same type {type(Vector)}")
        return self.x + other.x + self.y + other.y + self.z + other.z

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)


my_vector = Vector(x=2, y=3, z=4)
print(my_vector)

v1 = Vector(x=2, y=9, z=9)
print(v1)
print(my_vector / abs(my_vector))

print(my_vector.dot(v1))
print(v1 * my_vector)
