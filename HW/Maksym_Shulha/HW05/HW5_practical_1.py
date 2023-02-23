import random

# Create list with elements of integer type
int_list = [random.randint(0, 99) for i in range(6)]

# Change type of elements to float

# using list comprehension
# flt_list = [float(num) for num in int_list]

# using loop
flt_list = []
for num in int_list:
    flt_list.append(float(num))

print(flt_list)