"""
You need to write a function that reverses the words in a given string.
A word can also fit an empty string.
"""
def reverseStr(sent):
    lst =  list(str(sent).split(' '))
    lst.reverse()

    return ' '.join(str(x) for x in lst)


print(reverseStr('World Hello'))
print(reverseStr('Hi There.'))


