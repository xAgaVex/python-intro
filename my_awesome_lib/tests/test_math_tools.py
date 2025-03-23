import unittest
from my_awesome_lib.math_tools import add, multiply


class TestMathTools(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Normalne dodawanie
        self.assertEqual(add(-1, 1), 0)  # Testujemy z liczbami ujemnymi

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)  # Normalne mnożenie
        self.assertEqual(multiply(0, 5), 0)  # Testujemy mnożenie przez 0
