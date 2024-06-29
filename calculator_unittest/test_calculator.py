import unittest
from unittest.mock import patch
from calculator_app import Calculations, get_valid_operand

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calc = Calculations(10, 5)

    def test_get_sum(self):
        self.assertEqual(self.calc.get_sum(), 15)

    def test_get_difference(self):
        self.assertEqual(self.calc.get_difference(), 5)

    def test_get_product(self):
        self.assertEqual(self.calc.get_product(), 50)

    def test_get_quotient(self):
        self.assertEqual(self.calc.get_quotient(), 2)

    def test_get_quotient_divide_by_zero(self):
        calc = Calculations(10, 0)
        with self.assertRaises(ValueError):
            calc.get_quotient()

    def test_get_valid_operand_valid_input(self):
        with patch('builtins.input', return_value='10.5'):
            self.assertEqual(get_valid_operand("Enter a number: "), 10.5)

    def test_get_valid_operand_invalid_input(self):
        with patch('builtins.input', side_effect=['invalid', '10.5']):
            self.assertEqual(get_valid_operand("Enter a number: "), 10.5)

if __name__ == '__main__':
    unittest.main()