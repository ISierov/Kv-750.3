"""
Create a class Human, everyone has a name, create a method in the class that displays a wellcome message to each person.
Create a class method in the class that returns info that it is a species of "Homosapiens".
And in the class create a static method that returns an arbitrary message.
"""


class Human:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f'You are welcome {self.name}'

    @classmethod
    def species(cls):
        return 'Human is a species of "Homosapiens"'

    @staticmethod
    def message(message='Hi to everybody'):
        return message


firstPerson = Human('Stas')
print(firstPerson.welcome())
print(Human.species())

print(Human.message('Hello friends'))
print(Human.message())

