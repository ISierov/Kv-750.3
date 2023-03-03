from formulas import *


def area():
    fig = input("""Select figure, to calculate its area
(1 - rectangle, 2 - triangle, 3 - circle): """)
    match fig:
        case "1":
            rect_area()
        case "2":
            tri_area()
        case "3":
            cir_area()
        case _:
            print("Enter correct figure index")
            area()


area()
