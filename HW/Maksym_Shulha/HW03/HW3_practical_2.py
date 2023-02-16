# Four digit natural number
number = 8936

# Product of the digits
product = 1
for i in range(0, len(str(number))):
    product *= int(str(number)[i])
print(f"The product of digits of the number {number} is {product}")

# Number in the reverse order
rev_num = int(str(number)[::-1])
print(f"Number {number} reversed is {rev_num}.")

# Sort numbers included in given number in ascending order
num_list = []
for i in range(0, len(str(number))):
    num_list.append(str(number)[i])
sort_num = ""
for digit in sorted(num_list):
    sort_num += digit
print(f"Number {number} with sorted digits gives {int(sort_num)}.")
