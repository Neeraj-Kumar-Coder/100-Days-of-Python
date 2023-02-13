class Basic:
    def __init__(self) -> None:
        self.id = 0

    def show_id(self) -> None:
        print(self.id)

    @staticmethod
    def multiply(first, second):
        return first * second


instance = Basic()
instance.show_id()
print(Basic.multiply(12, 12))
