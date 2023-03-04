# Write a program that calculates the area of a rectangle S=a*b, the area of a triangle S=0.5*h*a,
# the area of a circle S=pi*r**2. This module must be used in another module in which we ask the user
# the area of which figure he wants to calculate.
# (To perform the task, you need to import the math module, and from it the
# pow() function and the value of the variable pi, and module, which contains
# three functions for finding areas, into the main program. The basic logic of the
# program is executed in the main module).

import calculation

choice = int(input(""" Calculate area of
    1 - rectangle, 2 - triangle, 3 - circle
    Your choice: """))

if choice == 1:
    a = float(input('Enter first side of rectangle: '))
    b = float(input('Enter second side of rectangle: '))
    calculation.rectangle(a, b)
elif choice == 2:
    a = float(input('Enter side of triangle: '))
    b = float(input('Enter height of triangle: '))
    calculation.triangle(a, b)
elif choice == 3:
    a = float(input('Enter radius of circle: '))
    calculation.circle(a)
