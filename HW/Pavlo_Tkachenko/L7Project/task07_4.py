"""
Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different.
She added a special case to her function, but she made a mistake.
"""
import math
import string

def greetUser(user):
    if user == 'Johnny':
        return "Welcome, nice Johnny"
    else:
        return "Welcome, "+user

print(greetUser(input("Your name is ")))

