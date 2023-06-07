import random


num = random.randint(1,100)
print('try to guess the number from 1 to 100 by less then 10 attempts')
for i in range(10):
    pnum = int(input(f" Attempt {i+1}. Input number:\n"))
    if pnum == num:
        print(f'Congrats! You guessed the number by {i+1} attempts')
        break
    elif pnum > num:
        print('The number is less')
    elif pnum < num:
        print('The number is greater')
    if i == 9:
        print (f"You reached max number of attempts {i+1}. Try again (((")
