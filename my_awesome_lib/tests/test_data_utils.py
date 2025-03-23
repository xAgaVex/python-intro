import unittest
from my_awesome_lib.data_utils import convert_to_int, split_string


class TestDataUtils(unittest.TestCase):

    def test_convert_to_int(self):
        self.assertEqual(convert_to_int("123"), 123)  # Testujemy poprawne dane
        self.assertEqual(convert_to_int("abc"), None)  # Testujemy błędne dane

    def test_split_string(self):
        self.assertEqual(split_string("a,b,c"), ['a', 'b', 'c'])  # Testujemy poprawne dane
        self.assertEqual(split_string("a|b|c", "|"), ['a', 'b', 'c'])  # Zmieniamy separator
        self.assertEqual(split_string("", ","), [])  # Testujemy pusty ciąg
