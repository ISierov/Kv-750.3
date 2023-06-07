class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i+1, "s", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        self.n = 3
        print("This is a triangle")

    def find_area(self):
        s = (sum(self.sides)) / 2
        print((s * (s-self.sides[0]) * (s-self.sides[1]) * (s-self.sides[2])) ** 0.5)


triangle = Triangle()
triangle.input_sides()
triangle.find_area()