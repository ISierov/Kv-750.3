# in the range from 1 to 10 determine
# even numbers divisible by 2
# odd numbers divisible by 3
# numbers not divisible by 2 and 3

div_2 = []
div_3 = []
others = []
for num in range(1,10):
    if num % 2 == 0:
        div_2.append(num)
    elif num % 2 != 0 and num % 3 == 0:
        div_3.append(num)
    else:
        others.append(num)

print(f"""
Even numbers divisible by 2: {div_2}
Odd numbers divisible by 3: {div_3}
Numbers not divisible by 2 and 3: {others}
""")

