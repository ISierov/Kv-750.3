"""
Jenny's secret message

Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different.
She added a special case to her function, but she made a mistake.
"""
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)
#
# print(greet("Johnny"))


"""
Find The Distance Between Two Points

Given two ordered pairs calculate the distance between them. Round to two decimal places. 
This should be easy to do in 0(1) timing.
"""
# def distance(x1, y1, x2, y2):
#     return round(((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)), 2)
#
# print(distance(4, 6, 11, 33))


"""
No yelling!

Write a function taking in a string like "WOW this is REALLY          amazing" 
and returning "Wow this is really amazing".
String should be capitalized and properly spaced. Using re and string is not allowed.
"""
# def filter_words(st):
#     return ' '.join(st.capitalize().split())
# print(filter_words("WOW this is REALLY          amazing"))


"""
Convert a Number to a String!

We need a function that can transform a number (integer) into a string.
"""
# def number_to_string(num):
#     return str(num)


"""
Reversing Words in a String

You need to write a function that reverses the words in a given string. 
"""
# def reverse(st):
#     lst = st.split()
#     lst.reverse()
#     return " ".join(lst)
# print(reverse("Hello World"))


"""
Reverse List Order

In this kata you will create a function that takes in a list and returns a list with the reverse order.
"""
# def reverse_list(l):
#     l.reverse()
#     return l
# print(reverse_list([1, 2, 3, 4]))


"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
"""
# def solution(number):
#     total = 0
#     for a in range(number):
#         if a % 3 == 0 or a % 5 == 0:
#             total += a
#     return total
# print(solution(500))

"""
Will you make it?

You were camping with your friends far away from home, but when it's time to go back, 
you realize that your fuel is running out and the nearest pump is 50 miles away! 
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.
"""
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left
# print(zero_fuel(50, 25, 2))


"""
Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!
"""
# def are_you_playing_banjo(name):
#     if name.lower()[0] == 'r':
#         return f"{name} plays banjo"
#     return f"{name} does not play banjo"
# print(are_you_playing_banjo("ron"))


"""
Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     elif boolean == False:
#         return "No"
# print(bool_to_word(False))


"""
Counting sheep...
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).
"""
# def count_sheeps(sheep):
#     return sheep.count(True)


"""
Is this my tail?

Some new animals have arrived at the zoo. 
The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
If the tail is right return true, else return false.
"""
# def correct_tail(body, tail):
#     return body[-1] == tail
