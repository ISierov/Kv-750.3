my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i = 0
while i < len(my_list):
    my_list[i] = float(my_list[i])
    i += 1

print(type(my_list[9]))