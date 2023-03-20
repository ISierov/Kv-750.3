'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:
'''

def banjo(name):
    if name.upper()[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"