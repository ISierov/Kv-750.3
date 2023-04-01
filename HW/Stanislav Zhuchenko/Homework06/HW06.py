"""
Task 1
In the range from 1 to 10 determine:
- even numbers that are divisible by 2;
- odd numbers, which are divisible by 3;
- numbers that are not divisible by 2 and 3.
"""


def task1():
    even_numbers = []
    odd_numbers = []
    other_numbers = []
    for x in range(1, 11):
        if x % 2 == 0:
            even_numbers.append(x)
        if x % 3 == 0:
            odd_numbers.append(x)
        if x % 2 != 0 and x % 3 != 0:
            other_numbers.append(x)
    results = f'even numbers: {even_numbers}\nodd_numbers: {odd_numbers}\nother_numbers: {other_numbers}'
    return results


# print(task1())


"""
Task 2
Write a script that checks thw login that the user enters. If the login is "First", then greet the users.
If the login is different, send an error message.
"""


def login():
    name = input('Login: ')
    while name != 'First':
        print('Unknown login, please try again')
        name = input('Login: ')
    else:
        return f'Hello, {name}!'


print(login())
