# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)

class Employee(object):
    """Employees. Class of workers"""
    __counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__counter += 1

    def __del__(self):
        self.__counter -= 1

    @classmethod
    def get_num_employee(cls):
        print(f'Number of employees {Employee.__counter}')

e1 = Employee(1, 2)
e2 = Employee(5,7)
# return number of objects in Employee class
Employee.get_num_employee()
# return description of Employee class
print(Employee.__doc__)
# return nearest parent type of inheritance
print(Employee.__base__)
# return all the data stored in Employee class
print(Employee.__dict__)
# return name of the class of object e1
print(type(e1).__name__)
# return the name of the module in which the class was declared
print(Employee.__module__)
