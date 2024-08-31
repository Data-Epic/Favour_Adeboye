import unittest
import pandas as pd
from pandas.api.types import CategoricalDtype
from datawrangler.data_type import (
    validate_data_types,
    convert_to_numeric,
    convert_to_datetime,
    convert_to_category,
    detect_data_types,
    change_dtype,
    correct_data_types
)

class TestDataType(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'int_column': [1, 2, 3, 4],
            'float_column': [1.1, 2.2, 3.3, 4.4],
            'str_column': ['a', 'b', 'c', 'd'],
            'date_column': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'],
            'mixed_column': ['1', 'two', 3, 4.0]
        })
    
    # Test validate_data_types function
    def test_validate_data_types(self):
        # Test with correct data types
        expected_types = {
            'int_column': 'int64',
            'float_column': 'float64',
            'str_column': 'object'
        }
        self.assertTrue(validate_data_types(self.df, expected_types))

        # Test with incorrect data types
        expected_types_wrong = {
            'int_column': 'float64',
            'float_column': 'int64',
            'str_column': 'int64'
        }
        self.assertFalse(validate_data_types(self.df, expected_types_wrong))

        # Test with invalid input
        with self.assertRaises(TypeError):
            validate_data_types("Not a DataFrame", expected_types)

        with self.assertRaises(TypeError):
            validate_data_types(self.df, "Not a dict")

        with self.assertRaises(ValueError):
            validate_data_types(self.df, {'nonexistent_column': 'int64'})

    # Test convert_to_numeric function
    def test_convert_to_numeric(self):
        # Test conversion with coercing errors
        result = convert_to_numeric(self.df, ['mixed_column'])
        self.assertTrue(result['mixed_column'].isnull().any())  # 'two' should be NaN

        # Test conversion with raising errors
        with self.assertRaises(ValueError):
            convert_to_numeric(self.df, ['str_column'], errors='raise')

        # Test with invalid input
        with self.assertRaises(TypeError):
            convert_to_numeric("Not a DataFrame", ['mixed_column'])

        with self.assertRaises(TypeError):
            convert_to_numeric(self.df, 'mixed_column')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            convert_to_numeric(self.df, ['nonexistent_column'])

    # Test convert_to_datetime function
    def test_convert_to_datetime(self):
        # Test conversion with date format
        result = convert_to_datetime(self.df, ['date_column'], format='%Y-%m-%d')
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result['date_column']))

        # Test conversion without specifying format
        result = convert_to_datetime(self.df, ['date_column'])
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(result['date_column']))

        # Test with invalid input
        with self.assertRaises(TypeError):
            convert_to_datetime("Not a DataFrame", ['date_column'])

        with self.assertRaises(TypeError):
            convert_to_datetime(self.df, 'date_column')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            convert_to_datetime(self.df, ['nonexistent_column'])

    # Test convert_to_category function
    def test_convert_to_category(self):
        # Test conversion to category
        result = convert_to_category(self.df, ['str_column'])
        self.assertTrue(pd.api.types.is_categorical_dtype(result['str_column']))

        # Test with invalid input
        with self.assertRaises(TypeError):
            convert_to_category("Not a DataFrame", ['str_column'])

        with self.assertRaises(TypeError):
            convert_to_category(self.df, 'str_column')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            convert_to_category(self.df, ['nonexistent_column'])

    # Test detect_data_types function
    def test_detect_data_types(self):
        # Test detecting data types
        result = detect_data_types(self.df)
        self.assertEqual(result['int_column'], 'int64')
        self.assertEqual(result['float_column'], 'float64')
        self.assertEqual(result['str_column'], 'object')

        # Test with invalid input
        with self.assertRaises(TypeError):
            detect_data_types("Not a DataFrame")

    # Test change_dtype function
    def test_change_dtype(self):
        # Test changing data type
        result = change_dtype(self.df, 'int_column', 'float')
        self.assertTrue(pd.api.types.is_float_dtype(result['int_column']))

        # Test with invalid input
        with self.assertRaises(TypeError):
            change_dtype("Not a DataFrame", 'int_column', 'float')

        with self.assertRaises(TypeError):
            change_dtype(self.df, 1, 'float')  # Column must be a string

        with self.assertRaises(ValueError):
            change_dtype(self.df, 'nonexistent_column', 'float')

        with self.assertRaises(TypeError):
            change_dtype(self.df, 'int_column', 'nonexistent_type')  # Invalid type

    # Test correct_data_types function
    def test_correct_data_types(self):
        # Test with valid column types
        column_types = {
            'int_column': 'float64',
            'str_column': CategoricalDtype()
        }
        result = correct_data_types(self.df, column_types)
        self.assertTrue(pd.api.types.is_float_dtype(result['int_column']))
        self.assertTrue(pd.api.types.is_categorical_dtype(result['str_column']))

        # Test with invalid input
        with self.assertRaises(TypeError):
            correct_data_types("Not a DataFrame", column_types)

        with self.assertRaises(TypeError):
            correct_data_types(self.df, "Not a dict")

        with self.assertRaises(ValueError):
            correct_data_types(self.df, {'nonexistent_column': 'int64'})

        with self.assertRaises(TypeError):
            correct_data_types(self.df, {'int_column': 'invalid_type'})

if __name__ == '__main__':
    unittest.main()