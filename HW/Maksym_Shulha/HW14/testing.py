import functions as file
# import functions_with_errors as file
import unittest


class FuncTest(unittest.TestCase):
    def test_greeting_by_name(self):
        try:
            self.assertEqual(file.greeting_by_name("Maks"), "Hello Maks!")
        except AssertionError:
            print("Test greeting_by_name(name) is Failed")
        else:
            print("Test greeting_by_name(name) is Passed")

    def test_get_symbol_position_1(self):
        try:
            self.assertEqual(file.get_symbol_position("Testing", "aa"),
                             "Error! Symbol can be string with only one letter")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol is incorrect is Failed")
        else:
            print("Test get_symbol_position(text, symbol) when symbol is incorrect is Passed")

    def test_get_symbol_position_2(self):
        try:
            self.assertEqual(file.get_symbol_position("Testing", "s"), 3)
        except AssertionError:
            print("Test get_symbol_position(text, symbol) with success is Failed")
        else:
            print("Test get_symbol_position(text, symbol) with success is Passed")

    def test_get_symbol_position_3(self):
        try:
            self.assertEqual(file.get_symbol_position("Testing", "w"), "Not found")
        except AssertionError:
            print("Test get_symbol_position(text, symbol) when symbol was not found is Failed")
        else:
            print("Test get_symbol_position(text, symbol) when symbol was not found is Passed")

    def test_merge_1(self):
        try:
            self.assertEqual(file.merge({1: "a"}, {2: "b"}), {1: "a", 2: "b"})
        except AssertionError:
            print("Test merge(dict1, dict2) Failed")
        else:
            print("Test merge(dict1, dict2) is Passed")

    def test_merge_2(self):
        dict1 = {1: "a"}
        dict2 = {2: "b"}
        dict3 = file.merge(dict1, dict2)
        try:
            self.assertNotEqual(dict1, dict3)
        except AssertionError:
            print("Test merge(dict1, dict2) dict1 immutability Failed")
        else:
            print("Test merge(dict1, dict2) dict1 immutability is Passed")

    def test_merge_3(self):
        dict1 = {1: "a"}
        dict2 = {2: "b"}
        dict3 = file.merge(dict1, dict2)
        try:
            self.assertNotEqual(dict2, dict3)
        except AssertionError:
            print("Test merge(dict1, dict2) dict2 immutability Failed")
        else:
            print("Test merge(dict1, dict2) dict2 immutability is Passed")


if __name__ == '__main__':
    unittest.main()
