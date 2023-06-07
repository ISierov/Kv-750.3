
number = "5813"
multiplication = int(number[0])*int(number[1])*int(number[2])*int(number[3])
print(f"Number = {number}")
print(f"Production of digits = {multiplication}")
print(f"Reverse = {number[::-1]}")
sorted_chars = sorted(number)
number = ''.join(sorted_chars)
print(f"Sorted - {number}")