# Function that calculates number of characters included in given string

def char_num():
    st = input("Enter text: ")
    dct = {}
    for let in st:
        if let not in dct:
            dct[let] = st.count(let)
    print(dct)

char_num()


