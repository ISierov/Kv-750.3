#_______Task1. In the range from 1 to 10 determine 
print("____Task1____")

even_2 = []
odd_3 = []
not_div_2_3 = []

for i in range(1,10):
    if i % 2 == 0 :
        even_2.append(i)
    if i % 3 == 0 and i % 2 != 0:
        odd_3.append(i)
    if i % 3 != 0 and i % 2 != 0:
        not_div_2_3.append(i)

print ("Even numbers that are divisible by 2  ===> ", even_2)
print ("Odd numbers, which are divisible by 3  ===> ", odd_3)
print ("Numbers that are not divisible by 2 and 3  ===> ", not_div_2_3)


#_____Task2. Write a script that checks the login that the user enters
print("____Task2____")

login = "First"

while True:

    entered_login = input("Enter your login: ")
    
    if login == entered_login:
        print("Entered login is correct, Welcome back!!!")
        break
    else:
        print("Error!!! (entered login does not exist) \nTry again")