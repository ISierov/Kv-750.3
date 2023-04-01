class Employee:
    """The class of Employees"""
    __numb_of_inst = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__numb_of_inst += 1

    def __del__(self):
        Employee.__numb_of_inst -= 1

    def disp_name(self):
        return self.name

    def disp_salary(self):
        return self.salary

    @classmethod
    def number_of_instances(cls):
        return Employee.__numb_of_inst

    @classmethod
    def info(cls):
        info = f'<! {cls.__name__} !> is inherited from <! {cls.__base__} !> \n' \
               f'The class namespace: {cls.__dict__} \n' \
               f'The class name is <! {cls.__name__} !> \n' \
               f'The module name in which the class defined <! {cls.__module__} !> \n' \
               f'Doc string <! {cls.__doc__} !>'
        return print(info)


Employee.info()
print('---------------------------------------')
f = Employee('Stas', 100)
s = Employee('Julia', 500)
t = Employee('Alex', 200)

print(f.disp_name(), f.disp_salary())
print(s.disp_name())
print(t.disp_salary())
print(Employee.number_of_instances())

del f, t

print(Employee.number_of_instances())
