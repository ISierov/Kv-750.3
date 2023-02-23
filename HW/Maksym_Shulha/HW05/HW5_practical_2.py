# Print Fibonacci numbers up to the entered number n using cycles.
n = int(input('Enter ending number of Fibonacci sequence: '))
fib = [0, 1]
if n == 0:
    fib = [0]
else:
    for i in range(1, 999):
        if fib[i - 1] + fib[i] > n:
            break
        fib.append(fib[i - 1] + fib[i])

print(fib)
