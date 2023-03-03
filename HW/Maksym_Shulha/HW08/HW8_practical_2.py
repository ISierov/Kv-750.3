# Program to check validity of password
import re


def pas_check():
    pas = input("Enter password: ")
    if 6 <= len(pas) <= 16 and \
            len(re.findall("[a-z]", pas)) >= 1 and \
            len(re.findall("[A-Z]", pas)) >= 1 and \
            len(re.findall("[0-9]", pas)) >= 1 and \
            len(re.findall("[!@#$%^&*()_+=]", pas)) >= 1:
        print("Password is valid")
    else:
        print("Invalid password")


pas_check()
