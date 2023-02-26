div2 = []
odd_div3 = []
non_div = []
for i in range(1,10):
    if i%2 == 0 :
        div2.append(i)
    elif  i%3 == 0 and i%2 != 0:
        odd_div3.append(i)
    else :
        non_div.append(i)    

print (f"Even divisible by 2:\n{div2}")
print (f"Odd divisible by 3:\n{odd_div3}")
print (f"Not divisible by 2 & 3:\n{non_div}")