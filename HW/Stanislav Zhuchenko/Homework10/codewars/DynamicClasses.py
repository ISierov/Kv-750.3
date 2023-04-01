def class_name_changer(cls, new_name):
    cls.__name__ = new_name


class MyClass:
    pass


o = MyClass()
print(MyClass.__name__)

class_name_changer(MyClass, 'SecondMyClass')

print(MyClass.__name__)
