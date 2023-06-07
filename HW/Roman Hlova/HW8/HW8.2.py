import re

password = input("enter your password: ")

if re.search('[a-z]', password) and\
  re.search('[A-Z]', password) and\
  re.search('[$#@]', password) and\
  len(password) > 5 and\
  len(password) < 17:
    print("The password is valid")
else:
    print("ERORR invalid password !!!")
    

    
