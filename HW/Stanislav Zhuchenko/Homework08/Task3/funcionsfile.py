from math import pow, pi


def rectangle_area(a: float, b: float):
    """
    The function calculates the area of a rectangle
    :param a: first (long) side of rectangle, type of number: float or integer
    :param b: second (short) side of rectangle, type of number: float or integer
    :return: area of rectangle, type of number: float or integer
    """
    return a * b


def triangle_area(base: float, h: float):
    """
    The function calculates the area of a triangle
    :param base: the base of triangle, type of number: float or integer
    :param h: the height of triangle, type of number: float or integer
    :return: area of triangle, type of number: float
    """
    return 1/2 * base * h


def circle_area(r: float):
    """
    The function calculates the area of a circle
    :param r: radius of circle, type of number: float
    :return: area of circle, type of number: float
    """
    return round(pi, 2) * pow(r, 2)
