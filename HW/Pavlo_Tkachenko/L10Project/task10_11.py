class Polygon:
    def __init__(self):
        pass

class Rectangle(Polygon):
    def __init__(self, sideA, sideB = None):
        self.sideA = sideA
        if self.sideB == None:
            self.sideB = self.sideA
        else:
            self.sideB = sideB

    def square(self):
        return self.sideA * self.sideB

