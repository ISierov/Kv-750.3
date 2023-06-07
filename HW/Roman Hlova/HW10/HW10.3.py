class Employee:

    num_of_emp = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_emp += 1

    def display_emp (self):
        print("name : ", self.name, ",  salary: ", self.salary)
    
    def __del__(self):
        Employee.num_of_emp -= 1

    @classmethod
    def number_of_employee(cls):
        print(Employee.num_of_emp)



print("Employee  base classes:", Employee.__base__)
print("Employee  namespace:", Employee.__dict__)
print("Employee  name:", Employee.__name__)
print("Employee  module name:", Employee.__module__)
print("Employee  __doc__:", Employee.__doc__)

employer1 = Employee("Jeck", 40000)

employer1.display_emp()
Employee.number_of_employee()
