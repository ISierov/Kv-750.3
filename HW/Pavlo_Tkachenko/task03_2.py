num = 3054
product = 1
list_num = list(map(int, str(num)))

print("The number is "+str(num))

for i in list_num:
    product *= i
print("  the product of the number is " + str(product))

list_num.reverse()
print("  reverse order of the number is " + ''.join(str(i) for i in list_num))

list_num.sort()
print("  ascending order is " + ''.join(str(i) for i in list_num))



