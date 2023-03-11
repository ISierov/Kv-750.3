def rectangle_area(a: float, b: float):
    """
    The function calculates the area of a rectangle
    :param a: first (long) side of rectangle, type of number: float or integer
    :param b: second (short) side of rectangle, type of number: float or integer
    :return: area of rectangle, type of number: float or integer
    """
    return a * b


def triangle_area(a: float, h: float):
    """
    The function calculates the area of a triangle
    :param a: the base of triangle, type of number: float or integer
    :param h: the height of triangle, type of number: float or integer
    :return: area of triangle, type of number: float
    """
    return 1/2 * a * h


def circle_area(r: float):
    """
    The function calculates the area of a circle
    :param r: radius of circle, type of number: float
    :return: area of circle, type of number: float
    """
    return 3.14 * r**2


print('Area of a rectangle', rectangle_area(10, 3))
print('Area of a triangle', triangle_area(10, 5))
print('Area of a circle', circle_area(5))


