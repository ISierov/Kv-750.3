"""
Regular Ball Super Ball

Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)


"""
Color Ghost

Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
"""
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
ghost = Ghost()
print(ghost.color)


"""
Basic subclasses - Adam and Eve

You have to do God's job. The creation method must return an array of length 2 containing objects (representing 
Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance 
of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman 
classes.
"""
class Human:
    def __init__(self):
        pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

print(God())


"""
Classy Classes

Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property 
and getInfo method/Info getter which should return johns age is 34
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return str(f"{self.name}s age is {self.age}")


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
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


"""
Python's Dynamic Classes #1

Prepare some function, which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), 
but starting only with upper case letter. In other case it should raise an exception.
"""
def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception("Name contains restricted values")