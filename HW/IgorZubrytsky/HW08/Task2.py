import re


def Valid(pas):
    if len(pas) < 6 and len(pas) > 16:
        return False
    if re.search("[A-Z]", pas) == None:
        return False
    elif re.search("[a-z]", pas) == None:
        return False
    elif re.search(".[0-9].", pas) == None:
        return False
    elif re.search(".[@$#].", pas) == None:
        return False
    return True


pas = ''
while True:
    pas = input("Input pass:\n")
    if pas == 'exit':
        break
    print('Valid Password ' if Valid(pas) == True else 'Password Invalid')
