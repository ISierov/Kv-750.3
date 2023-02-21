num = float(input("Enter the number: "))
num2 = num
fact = 1

while num2 > 0:
    fact *= num2
    num2 -= 1

print(f'{num}! = {fact}')
