def print_message(data):
    print('Info:', data)
    return
def fib(n):             # write Fibonacci series up to n
    a, b = 1, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):            # return Fibonacci series up to n
    result = []
    a, b =1, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    def smth():
        print('smth')

    from Meet7_1 import main
    main()