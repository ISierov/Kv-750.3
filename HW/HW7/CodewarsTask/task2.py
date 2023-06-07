'''
Given two ordered pairs calculate the distance between them. Round to two decimal places.
This should be easy to do in 0(1) timing.
'''
import cmath
def distance(x1, y1, x2, y2):
    x_distance = abs(x2) - abs(x1)
    y_distance = abs(y2) - abs(y1)
    distance = (x_distance**2) + (y_distance**2)
    return cmath.sqrt(distance)
