import re


def check_password(password: str) -> str:
    """
    The function to check the validity of password
    :param password: string, length minimum 6, maximum 16 symbols. Required minimum 1 number, 1 letter in lowercase and
    1 letter in uppercase.
    :return: string, if the conditions are true - 'Password is valid', if false - an error about what is going wrong
    """
    patterns_errors = {'[$#@]': 'Password required minimum 1 symbol from $#@',
                       '[\d]': 'Password required minimum 1 number between 0-9',
                       '[a-z]': 'Password required minimum 1 lowercase letter',
                       '[A-Z]': 'Password required minimum 1 uppercase letter'
                       }
    if not 6 <= len(password) <= 16:
        return 'minimum len 6, maximum len 16'
    for pattern in patterns_errors:
        if re.search(pattern, password) is None:
            return patterns_errors[pattern]
    return 'Password is valid'


pssword = input('Password: ')
print(check_password(pssword))
