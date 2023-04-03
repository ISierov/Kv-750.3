import calc


while True:

    choice = input("  The area of what you want to calculate? \n   ENTER: \
        \n  '1' for rectangle \n  '2' for triangle \n  '3' for circle \
        \n  or any symbol for exit\n")

    if choice == '1':
        a = float(input("enter a:\n"))
        b = float(input("enter b:\n"))
        print("area is: ", calc.rectangle_area(a,b))
    elif choice == '2':
        a = float(input("enter a:\n"))
        h = float(input("enter h:\n"))
        print("area is: ", calc.triangle_area(a , h))
    elif choice == '3':
        r = float(input("enter r:\n"))
        print("area is: ", calc.circle_area(r))
    else:
        break