class emp:
    __doc__ = "this is employee class"
    count_emp = 0
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        emp.count_emp += 1

    def __str__(self):
        return f" inherited: {self.__class__.__base__}; namespace: {self.__dict__}; name: {__name__}; " \
               f"module:{self.__module__}; docs:{self.__doc__}"
    def __del__(self):
        emp.count_emp -= 1
    def count_of_employees(self):
        return emp.count_emp
    def emp_info(self):
        return f"name is {self.__name}; salary is {self.__salary}"

me = emp("Flash", 1000)
ans = emp("Flash2", 1200)
print(ans.count_of_employees(), ";", me.emp_info())
del me
print(ans.count_of_employees())
