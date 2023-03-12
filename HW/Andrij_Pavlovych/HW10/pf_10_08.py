# Building Spheres
# Now that we have a Block let's move on to something slightly more complex a Sphere.
# #Arguments for the constructor
#
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
#
# #Methods to be defined
#
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
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
        return round((self.mass / (4 * math.pi * self.radius ** 3) ), 5)

s1 = Sphere(1.25, 456.3)
print(s1.get_density())