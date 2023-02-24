# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

x = [i for i in range(1, 11)]
even_div2 = []
odd_div3 = []
others = []
while x:
    match x:
        case [i, *wtv] if not i % 2:
            even_div2.append(x.pop(0))
        case [i, *wtv] if not i % 3:
            odd_div3.append(x.pop(0))
        case _:
            others.append(x.pop(0))

print('Even divisible by 2:', even_div2)
print('Odd divisible by 3:', odd_div3)
print('Others:', others)