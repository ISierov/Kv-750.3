def lettersCount(word):
    d = dict.fromkeys(word)
    for x in d:
        d[x] = word.count(x)
    return d

print(lettersCount(input("Calculating count of letters. Your word is ")))

