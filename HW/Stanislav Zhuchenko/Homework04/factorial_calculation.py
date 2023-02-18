import math

number = int(input('Please input the integer number more or equal 0: \nn = '))


def factorial(int: number):
    res = 1
    for i in range(1, number+1):
        res *= i
    return res


print(f'The factorial of number {number} is equal:', factorial(number))
#print(factorial(number) == math.factorial(number))



