# s = set([5, 1, 2, 3])
# print(s)
#
# s.update([5.0])
# print(s)
#
# print(id(5.0))
# print(id(5))

# s.discard(1)
# s.remove(1)
#
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# print(A | B)
# print(A.union(B))

# print(A & B)
# print(A.intersection(B))

# print(A - B)
# print(A - (A & B))
# print(B.difference(A))

# print(A ^ B) # (A | B) - (A & B)
# print((A | B) - (A & B))
# print((A - B) | (B - A))
# print(B.symmetric_difference(A))
#
# print(A)
# print(B)

A = {1, 2}
B = {1, 2, 3, 4}

# print(A.issubset(A))
# print(A.issubset(B))
# print(A.issuperset(B))
#
# print(B.issuperset(A))
# print(B.issuperset(B))
#
# C = {3, 4}
# print(A.isdisjoint(C))

# di = {1: 123, 2: 222, 3:345}
# print(di[1])
# print(di[1234])
#
# print(di.get(123))
# print(di.get(3))

# print(di.fromkeys((12, 3), (1, 2)))
# print(di.items())
# print(di.keys())
# di.update(([1, 'hello'], (4, .5)))
# print(di)

# print(di.values())


# def my_func():
#     """Some info about"""
#     return []
#
# def lin_search(a, arr):
#     """
#     Linear search function
#     :param a: value of element
#     :param arr: array of elements
#     :return: index of element, else return None
#     """
#     for i in range(len(arr)):
#         if arr[i] == a:
#             return i
#     else:
#         return None

# def arithmetic_mean(*args):
#     return sum(args)/len(args)
#     # s = 0
#     # for i in args:
#     #     s += i
#     # return s/len(args)
#
# print(arithmetic_mean(1, 2, 3, 4, 10))
# print(arithmetic_mean(1, 2, 3, 4, 5))

# x = 0
# def foo():
#     x = 1
#     def in_foo():
#         nonlocal x
#         x = 123
#         def in_in_foo():
#             nonlocal x
#             print(x)
#         in_in_foo()
#     in_foo()
#
# foo()
# print(x)