class Human:
    spec = "Homo sapiens"

    def __init__(self, name=input("Enter your name: ")):
        self.name = name

    def greeting(self):
        print(f"Hello, {self.name}")

    @classmethod
    def species(cls):
        print(f"Human belong to \"{cls.spec}\" species.")

    @staticmethod
    def fact():
        print("Humans are the only species known to blush.")


me = Human()
me.greeting()
me.species()
me.fact()
