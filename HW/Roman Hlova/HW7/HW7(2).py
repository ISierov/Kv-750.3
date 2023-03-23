#___Task 2

def rectangle_area(a, b):
    return a*b

def triangle_area(a , h):
    return 1/2 * a * h

def circle_area(r):
    return 3.14 * r**2

while True:

    choice = input("  The area of what you want to calculate? \n   ENTER: \
        \n  '1' for rectangle \n  '2' for triangle \n  '3' for circle \
        \n  or any symbol for exit\n")

    if choice == '1':
        a = float(input("enter a:\n"))
        b = float(input("enter b:\n"))
        print("area is: ",rectangle_area(a,b))
    elif choice == '2':
        a = float(input("enter a:\n"))
        h = float(input("enter h:\n"))
        print("area is: ",triangle_area(a , h))
    elif choice == '3':
        r = float(input("enter r:\n"))
        print("area is: ",circle_area(r))
    else:
        break
    