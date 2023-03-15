class Polygon:
    def __init__(self, sides_num):
        self.sides_num = sides_num

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.sides_num)]


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def area(self):
        a, b = self.sides
        area = a * b
        print(f"Area of rectangle is {area}")


r1 = Rectangle()
r1.input_sides()
r1.area()
