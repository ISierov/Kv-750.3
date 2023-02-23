# I couldn't do it without recursion.

# Solution 1. Cheating :)
# import math
# number = int(input("Enter number: "))
# print(math.factorial(number))

# Solution 2. With recursion
number = int(input("Enter a number: "))
result = 1
for i in range(1, number + 1, 1):
    result *= i
print(result)