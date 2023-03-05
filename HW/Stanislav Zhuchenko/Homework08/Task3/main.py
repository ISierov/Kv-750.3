from funcionsfile import rectangle_area as rectangle, triangle_area as triangle, circle_area as circle

text = '''Please choice the figure what the area you want to calculate and enter the number:
1 - area of a rectangle
2 - area of a triangle
3 - area of a circle
>>> '''


inpt = input(text)
match inpt:
    case '1':
        print('Enter parameters of a rectangle:')
        param_a, param_b = input('a: '), input('b: ')
        print(rectangle(float(param_a), float(param_b)))
    case '2':
        print('Enter parameters of a triangle:')
        param_a, param_b = input('base: '), input('height: ')
        print(triangle(float(param_a), float(param_b)))
    case '3':
        print('Enter parameter of a circle:')
        param_a = input('radius: ')
        print(circle(float(param_a)))
    case _:
        print('Please enter valid number from 1 to 3')
