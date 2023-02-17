class Employee:
    class_property = "This is class Property"

    @classmethod
    def changeClassProperty(cls, newProperty):
        cls.class_property = newProperty

    def showClassProperty(self):
        print(self.class_property)


e = Employee()
e.showClassProperty()

e.changeClassProperty("This is changed class Property")
e.showClassProperty()

print(Employee.class_property)
