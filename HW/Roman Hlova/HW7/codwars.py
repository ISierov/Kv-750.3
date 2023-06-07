# ----- 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# ----- 2

def distance(x1, y1, x2, y2):
    a = pow((pow((x2-x1),2)+pow((y2-y1),2)),(1/2))
    return round(a,2)

# ------ 3 

def filter_words(st):
    return ' '.join(st.capitalize().split())


# ----- 4 

def number_to_string(num):
    return str(num)

# ----- 5 

def reverse(st):
    return ' '.join(reversed(st.split()))

# ----- 6 

def reverse_list(l):
    return l[::-1]

# ----- 7 

def solution(number):
    y = {0}                      
    for x in range(0,number,3):
        y.add(x)
    for x in range(0,number,5):
        y.add(x)
    return sum(y)

# ----- 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False

# ----- 9

def are_you_playing_banjo(name):
    if name[0] == 'r' or 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# ----- 10

def bool_to_word(boolean):
    match boolean:
        case True:
            return "Yes"
        case False:
            return "No"
        case _:
            pass

# ----- 11

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count+=1
    return count

# ----- 12

def correct_tail(body, tail):
    return True if body[-1] == tail else False

