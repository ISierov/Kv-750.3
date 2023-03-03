import task08_31
import random

a = random.randrange(1, 10)
b = random.randrange(1, 10)
h = random.randrange(1, 10)

match input("Calculating area. Choose the object (r-rectangle, t-triangle, с-circle): "):
    case 'r':
        print("Area of rectangle (sides: {}, {}) is {}".format(a, b, task08_31.rectangleArea(a, b)))
    case 't':
        print("Area of triangle (side and height: {}, {}) is {}".format(a, h, task08_31.triangleArea(a, h)))
    case 'c':
        print("Area of circle (radius {}) is {}".format(a, task08_31.circleArea(a)))

