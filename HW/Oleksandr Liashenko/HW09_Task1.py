from random import randint

rand_num = randint(1, 100)
tries = 10

while tries > 0:
    usr_num = int(input(f"Enter a number ({tries} left): "))
    if usr_num == rand_num:
        print("Congratulations!")
        break
    elif tries == 1:
        print("Game over")
        break
    elif usr_num < rand_num:
        print("Try a greater number")
    elif usr_num > rand_num:
        print("Try a lesser number")
    tries -= 1


