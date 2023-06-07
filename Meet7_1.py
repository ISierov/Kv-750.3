# import Meet7

# print(Meet7.fib2(10))
# Meet7.fib(10)
# print(Meet7.__name__)
#
# import Meet7
#
# fibo = Meet7.fib
#
# print(fibo(10))

# from Meet7 import fib, fib2 as fibo
#
# fib(10)
# print(fibo(10))

# import Meet7 as f
#
# f.fib(10)
#
# import Meet7
#
# print(dir(), Meet7.smth())

def myfunc():
    print('name:', __name__)

def main():
    myfunc()

if __name__ == '__main__':
    main()