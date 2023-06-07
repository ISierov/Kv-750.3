class Human:
    def __init__(self):
        self.Adam = Woman()
        self.Eva = Man()
    def creation(self):
        return [self.Adam, self.Eva]
class Woman(Human):
    def __init__(self):
        pass
class Man(Human):
    def __init__(self):
        pass

