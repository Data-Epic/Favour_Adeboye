import unittest
from unittest.mock import patch
from calculator_app import Calculations, get_valid_operand

class TestCalculations(unittest.TestCase):
    """
    Unit test class for testing the Calculations class and the get_valid_operand function.
    """
    
    def setUp(self):
        """
        Sets up a Calculations instance for use in tests.
        """
        self.calc = Calculations(10, 5)

    def test_get_sum(self):
        """
        Tests the get_sum method of the Calculations class.
        """
        self.assertEqual(self.calc.get_sum(), 15)

    def test_get_difference(self):
        """
        Tests the get_difference method of the Calculations class.
        """
        self.assertEqual(self.calc.get_difference(), 5)

    def test_get_product(self):
        """
        Tests the get_product method of the Calculations class.
        """
        self.assertEqual(self.calc.get_product(), 50)

    def test_get_quotient(self):
        """
        Tests the get_quotient method of the Calculations class.
        """
        self.assertEqual(self.calc.get_quotient(), 2)

    def test_get_quotient_divide_by_zero(self):
        """
        Tests the get_quotient method of the Calculations class when a zero value is assigned to the second operand.
        """
        calc = Calculations(10, 0)
        with self.assertRaises(ValueError):
            calc.get_quotient()

    def test_get_valid_operand_valid_input(self):
        """
        Tests the get_valid_operand function with valid input.
        """
        with patch('builtins.input', return_value='10.5'):
            self.assertEqual(get_valid_operand("Enter a number: "), 10.5)

    def test_get_valid_operand_invalid_input(self):
        """
        Tests the get_valid_operand function with invalid input followed by a valid input.
        """
        with patch('builtins.input', side_effect=['invalid', '10.5']):
            self.assertEqual(get_valid_operand("Enter a number: "), 10.5)

if __name__ == '__main__':
    unittest.main()