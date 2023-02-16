# Python fundamentals 03
# Practical task 2

number = input('Enter a four-digit natural number: ')

# the product of the digits of this number:
print('The product is', eval('*'.join(list(number))))

# write the number in reverse order
print('Reverse order is', number[::-1])

# sort the numbers included in the given number
print('Sorted digits is', ''.join(sorted(number)))