#___Task 3 

def letter_calculator(word):

    d = dict.fromkeys(word)
    
    print(d)
    for key in d.keys():
        d[key] = word.count(key)
    return d
