import unittest

from calculator_app import Calculations

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        sum = sum(3, 5)
        self.assertEqual(sum.execute(), 8)

    def test_difference(self):
        difference = difference(10, 4)
        self.assertEqual(difference.execute(), 6)

    def test_product(self):
        product = product(6, 7)
        self.assertEqual(product.execute(), 42)

    def test_quotient(self):
        quotient = quotient(20, 5)
        self.assertEqual(quotient.execute(), 4)

    def test_division_by_zero(self):
        division = division(10, 0)
        with self.assertRaises(ValueError):
            division.execute()

if __name__ == '__main__':
    unittest.main()
