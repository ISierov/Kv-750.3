# Program that calculates area of selected figure

def rect_area():
    len = float(input('Enter rectangle length: '))
    wid = float(input('Enter rectangle width: '))
    print(f"Rectangle area is: {len * wid}")

def tri_area():
    height = float(input('Enter triangle height: '))
    base = float(input('Enter triangle base: '))
    print(f"Triangle area is: {(height * base) / 2}")

def cir_area(pi = 3.14):
    r = float(input('Enter circle radius: '))
    print(f"Circle area is: {pi * r ** 2}")

def area():
    figure = input("""Enter the name of figure, to calculate its area
(rectangle, triangle or circle): """)
    if figure.lower() == "rectangle":
        rect_area()
    elif figure.lower() == "triangle":
        tri_area()
    elif figure.lower() == "circle":
        cir_area()
    else:
        print("Incorrect figure name")
        area()

area()