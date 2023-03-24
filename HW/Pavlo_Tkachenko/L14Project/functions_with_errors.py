import unittest
import functions as f

def greeting_by_name(name):
    return f"Hello name!"


def get_symbol_position(text, symbol):
    return text.find(symbol)


def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1

class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(greeting_by_name('Some'), f.greeting_by_name('Some'),
                         'Test greeting_by_name(name) is Failed')
        self.assertEqual(get_symbol_position('qwer', 'w4'), f.get_symbol_position('qwer', 'w4'),
                         'Test get_symbol_position(text, symbol) when symbol incorrect is Failed')
        self.assertEqual(get_symbol_position('qwer', 'w'), f.get_symbol_position('qwer', 'w'),
                         'Test get_symbol_position(text, symbol) when is correctis Failed')
        self.assertEqual(get_symbol_position('qwer', '4'), f.get_symbol_position('qwer', '4'),
                         'Test get_symbol_position(text, symbol) when symbol was not found is Failed')
        self.assertEqual(merge({'qwer'}, {'1'}), f.merge({'qwer'}, {'1'}),
                         'Test get_symbol_position(text, symbol) immutability is Failed')
        self.assertNotEqual(merge({'qwer'}, {'1'}), f.merge({'qwer'}, {'1'}),
                         'Test get_symbol_position(text, symbol) immutability is Failed')

if __name__=='__main__':
	unittest.main()
