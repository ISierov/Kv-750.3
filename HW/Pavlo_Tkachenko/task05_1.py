list_int = list(range(5))

print("Origin list of int: " + str(list_int))

i = 0
while i < len(list_int):
    list_int[i] = float(list_int[i])
    i += 1

print("Result list of float: " + str(list_int))

