import math

number = int(input('Please input the integer number more or equal 0: \nn = '))


def factorial(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


print(f'The factorial of number {number} is equal:', factorial(number))
#print(factorial(number) == math.factorial(number))



