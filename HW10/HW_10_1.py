class Poligon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0] * num_sides

    def input_sides(self):
        self.sides = [float(input(f"Enter side {i+1}: "))
                                for i in range(self.num_sides)]

    def display_sides(self):
        for i in range(self.num_sides):
            print(f"Side {i+1}: {self.sides[i]}")

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        pass


class Rectangle(Poligon):
    def __init__(self):
        super().__init__(2)

    def area(self):
        return self.sides[0] * self.sides[1]


a = Rectangle()
a.input_sides()
a.display_sides()
print(a.area())