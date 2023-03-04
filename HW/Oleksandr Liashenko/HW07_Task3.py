word = input("Enter word: ")
result = dict()
for i in word:
    dictionary = dict.fromkeys(i, word.count(i))
    result.update(dictionary)

print(result)
