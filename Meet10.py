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

# class Animal:
#     def __init__(self, name):    # Constructor of the class
#         self.name = name
#     def talk(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Cat(Animal):
#     def talk(self):
#         return 'Meow!'
#
# class Dog(Animal):
#     def talk(self):
#         return 'Woof! Woof!'
#
# animals = [Cat('Missy'),
#            Cat('Mr. Mistoffelees'),
#            Dog('Lassie')]
#
# for animal in animals:
#     print (animal.name + ': ' + animal.talk())


class Bank_acc:
    def __init__(self, id, balance):
        self.__id = id
        self.__balance = balance

    def set_id(self, id):
        if float(id) < 0 or not id.isnumeric():
            raise ValueError()
        else:
            self.__id = id

    def get_id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if (balance < 0) or not balance.isnumeric():
            raise ValueError()
        else:
            self.__balance = balance

    def __repr__(self):
        return f'For {self.__id}: {self.__balance}\n'

if __name__ == '__main__':
    my = Bank_acc('1234', '1234.00')
    print(my)
    my.set_id('1234567')
    print(my)
