import unittest
from my_awesome_lib.text_processing import to_uppercase, is_palindrome


class TestTextProcessing(unittest.TestCase):

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")  # Testujemy zwykły tekst
        self.assertEqual(to_uppercase("world"), "WORLD")  # Testujemy inny tekst
        self.assertEqual(to_uppercase(""), "")  # Testujemy pusty tekst

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))  # Sprawdzamy palindrom
        self.assertFalse(is_palindrome("hello"))  # Sprawdzamy tekst, który nie jest palindromem
        self.assertFalse(is_palindrome(""))  # Testujemy pusty tekst
