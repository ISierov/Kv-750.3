try:
    number1, number2 = float(input('Please input 2 numbers:\nA = ')), \
                       float(input('B = '))
    result = [f'A + B = {number1 + number2}',
              f'A - B = {number1 - number2}',
              f'A * B = {number1 * number2}',
              f'A / B = {number1 / number2}',
              f'A ** B = {number1 ** number2}',
              f'A // B = {number1 // number2}',
              f'A % B = {number1 % number2}']
    [print(x) for x in result]
except ValueError:
    print('Please input only numbers')
