fibonacci = [0,1]
n=int(input("Введите число\n"))
for i in range(2,n):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(fibonacci)