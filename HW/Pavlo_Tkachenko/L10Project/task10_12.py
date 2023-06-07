class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"
    def species(self):
        return "Homosapiens"
    @staticmethod
    def arbitrary():
        return "Static method returns an arbitrary message"

me = Human("Flash")
print(me.welcome())
print(me.arbitrary())