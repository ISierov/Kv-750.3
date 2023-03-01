# Function that returns largest numbers of two

def largest(a, b):
    """
    Returns largest of two numbers
    :param a: int or float, first number
    :param b: int or float, second number
    :return: str stating the largest number
    """
    return f"Largest number is: {max(a, b)}"

print(largest(10.49, 10.5))