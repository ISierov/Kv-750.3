"""
Create a function that takes a list and finds the list of integers that appear an odd number of times.
"""


def find_odd(lst: list):
    res = []
    for i in set(lst):
        if lst.count(i) % 2 != 0:
            res.append(i)
    return res


# print(find_odd([1, 1, 1, 2, 3, 3, 4, 5, 5]))


"""
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

Notes

Zero is a non-negative integer.
The given list only has integers and strings.
Numbers in the list should not repeat.
The original order must be maintained.
"""


def filter_list(lst):
    res = []
    for element in lst:
        if type(element) == int:
            res.append(element)
    return res


# print(filter_list([1, 2, 0.5, 0, '23']))


"""
Given a list of numbers, create a function which returns the list but with each element's index in the 
list added to itself. 
This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
"""


def add_indexes(lst: list):
    res = []
    for i in range(len(lst)):
        res.append(int(lst[i] + i))
    return res


# print(add_indexes([0, 0, 0, 0, 0]))


"""
Given an unsorted list, create a function that returns the nth smallest integer 
(the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).

Notes

n will always be >= 1.
Each number in the array will be distinct (there will be a clear ordering).
Given an out of bounds parameter (e.g. a list is of size k), 
and you are asked to find the m > k smallest integer, return None.
"""


def nth_smallest(lst: list, n: int):
    if n > len(lst):
        return None
    else:
        lst.sort()
    return lst[n-1]


# print(nth_smallest([1, 3, 5, 7], 5))


"""
Given a list of numbers and a value n, 
write a function that returns the probability of choosing a number greater than or equal to n from the list. 
The probability should be expressed as a percentage, rounded to one decimal place.

Notes. Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
"""


def probability(lst: list, num: int):
    count = 0
    for i in lst:
        if i >= num:
            count += 1
    res = 100 * count / len(lst)
    return round(res, 1)


print(probability([4, 6, 2, 9, 15, 18, 8, 2, 10, 8], 6))
