from random import randint


class Ghost(object):
    def __init__(self):
        c = {1: 'white', 2: 'yellow', 3: 'purple', 4: 'red'}
        self.color = c[randint(1, 4)]

    def color(self):
        self.color()


ghost = Ghost()
print(ghost.color)
