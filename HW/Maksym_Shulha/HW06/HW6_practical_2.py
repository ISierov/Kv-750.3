# If login is "First" greet the user, if different, send error message
valid = ["First"]
login = input("Enter login: ")
while login not in valid:
    login = input("Incorrect login, try again: ")
print(f"Hello, {login}")