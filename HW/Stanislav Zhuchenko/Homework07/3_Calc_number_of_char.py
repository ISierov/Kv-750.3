def number_of_char(string: str):
    """
    The function calculates the number of chars in string
    :param string:
    :return: dictionary where keys are chars from the string and values is the quantity char in the string
    """
    d = dict()
    for ch in string:
        d.update({ch: string.count(ch)})
    return d


print(number_of_char('hello'))
print(number_of_char('SoftServe Academy'))
