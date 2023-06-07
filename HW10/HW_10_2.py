class Human:
    spec = "homo sapiens"

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}")

    @classmethod
    def species(cls):
        print(f"Belong to: {cls.spec}")

    @staticmethod
    def arb_message():
        print("Arbitrary message")