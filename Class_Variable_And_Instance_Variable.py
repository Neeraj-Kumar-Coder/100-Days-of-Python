class Google:
    company_name = "Google"
    number_of_employees = 99

    def __init__(self) -> None:
        pass


class Employee(Google):
    salary_raise_per_year = 0.3

    def __init__(self, name, age) -> None:
        super().__init__()
        self._id = 0
        self.name = name
        self.age = age

    def show_details(self) -> None:
        print(
            f"Id = {self._id}\nName = {self.name}\nAge - {self.age}\nSalary raise = {self.salary_raise_per_year} / year\nCompany = {self.company_name}\n")


neeraj = Employee("Neeraj Kumar", 22)
neeraj.show_details()

neeraj.salary_raise_per_year = 0.5
neeraj.show_details()

tushar = Employee("Tushar Bharti", 21)
tushar.show_details()

tushar.company_name = "Apple"

neeraj.show_details()
tushar.show_details()
