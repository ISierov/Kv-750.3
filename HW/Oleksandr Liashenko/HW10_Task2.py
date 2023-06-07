class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}")

    def species(self):
        print(f"{self.name} belongs to the species of Homo Sapiens")

    @staticmethod
    def message():
        print("Just a message")


person = Human("Oleksandr")
person.welcome()
person.species()
person.message()