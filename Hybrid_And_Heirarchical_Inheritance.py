class Vehicle:
    def description(self):
        print(f"I am a vehicle")


class Car(Vehicle):
    def description(self):
        super().description()
        print(f"I am a car")


class Racing:
    def description(self):
        print(f"I am a racing utility")


class Ferrari(Car, Racing):
    def description(self):
        Car.description(self=self)
        Racing.description(self=self)
        print(f"I am ferrari")


F8_Tributo = Ferrari()
F8_Tributo.description()
