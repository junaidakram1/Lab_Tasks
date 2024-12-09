import unittest
from sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(987654321), 45)
        self.assertEqual(sum_of_digits(999999999), 81)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits(-123), 6)
        self.assertEqual(sum_of_digits(-456), 15)

    def test_large_number(self):
        self.assertEqual(sum_of_digits(12345678901234567890), 90)

if __name__ == "__main__":
    unittest.main()
