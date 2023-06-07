# class MyClass:
#     a = 100
#     def __init__(self, b = 0):
#         self.b = b
#
#     @classmethod
#     def a_add(cls):
#         cls.a += 1
#
#     def b_add(self):
#         self.b +=1
#
#
# o = MyClass()
#
# # print(id(MyClass.a))
# # o.a_add()
# # MyClass.a_add()
# # print(id(MyClass.a))
# # print(id(o.a))
#
#
# print(o.b)
# o.b_add()
# print(o.b)
# MyClass.b_add()
#

class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print (animal.name + ': ' + animal.talk())
