def circle_area(r):
    return r**2*3.14
def triangle_area(b,h):
    return b*h*0.5
def rect_area(a,b):
    return a*b

acct = input("What area do you whant to calculate : circle, triangle or rectangle?  \n")
match acct:
    case "circle":
        r = int(input("Input radius: \n"))
        print(f"Area = {circle_area(r)}")
    case "triangle":
        b = int(input("Input side: \n"))
        h = int(input("Input height: \n"))
        print(f"Area = {triangle_area(b,h)}")
    case "rectangle":
        a = int(input("Side a: \n"))
        b = int(input("Side b: \n"))
        print(f"Area = {rect_area(a,b)}")
    
