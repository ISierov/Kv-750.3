# list int to float

print([float(i) for i in list(range(5))])


# Fibonacchi sequence, using cycles

fib_past = 0
fib_present = 1
fib_range = int(input('Enter number of digits of Fibonacci sequence: '))
if fib_range == 0:
    print('Nothing to calculate')
elif fib_range == 1:
    print(fib_past, end=' ')
else:
    print(fib_past, fib_present, end=' ')
    for i in range(2, fib_range):
        fib_past, fib_present = fib_present, fib_past + fib_present
        print(fib_present, end=' ')
