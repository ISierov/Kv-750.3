"""
You were camping with your friends far away from home, but when it's time to go back,
you realize that your fuel is running out and the nearest pump is 50 miles away!
You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return true if it is possible and false if not.
"""
def is_it_possible(miles, miles_gallon, left_galons):
    n = (miles/miles_gallon) - left_galons
    return n>0 or n==0

print(is_it_possible(50, 25, 2))
print(is_it_possible(50, 15, 2))
print(is_it_possible(30, 25, 4))


