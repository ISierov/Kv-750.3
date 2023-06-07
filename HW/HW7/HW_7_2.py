import math

def rectangle(a = 0, b = 0):
    '''
    :param a:side a
    :param b:side b
    :return: the area of the rectangle
    '''
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    return a * b

def triangle(a = 0, h = 0):
    '''
    :param a: side a
    :param h: height of the triangle
    :return: the area of the triangle
    '''
    a = int(input("Enter side a: "))
    h = int(input("Enter height of the triangle: "))
    return a/2 * h

def circle(r = 0):
    '''
    :param r: circle radius
    :return:the area of the circle
    '''
    r = int(input("Enter radius: "))
    return math.pi * r ** 2

figure = input("Enter figure(rectangle, triangle, circle) for calculate the area: ")

if figure == "rectangle":
    print(rectangle())
elif figure == "triangle":
    print(triangle())
elif figure == "circle":
    print(circle())