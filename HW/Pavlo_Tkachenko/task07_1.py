import random

def largeNum(num1, num2):
    '''
    Return the larger number of 2 numbers
    :parameter num1: 1st number
    :parameter num2: 2st number
    :return: (int) larger number
    '''
    if num1>num2:
        return num1
    else:
        return num2

num1 = random.randrange(1000)
num2 = random.randrange(1000)

print('Given 2 numbers: {}, {}. The largest one is {}'.format(num1, num2, largeNum(num1,num2)))

