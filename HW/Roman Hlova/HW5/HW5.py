# _________________Task 1

#list int
a = [10, 2, 3 , 4, 5]
print(a)

for i in range(0, len(a)): 
    a[i] = float(a[i])
    
#list float
print(a)



# _________________Task 2
              # Fibonacci numbers

numb =int(input("Enter nunmer:"))
F = [0, 1, 1]

if numb == 0:
    print(F[:1])
elif numb ==1:
    print(F[:2])
else:

    while F[-1] < numb:
        fibo = F[-1] + F[-2]
        F.append(fibo)

    if numb not in F:
        print (f"The entered number is not included \"Fibonacci Sequence\" of integer. \
             \n Nearest number is {F[-1]},\
             \n {F}")
    else:
        print(F)