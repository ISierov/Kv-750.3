## Task2
# Let x be a given number
x = 5312
print("number =",x)

#  sum of the digits of this number
x1 = str(x)

n1 = int(x1[0])
n2 = int(x1[1])
n3 = int(x1[2])
n4 = int(x1[3])

summ = n1 + n2 + n3 + n4
print("sum of the digits of this number =",summ)

# reverse order
reverse = int(x1[::-1])
print ("reverse order of number:",reverse)

#sort the numbers
sort_min_max = ''.join(sorted(x1))
print("sort the numbers min-max:",sort_min_max)

## Task3
#changing the value of two variables without using a third variable.

a = 3
b = 7
print('a=',a)
print('b=',b)

a = a + b
b = a - b
a = a - b

print('a=',a)
print('b=',b)

