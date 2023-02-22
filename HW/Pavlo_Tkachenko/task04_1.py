num = int(input("Calculate factorial.\nThe number is "))
res = 1
for i in range(1, num+1, 1):
    res = res*i

print(res)
