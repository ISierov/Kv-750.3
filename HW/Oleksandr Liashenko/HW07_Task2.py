def s_rectangle(width, length):
    return width * length


def s_triangle(base, height):
    return base * height / 2


def s_circle(radius):
    return 3.14 * radius ** 2


print("Choose an object to calculate it\'s area:"
      "\n1. Rectangle"
      "\n2. Triangle"
      "\n3. Circle")


while True:
    figure = int(input("Enter a number of the figure: "))
    if figure == 1:
        print("Calculating area of the rectangle")
        rect_wid = int(input("Enter width: "))
        rect_len = int(input("Enter length: "))
        print("Area:", s_rectangle(rect_wid, rect_len))
        break
    elif figure == 2:
        print("Calculating area of the triangle")
        trian_b = int(input("Enter base: "))
        trian_h = int(input("Enter height: "))
        print("Area:", s_triangle(trian_b, trian_h))
        break
    elif figure == 3:
        print("Calculating area of the circle")
        circle_rad = int(input("Enter radius: "))
        print("Area:", s_circle(circle_rad))
        break
    else:
        print("\nEnter 1, 2 or 3")
        continue