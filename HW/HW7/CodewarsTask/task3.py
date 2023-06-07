'''
Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing.
String should be capitalized and properly spaced. Using re and string is not allowed.
'''


def clean_string(sentence):
    words = sentence.split()

    for i in range(1, len(words)):
        words[i] = words[i].lower()

    words[0] = words[0].capitalize()

    return " ".join(words)