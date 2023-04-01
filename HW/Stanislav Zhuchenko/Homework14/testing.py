import unittest
from functions_with_errors import *
# from functions import *

class Test(unittest.TestCase):

    def test_greeting_by_name(self):
        try:
            self.assertEqual(greeting_by_name('Name'), 'Hello Name!')
        except AssertionError:
            print('Test greeting_by_name(name) is Failed')
        else:
            print('Test greeting_by_name(name) is Passed')

    def test_get_symbol_position1(self):
        text = 'Hello'
        symbol = 'e'
        res = 2
        try:
            self.assertEqual(get_symbol_position(text, symbol), res)
        except AssertionError:
            print('Test get_symbol_position(text, symbol) with success symbol is Failed')
        else:
            print('Test get_symbol_position(text, symbol) with success symbol is Passed')

    def test_get_symbol_position2(self):
        text = 'Hello'
        symbol = 'Hello'
        res = "Error! Symbol can be string with only one letter"
        try:
            self.assertEqual(get_symbol_position(text, symbol), res)
        except AssertionError:
            print('Test get_symbol_position(text, symbol) with symbol incorrect is Failed')
        else:
            print('Test get_symbol_position(text, symbol) with symbol incorrect is Passed')

    def test_get_symbol_position3(self):
        text = 'Hello'
        symbol = 'D'
        res = "Not found"
        try:
            self.assertEqual(get_symbol_position(text, symbol), res)
        except AssertionError:
            print('Test get_symbol_position(text, symbol) when symbol was not found is Failed')
        else:
            print('Test get_symbol_position(text, symbol) when symbol was not found is Passed')

    def test_merge1(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3}
        res = {'a': 1, 'b': 2, 'c': 3}
        try:
            self.assertEqual(merge(dict1, dict2), res)
        except AssertionError:
            print('Test merge(dict1, dict2) is Failed')
        else:
            print('Test merge(dict1, dict2) is Passed')


    def test_merge2(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3}
        try:
            self.assertIsNot(dict1, merge(dict1, dict2))
        except AssertionError:
            print('Test merge(dict1, dict2) dict1 immutability is Failed')
        else:
            print('Test merge(dict1, dict2) dict1 immutability is Passed')

    def test_merge3(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3}
        try:
            self.assertIsNot(dict2, merge(dict1, dict2))
        except AssertionError:
            print('Test merge(dict1, dict2) dict2 immutability is Failed')
        else:
            print('Test merge(dict1, dict2) dict2 immutability is Passed')
