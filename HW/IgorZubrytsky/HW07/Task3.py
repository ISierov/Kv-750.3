def char_count(str_):
    str_=str_.lower()
    strset=set(str_)
    output = {}
    for i in range(len(strset)):
        count = 0
        tmpstr = strset.pop()
        for j in range(len(str_)):
            if str_[j] == tmpstr:
                count+=1
        output[tmpstr] = count
    return output

print (char_count("This is a simple string!!!"))