class Employee:

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def employee_num(cls):
        print(f"The company has {Employee.counter} employees")

    def about_emp(self):
        print(f"Employee {self.name} earns {self.salary}!")

