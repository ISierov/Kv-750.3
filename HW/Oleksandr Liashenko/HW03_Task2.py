# Given 4-digit number
number = 2649
# Converting it to string
num_str = str(number)
# Finding every digit of the given number
d0 = int(num_str[0])
d1 = int(num_str[1])
d2 = int(num_str[2])
d3 = int(num_str[3])
# Product
print("Product =", d0 * d1 * d2 * d3)
# Given number in reverse order
print("Number in reverse order:", num_str[3] + num_str[2] + num_str[1] + num_str[0])
# Creating a list to sort digits
num_list = [d0, d1, d2, d3]
# Printing sorted digits included in the given number
print(sorted(num_list))
