# A set for even numbers that are divisible by 2
even_div2 = set()
# A set for odd numbers that are divisible by 3
odd_div3 = set()
# A set for all numbers in range
full_range = set()
# A loop to determine numbers and fill our sets
for i in range(1, 11, 1):
    full_range.add(i)
    if i % 2 == 0:
        even_div2.add(i)
    elif i % 3 == 0:
        odd_div3.add(i)
# Output results
print("Even numbers that are divisible by 2:", sorted(even_div2))
print("Odd numbers that are divisible by 3:", sorted(odd_div3))
# Determining numbers that are not divisible by 2 and 3. Subtracting determined sets from full range of numbers
print("Numbers that are not divisible by 2 and 3:", sorted(full_range - even_div2 - odd_div3))
