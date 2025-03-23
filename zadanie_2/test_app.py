import unittest
from app import is_valid_email, rectangle_area, sort_list, convert_date, is_palidrome


class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        # Przygotowanie danych do testów
        self.valid_email = "test@example.com"
        self.invalid_email = "testexample.com"
        self.rectangle_a = 5
        self.rectangle_b = 3
        self.unsorted_list = [3, 1, 4, 2]
        self.sorted_list = [1, 2, 3, 4]
        self.date = "23-03-2025"
        self.palindrome_text = "A to kanapa pana Kota"
        self.non_palindrome_text = "ChatGPT"

    # Parametryzacja testów dla is_valid_email
    def test_valid_email(self):
        test_cases = [
            ("test@example.com", True),
            ("invalid-email", False),
            ("test@com", False),
            ("@missinglocalpart.com", False)
        ]
        for email, expected in test_cases:
            with self.subTest(email=email):
                self.assertEqual(is_valid_email(email), expected)

    # Parametryzacja testów dla is_palindrome
    def test_is_palindrome(self):
        test_cases = [
            ("kajak", True),
            ("A to kanapa pana Kota", True),
            ("12321", True),
            ("ChatGPT", False),
            ("hello", False)
        ]
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palidrome(text), expected)

    # Parametryzacja testów dla convert_date
    def test_convert_date(self):
        test_cases = [
            ("23-03-2025", "2025/03/23"),
            ("31-12-2025", "2025/12/31"),
            ("31-02-2025", ValueError),
        ]
        for date, expected in test_cases:
            with self.subTest(date=date):
                if isinstance(expected, str):
                    self.assertEqual(convert_date(date), expected)
                else:
                    with self.assertRaises(expected):
                        convert_date(date)

    # Pozostałe testy dla innych funkcji
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(self.rectangle_a, self.rectangle_b), 15)

    def test_sort_list(self):
        sort_list(self.unsorted_list)
        self.assertEqual(self.unsorted_list, self.sorted_list)

    def test_sort_list_empty(self):
        self.assertEqual(sort_list([]), None)


if __name__ == "__main__":
    unittest.main()
