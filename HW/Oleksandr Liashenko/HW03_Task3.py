# Interchange the values of two variables without creating a new variable

a = 1
b = 3

print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b


print("new a =", a)
print("new b =", b)