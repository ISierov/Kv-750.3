# Write a function that calculates the number of characters
# included in a given string

def string_counter(my_str):
    return {i: list(my_str).count(i) for i in my_str}

my_str = input('Enter a string: ')

print(string_counter(my_str))
