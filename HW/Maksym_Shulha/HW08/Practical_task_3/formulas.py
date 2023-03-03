import math


def rect_area():
    ln = float(input('Enter rectangle length: '))
    wid = float(input('Enter rectangle width: '))
    print(f"Rectangle area is: {round(ln * wid, 2)}")


def tri_area():
    height = float(input('Enter triangle height: '))
    base = float(input('Enter triangle base: '))
    print(f"Triangle area is: {round((height * base) / 2, 2)}")


def cir_area():
    r = float(input('Enter circle radius: '))
    print(f"Circle area is: {round(math.pi * math.pow(r, 2), 2)}")
