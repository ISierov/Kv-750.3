# Write a Python program to check the validity of a password (input from users).
import re

def validity(password):
    error_dict = []
    for key, value in error_var.items():
        if not re.search(key, password):
            error_dict.append(value)
    return error_dict

def result_print(result):
    if result:
        print('Password invalid. Found errors:')
        for i in result: print(i)
    else:
        print('Password valid')

password = input('Enter the password: ')

error_var = {
    '[a-z]': 'At least 1 letter between [a-z]',
    '[A-Z]': 'At least letter between [A-Z]',
    '\d': 'At least 1 number between [0-9]',
    '[$#@]': 'At least 1 character from [$#@]',
    '.{6,16}': 'Lenth 6-16 characters'
    }

result = validity(password)
result_print(result)