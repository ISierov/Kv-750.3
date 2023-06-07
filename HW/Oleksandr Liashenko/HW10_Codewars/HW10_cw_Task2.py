# Color Ghost
#
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

from random import randint


class Ghost:
    def __init__(self):
        Ghost.color = ("white", "yellow", "purple", "red")[randint(0, 3)]
        print(Ghost.color)


ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
