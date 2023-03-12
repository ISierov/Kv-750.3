# Task1. Create a polygon class and a rectangle class that inherits from the
# polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f'Enter side {str(i + 1)}: '))
                      for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def square(self):
        a, b = self.sides
        square = 2 * (a + b)
        print(f'The square of rectangle is {square}')

rec = Rectangle()
rec.input_sides()
rec.square()