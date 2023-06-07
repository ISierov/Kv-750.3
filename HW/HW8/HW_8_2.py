import re

password = input("Enter a password: ")
tests = []

if len(password) < 6 or len(password) > 16:
    print("Password length should be between 6 and 16 characters")
else:
    if not re.search("[a-z]", password):
        print("Password should contain at least 1 lowercase letter")
        tests.append(False)
    else:
        tests.append(True)
    if not re.search("[A-Z]", password):
        print("Password should contain at least 1 uppercase letter")
        tests.append(False)
    else:
        tests.append(True)
    if not re.search("[0-9]", password):
        print("Password should contain at least 1 number")
        tests.append(False)
    else:
        tests.append(True)
    if not re.search("[$#@]", password):
        print("Password should contain at least 1 special character ($#@)")
        tests.append(False)
    else:
        tests.append(True)
    if all(tests):
        print(f"Password {password} is valid")