# task to calc factorial input number
num = int(input("Calculate factorial.\n Number is "))
res = 1
for i in range(1, num+1, 1):
    res = res*i

print(res)
