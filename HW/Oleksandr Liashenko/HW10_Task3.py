class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print(f"{self.name}'s salary is {self.salary}")

    @classmethod
    def total_numbers(cls):
        print("Total employees:", cls.count)


emp1 = Employee("Carlos", 3800)
emp2 = Employee("Jose", 3220)
emp3 = Employee("Juan", 4100)
Employee.total_numbers()

emp1.display()
emp2.display()
emp3.display()

print(Employee.__base__.__subclasses__())
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

