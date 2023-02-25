# Getting a number
number = input("Enter a number: ")
# Defining first two numbers of Fibonacci sequence
x, y = 0, 1
# Declaring a list ot write the sequence in
Fibo = [x, y]
# A loop which calculates next number of the sequence and while result is less than previously inputted number
while Fibo[x]+Fibo[y] < int(number):
    Fibo.append(Fibo[x]+Fibo[y])
    x += 1
    y += 1
# Outputs result
print(Fibo)