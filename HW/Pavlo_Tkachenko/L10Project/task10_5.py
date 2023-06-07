import math


class Ball:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(math.pi*4*math.pow(self.radius,3)/3, 5)
    def get_surface_area(self):
        return round(math.pi*4*math.pow(self.radius,2), 5)
    def get_density(self):
        return round(self.mass/self.get_volume(), 5)

b = Ball(2, 50)
print(b.get_radius())
print(b.get_mass())
print(b.get_volume())
print(b.get_surface_area())
print(b.get_density())
