# Task2. Create a class Human, everyone has a name, create a method in the class that displays a
# welcome message to each person. Create a class method in the class that returns information that it
# is a species of "Homosapiens". And in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}')

    @classmethod
    def specie_info(cls):
        print(f'Class method. Species of "Homosapiens"')

    @staticmethod
    def message():
        print('Static method called')

man = Human('Gizmo')
man.greeting()
Human.specie_info()
Human.message()


