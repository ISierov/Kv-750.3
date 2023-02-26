# Write a program that calculates the area of a rectangle, triangle
# and circle (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
PI = 3.14

def general_area(choise, a, b):
    match choise, a, b:
        case 1, a, b:
            print('Area of rectangle =', a * b)
        case 2, a, b:
            print('Area of triangle =', 0.5 * a * b)
        case 3, a, *b:
            print('Area of circle =', PI * a ** 2)

choice = int(input(""" 
    1 - calculate area of of a rectangle
    2 - calculate area of of a triangle
    3 - calculate area of of a circle
    Your choice: """))

if choice == 1:
    a = float(input('Enter first side of rectangle: '))
    b = float(input('Enter second side of rectangle: '))
    general_area(choice, a, b)
elif choice == 2:
    a = float(input('Enter side of triangle: '))
    b = float(input('Enter height of triangle: '))
    general_area(choice, a, b)
elif choice == 3:
    a = float(input('Enter radius of circle: '))
    general_area(choice, a, b = 0)
