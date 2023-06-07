class Human:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}")

    @classmethod
    def species(self):
        return "Homosapiens"

    @staticmethod
    def arb_message():
        print("arbitrary message")





