# Python fundamentals 03
# Practical task 3

# Interchange the values of two variables without using the third variable.

number1 = 45
number2 = 97

print('Before interchanging:', number1, number2)

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

print('After interchanging:', number1, number2)