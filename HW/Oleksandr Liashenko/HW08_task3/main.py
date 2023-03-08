# This is the main module. The basic logic is executed here.

import calculation

figure = int(input("The area of figure do you want to calculate? \n1 - Rectangle \n2 - Triangle \n3 - Circle"
                   "\nEnter the number: "))

if figure == 1:
    side_a = int(input("Enter side a length: "))
    side_b = int(input("Enter side b length: "))
    print("Area:", calculation.s_rectangle(side_a, side_b))
elif figure == 2:
    height = int(input("Enter height: "))
    side_a = int(input("Enter side a length: "))
    print("Area:", calculation.s_triangle(height, side_a))
elif figure == 3:
    radius = int(input("Enter radius: "))
    print("Area:", round(calculation.s_circle(radius), 2))
