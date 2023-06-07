n = int(input("enter number: "))
fibonachi_nums = [0, 1]

i = 0
while i < n:
    next = fibonachi_nums[-1] + fibonachi_nums[-2]
    fibonachi_nums.append(next)
    i += 1

for num in fibonachi_nums:
    print(num)