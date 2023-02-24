res2 = []
res3 = []
res0 = []

for x in range(1, 11, 1):
    if x % 2 == 0:
        res2.append(x)
    elif x % 3 == 0:
        res3.append(x)
    else:
        res0.append(x)

print("Even numbers:")
print(res2)
print("Odd numbers:")
print(res3)
print("Numbers are not divisible by 2 or 3:")
print(res0)


