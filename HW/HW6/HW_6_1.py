even_nums = []
odd_nums = []
not_divis = []

for x in range(1, 11):
    if x % 2 == 0:
        even_nums.append(x)
    elif x % 3 == 0:
        odd_nums.append(x)

    if x % 2 != 0 and x % 3 != 0:
        not_divis.append(x)

print("Even numbers that are divisible by 2: ")
for num in even_nums:
    print(num, end=" ")

print("\nOdd numbers, which are divisible by 3: ")
for num in odd_nums:
    print(num, end=" ")

print("\nNumbers that are not divisible by 2 and 3: ")
for num in not_divis:
    print(num, end=" ")