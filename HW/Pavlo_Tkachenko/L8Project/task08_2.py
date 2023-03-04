"""
to check validity of password
"""
import re

def validate_pass(word):
    return (bool(re.search(r'\d', word)) and bool(re.search('[a-z]', word)) and
        bool(re.search('[A-Z]', word)) and
        bool(re.search('[@#$]', word)) and
        len(word) > 5 and len(word) < 17)

attempts = 5
print("Validate your password. You have {} attempts.".format(attempts))
for i in range(attempts):
    if validate_pass(input(str(i+1) + ". Your password is ")):
        print("Password is valid")
        break





