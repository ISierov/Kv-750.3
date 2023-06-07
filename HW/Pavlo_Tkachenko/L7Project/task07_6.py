'''
Write a function taking in a string like [WOW this is REALLY          amazing]
and returning Wow this is really amazing. String should be capitalized and properly spaced. 
Using [re] and [string] is not allowed.
'''
def no_yelling(sent):
    dct = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    cnt = 0
    lst = list(sent)
    print()
    if lst[0] in dct.keys():
        res = list(lst[0])
    else:
        res = list(list(dct.keys())[list(dct.values()).index(lst[0])])

    for i in range(1, len(lst)):
        if lst[i] in dct.keys():
            res.extend(dct[lst[i]])
            cnt = 0
        elif lst[i] in " " and cnt == 0:
            res.extend(lst[i])
            cnt = 1
        elif lst[i] in " " and cnt == 1:
            pass
        else:
            res.extend(lst[i])
            cnt = 0

    return ''.join(str(x) for x in res)

print(no_yelling("WOW this is REALLY          amazing"))
print(no_yelling("THAT was EXTRAORDINARY!"))
print(no_yelling('now THIS is REALLY interesting    4 you'))




