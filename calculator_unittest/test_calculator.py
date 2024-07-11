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
        result = self.calc.get_sum()
        self.assertEqual(result, 15)

    def test_get_difference(self):
        """
        Tests the get_difference method of the Calculations class.
        """
        result = self.calc.get_difference()
        self.assertEqual(result, 5)

    def test_get_product(self):
        """
        Tests the get_product method of the Calculations class.
        """
        result = self.calc.get_product()
        self.assertEqual(result, 50)

    def test_get_quotient(self):
        """
        Tests the get_quotient method of the Calculations class.
        """
        result = self.calc.get_quotient()
        self.assertEqual(result, 2)

        # Test division by zero
        calc = Calculations(10, 0)
        with self.assertRaises(ValueError):
            calc.get_quotient()

    def test_get_valid_operand(self):
        """
        Tests the get_valid_operand function with valid and invalid input.
        """
        # Valid input
        with patch('builtins.input', return_value='10.5'):
            result = get_valid_operand("Enter a number: ")
            self.assertEqual(result, 10.5)

        # Invalid input followed by valid input
        with patch('builtins.input', side_effect=['invalid', '10.5']):
            result = get_valid_operand("Enter a number: ")
            self.assertEqual(result, 10.5)

if __name__ == '__main__':
    unittest.main()