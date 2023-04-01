"""
Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle.
"""


class Polygon:
    pass


class Rectangle(Polygon):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b


Rect = Rectangle(10, 20)
print(Rect.square())
