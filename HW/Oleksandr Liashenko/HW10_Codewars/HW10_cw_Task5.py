# Building Spheres
#
# Now that we have a Block let's move on to something slightly more complex a Sphere.

from math import pi


class Sphere:
    def __init__(self, radius, mass):
        self.r = radius
        self.m = mass

    def get_radius(self):
        return self.r

    def get_mass(self):
        return self.m

    def get_volume(self):
        return round(4/3 * pi * self.r ** 3, 5)

    def get_surface_area(self):
        return round(4 * pi * self.r ** 2, 5)

    def get_density(self):
        return round(self.m / (4/3 * pi * self.r ** 3), 5)



