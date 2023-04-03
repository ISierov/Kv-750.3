from random import randint

secret_num = randint(1, 100)
a = 10

control = True

while control:
    your_num = int(input('Try to guess the number: '))
    if your_num == 0:
        print("You lose!")
        control = False
    if your_num == secret_num:
        print("You win!")
        control = False
    elif your_num > secret_num:
        print("The desired number is lesser. Try again: ")
        a -= 1
    elif your_num <= secret_num:
        print("The desired number is greater. Try again: ")
        a -= 1