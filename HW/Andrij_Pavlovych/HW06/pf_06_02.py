# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

desire_login = list('First')
user_login = list(input('Enter the login: '))

while desire_login:
    if desire_login[0] == user_login[0]:
        del desire_login[0]
        del user_login[0]
    else:
        print('Error, incorrect login')
        break
else:
    print('Login aacepted')
