import Square as s
print(dir())
o = input("input figure : circle - 1, triangle - 2, rectangle - 3 \n")
match int(o):
    case 1:
        r = input("Input radius \n")
        print(f'Square = ', s.circle(r))
    case 2:
        a = input("Input side \n")
        h = input("Input height \n")
        print(f'Square = ', s.tri(h, a))
    case 3:
        a = input("Input sides a  \n")
        b = input("Input sides b \n")
        print(f'Square = ', s.rect(a, b))
