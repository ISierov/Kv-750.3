# Python's Dynamic Classes #1
#
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:...

class MyClass:
    pass


def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise NameError("Try again")


class_name_changer(MyClass, "NewClass384653")

print(MyClass.__name__)