# In this module we define functions to calculate areas of the figures

from math import pi, pow


def s_rectangle(a, b):
    return a * b


def s_triangle(h, a):
    return 0.5 * h * a


def s_circle(r):
    return pi * pow(r, 2)
