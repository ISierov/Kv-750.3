import re

password = input("Enter password: ")

digits = re.findall("[0-9]", password)
lower = re.findall("[a-z]", password)
upper = re.findall("[A-Z]", password)
spec = re.findall("[@#$]", password)

if digits and lower and upper and spec and 6 <= len(password) <= 16:
  print("The password is valid")
else:
  print("The password is invalid")
