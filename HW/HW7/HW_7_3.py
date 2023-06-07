def count_characters(string):
    '''
    :param string: string
    :return: calculates the number of characters
included in a given string
    '''
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count