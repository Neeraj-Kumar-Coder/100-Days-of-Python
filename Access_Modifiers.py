# In python there is no concept called access modifiers.
# These are just convention used by the people and may vary from organization to organization

class Person:
    def __init__(self) -> None:
        self.name = "Neeraj"
        self.age = 22
        self._protected = 99  # protected is prefixed with '_'
        self.__private = 999  # private is prefixed with '__'


cool_dude = Person()
print(cool_dude.name)
print(cool_dude.age)
print(cool_dude._protected)
# print(cool_dude.__private) # Throws an error
# print(cool_dude._Person__private) # Can be accessed through name-mangling
