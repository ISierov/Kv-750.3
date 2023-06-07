"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

"""
Color Ghost
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
"""
import random
class Ghost:
    def __init__(self):
        self.colors = random.choice(["red", "yellow", "blue", "white"])

"""
According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and 
Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class 
Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
"""

class Human:
    def __init__(self):
        pass

class Man(Human):
    pass

class Woman(Human):
    pass

def create():
    return [Man(), Woman()]

"""
Classy Classes
Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property 
and getInfo method/Info getter which should return johns age is 34.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} age is {self.age}")


"""
Building Spheres
Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
#Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
"""

import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        v = round(4/3 * math.pi * self.radius ** 3, 5)
        return v

    def get_surface_area(self):
        s_a = round(4 * math.pi * self.radius**2, 5)
        return s_a

    def get_density(self):
        d = round(self.mass / self.get_volume(), 5)
        return d

"""
Prepare some function, which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), 
but starting only with upper case letter. In other case it should raise an exception.
"""

def change_class_name(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise ValueError("Invalid class name")

    cls.__name__ = new_name

    return cls