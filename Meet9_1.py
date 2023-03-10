# class MyClass:
#     """This is my second class"""
#     a = 10
#     def __init__(self):
#         pass
#         #self.a = 15
#     def func(self):
#         print(self.a)
#
#
# f = MyClass()
# g = MyClass()
# #f.a -> MyClass.a
# #MyClass.a -> f.a ()
# #f.a = new
#
# MyClass.a = 1
# print(id(MyClass.a),id(f.a), id(g.a))
#
# f.a = 2
# print(id(MyClass.a),id(f.a), id(g.a))
#
# MyClass.a = 5
# print(id(MyClass.a),id(f.a), id(g.a))
#
# g.a = 111
# print(id(MyClass.a),id(f.a), id(g.a))