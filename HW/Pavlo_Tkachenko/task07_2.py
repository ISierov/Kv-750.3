import math
import random

def rectangleArea(a, b):
    return a*b

def triangleArea(a, b, c):
    s = (a+b+c)/2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)

def circleArea(r):
    return round(math.pi*r**2, 2)

a = random.randrange(1, 10)
b = random.randrange(1, 10)
c = random.randrange(1, 10)

match input("Calculating area. Choose the object (r-rectangle, t-triangle, с-circle): "):
    case 'r':
        print("Area of rectangle (sides: {}, {}) is {}".format(a, b, rectangleArea(a, b)))
    case 't':
        print("Area of triangle (sides: {}, {}, {}) is {}".format(a, b, c, triangleArea(a, b, c)))
    case 'c':
        print("Area of circle (radius {}) is {}".format(a, circleArea(a)))




