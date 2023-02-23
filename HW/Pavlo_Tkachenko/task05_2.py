# task to calc factorial input number
num = int(input("Calculating Fibonacci numbers.\n Up to number: "))

res = [0, 1]

if num > 0:
    i = 1
    while True:
        append_num = res[i-1] + res[i]
        if append_num>num:
            break
        res.append(append_num)
        i += 1
else:
    res = [0]

print(res)



