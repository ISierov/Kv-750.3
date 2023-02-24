"""
Task 1
Create a list that contains elements of integer type, then use the loop to change the type of these elements
to a floating type
"""

arr_of_integer = [x for x in range(10)]
print('integer list:', *arr_of_integer)

arr_of_float = [float(y) for y in arr_of_integer]
print('float list:', *arr_of_float)


"""
Print Fibonacci numbers up to the entered number n
"""


def fibonacci(n: int) -> int:
    """
    Function that prints Fibonacci numbers up to n
    """
    numbers = [0, 1]
    if n == 0:
        return numbers[:1]
    elif n == 1:
        return numbers
    last_number = 0
    while last_number < n:
        last_number = numbers[-2] + numbers[-1]
        if last_number > n:
            break
        numbers.append(last_number)
    return numbers


print(fibonacci(2))
