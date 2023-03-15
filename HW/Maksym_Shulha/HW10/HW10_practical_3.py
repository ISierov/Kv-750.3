class Employee:
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def emp_num(cls):
        print(f"Total number of employees is {Employee.counter}.")

    def info(self):
        print(f"Employee: {self.name} \nSalary: {self.salary}")


emp_1 = Employee("Kate", 5000)
emp_2 = Employee("Andriy", 2000)
emp_3 = Employee("Vasyl", 4000)

Employee.emp_num()
emp_3.info()

print(f"Base classes from which \"Employee\" inherited: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name in which class is defined: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")
