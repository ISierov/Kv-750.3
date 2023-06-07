# #h-5 w-5
# '''
# #000#
# #000#
# 0#0#0
# 0#0#0
# 00#00
# '''
# def write_I(f):
#     for i in range(5):
#         f.write(' ### \n')
#     f.write('\n')
#
# def write_V(f):
#     f.write(
# """#   #
# #   #
#  # #
#  # #
#   #  """)
#     f.write('\n')
# def write_A(f):
#     pass
#
# def write_N(f):
#     pass
#
# if __name__ == '__main__':
#     with open('input.txt', 'w') as f:
#         write_I(f)
#         write_V(f)
#
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mult(a, b):
#     return a * b
#
# def div(a, b):
#     if b == 0:
#         return None
#     return (a) / b
#
# import unittest
#
# class TestMethods(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(1, 2), 3)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(-1, -1), -2)
#
#     def test_sub(self):
#         self.assertEqual(sub(1, 2), -1)
#         self.assertEqual(sub(-1, 1), -2)
#         self.assertEqual(sub(-1, -1), 0)
#
#     def test_mult(self):
#         self.assertEqual(mult(3, 5), 15)
#         self.assertEqual(mult(-3, 5), -15)
#         self.assertEqual(mult(-3, -5), 15)
#
#     def test_div(self):
#         self.assertEqual(div(10, 2), 5)
#         self.assertEqual(div(-10, 2), -5)
#         self.assertIsNone(div(10, 0))
#
# if __name__ == '__main__':
#     unittest.main()

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print('Working time = ', finish - start)
        return res
    return wrapper

@timer
def write_I():
    time.sleep(6)


write_I()