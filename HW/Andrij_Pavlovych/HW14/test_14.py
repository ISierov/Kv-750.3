import functions_with_errors
import functions
import unittest


class FuncErrorTest(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(functions_with_errors.greeting_by_name('Bob'), 'Hello Bob!')

    def test_get_symbol_position(self):
        result1 = 'Error! Symbol can be string with only one letter'
        result2 = 'Not found'
        self.assertEqual(functions_with_errors.get_symbol_position('text', 'ee'), result1),
        self.assertIsInstance(functions_with_errors.get_symbol_position('text', 'e'), int),
        self.assertEqual(functions_with_errors.get_symbol_position('text', 'e'), 2)
        self.assertEqual(functions_with_errors.get_symbol_position('text', 'r'), result2)

    def test_merge(self):
        dict1 = {'s': 1, 'e': 2}
        dict2 = {'t': 3}
        dict3 = {'s': 1, 'e': 2, 't': 3}
        self.assertEqual(functions_with_errors.merge(dict1, dict2), dict3)
        self.assertIsInstance(functions_with_errors.merge(dict1, dict2), dict)
        self.assertNotEqual(functions_with_errors.merge(dict1, dict2), dict1)


class FuncNoErrorTest(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(functions.greeting_by_name('Bob'), 'Hello Bob!')

    def test_get_symbol_position(self):
        result1 = 'Error! Symbol can be string with only one letter'
        result2 = 'Not found'
        self.assertEqual(functions.get_symbol_position('text', 'ee'), result1),
        self.assertIsInstance(functions.get_symbol_position('text', 'e'), int),
        self.assertEqual(functions.get_symbol_position('text', 'e'), 2)
        self.assertEqual(functions.get_symbol_position('text', 'r'), result2)

    def test_merge(self):
        dict1 = {'s': 1, 'e': 2}
        dict2 = {'t': 3}
        dict3 = {'s': 1, 'e': 2, 't': 3}
        self.assertEqual(functions.merge(dict1, dict2), dict3)
        self.assertIsInstance(functions.merge(dict1, dict2), dict)
        self.assertNotEqual(functions.merge(dict1, dict2), dict1)