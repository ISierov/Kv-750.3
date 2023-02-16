import random


# 1 task
zenOfPython = """The Zen of Python, by Tim Peters

1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
"""

# Count the number of occurrences 'better', 'never', 'is' in the zenOfPython
words = ['better', 'never', 'is']
for word in words:
    print(f'The number of occurrences of the word "{word}":', zenOfPython.count(word))

# Convert all text to uppercase
print(zenOfPython.upper())

# Replace "i" to "&"
print(zenOfPython.replace('i', '&'))


# 2 task
number = random.randint(1000, 9999)
print('The 4-digit number =', number)

# Find the product of the digits of this number
product = 1
for num in str(number):
    product *= int(num)
print(f'The product of the digits of this number = {product}')

# Write the number in reverse order
print('The number in reverse order:', str(number)[::-1])

# The number in ascending order
print('The number in ascending order:', ''.join(sorted(str(number))))


# 3 task
# Interchange the values of 2 variables without using the third variable
a = 1
b = 2
print(f'Before: a = {a}, b = {b}')
a, b = b, a
print(f'After: a = {a}, b = {b}')
