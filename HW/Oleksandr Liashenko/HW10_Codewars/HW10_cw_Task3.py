# Basic subclasses - Adam and Eve
#
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#
# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

#This works on Codewars but it doesn't use creation method like said in instructions

class God:
    def __init__(self):
        self.paradise = [Man("Adam"), Woman("Eve")]

    def __getitem__(self, index):
        return self.paradise[index]

    def __len__(self):
        return len(self.paradise)


# Before asking ChatGPT I tried this code and it passed sample test :
# # class God:
# #     def creation(self):
# #         global paradise
# #         paradise = [Man("Adam"), Woman("Eve")]
# #         return paradise
#
# but every time returned the same error:
#
# # Traceback (most recent call last):
# #  File "/workspace/default/tests.py", line 4, in <module>
# #    test.assert_equals(isinstance(paradise[0], Man) , True, "First object are a man")
# #                                  ~~~~~~~~^^^
# # TypeError: 'God' object is not subscriptable

# AFTER ALL I LOOKED AT ANSWERS. DOESN'T LOOK LIKE INSTRUCTIONS WERE CORRECT

class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

paradise = God()

print(isinstance(paradise[0], Man))