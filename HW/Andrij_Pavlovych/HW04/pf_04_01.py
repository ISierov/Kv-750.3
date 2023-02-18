# factorial of the entered number without using recursion

number = int(input('Enter a positive number: '))
factorial = 1

# avoid intermediate variable
print(f'Factorial of {number} is ', end='')

# practice in match case
while True:
    match number:
        case 0 | 1:
            print(factorial)
            break
        case _:
            factorial = factorial * number
            number = number - 1
