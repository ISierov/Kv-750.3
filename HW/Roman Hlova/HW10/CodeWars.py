#1 Regular Ball Super Ball

class Ball(object):
    def __init__(self, type = "regular"):
        self.ball_type = type

#2 Color Ghost

import random

class Ghost(object): 
    def __init__(self):
        self.color = random.choice(["white","yellow","purple","red"])

#3 Basic subclasses - Adam and Eve

def God():
    return [Man(), Woman()]

class Human:
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass

class Woman(Human):
    def __init__(self):
        pass

#4 Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'

#5 Building Spheres

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
        return round(((4 * math.pi * self.radius ** 3) / 3), 5)

    def get_surface_area(self):
        return round((4 * math.pi * self.radius ** 2), 5)

    def get_density(self):
        return round((self.mass / (4 / 3 * math.pi * self.radius ** 3) ), 5)

#6 Python's Dynamic Classes

import re
def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        cls.__name__ = new_name
    else:
        raise ValueError("Error")

