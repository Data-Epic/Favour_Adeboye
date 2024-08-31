import unittest
import pandas as pd
from datawrangler.missing_values import (
    identify_missing,
    impute_missing,
    fill_forward,
    fill_backward,
    drop_missing_data
)

class TestMissingValues(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [None, 2.2, 3.3, None, 5.5],
            'C': ['foo', 'bar', None, 'qux', 'quux'],
            'D': [10, 15, 20, 25, None]
        })

    # Test identify_missing function
    def test_identify_missing(self):
        # Test with valid DataFrame
        result = identify_missing(self.df)
        self.assertTrue(isinstance(result, pd.Series))
        self.assertEqual(result['A'], 1)
        self.assertEqual(result['B'], 2)
        self.assertEqual(result['C'], 1)
        self.assertEqual(result['D'], 1)

        # Test with invalid input
        with self.assertRaises(TypeError):
            identify_missing("Not a DataFrame")

    # Test impute_missing function
    def test_impute_missing(self):
        # Test mean imputation
        result = impute_missing(self.df.copy(), method='mean')
        self.assertAlmostEqual(result['A'][2], 3.0)  # Mean of column A
        self.assertAlmostEqual(result['B'][0], 3.666, places=3)  # Mean of column B

        # Test median imputation
        result = impute_missing(self.df.copy(), method='median')
        self.assertEqual(result['A'][2], 3.0)  # Median of column A
        self.assertEqual(result['B'][0], 3.3)  # Median of column B

        # Test mode imputation
        df_with_mode = pd.DataFrame({'A': [1, 2, 2, 4, None], 'B': [None, 2, 3, None, 3]})
        result = impute_missing(df_with_mode.copy(), method='mode')
        self.assertEqual(result['A'][4], 2)  # Mode of column A
        self.assertEqual(result['B'][0], 3)  # Mode of column B

        # Test constant imputation
        result = impute_missing(self.df.copy(), method=0)
        self.assertEqual(result['A'][2], 0)
        self.assertEqual(result['B'][0], 0)

        # Test with invalid method
        with self.assertRaises(ValueError):
            impute_missing(self.df.copy(), method='invalid_method')

        # Test with invalid input
        with self.assertRaises(TypeError):
            impute_missing("Not a DataFrame", method='mean')

    # Test fill_forward function
    def test_fill_forward(self):
        # Test forward fill on all columns
        result = fill_forward(self.df.copy())
        self.assertEqual(result['A'][2], 2.0)  # Should be filled with previous value
        self.assertEqual(result['B'][3], 3.3)  # Should be filled with previous value

        # Test forward fill on specific columns
        result = fill_forward(self.df.copy(), columns=['A', 'B'])
        self.assertEqual(result['A'][2], 2.0)  # Should be filled with previous value
        self.assertEqual(result['B'][3], 3.3)  # Should be filled with previous value

        # Test with invalid input
        with self.assertRaises(TypeError):
            fill_forward("Not a DataFrame")

        with self.assertRaises(TypeError):
            fill_forward(self.df, columns='A')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            fill_forward(self.df, columns=['nonexistent_column'])

    # Test fill_backward function
    def test_fill_backward(self):
        # Test backward fill on all columns
        result = fill_backward(self.df.copy())
        self.assertEqual(result['A'][2], 4.0)  # Should be filled with next value
        self.assertEqual(result['B'][0], 2.2)  # Should be filled with next value

        # Test backward fill on specific columns
        result = fill_backward(self.df.copy(), columns=['A', 'B'])
        self.assertEqual(result['A'][2], 4.0)  # Should be filled with next value
        self.assertEqual(result['B'][0], 2.2)  # Should be filled with next value

        # Test with invalid input
        with self.assertRaises(TypeError):
            fill_backward("Not a DataFrame")

        with self.assertRaises(TypeError):
            fill_backward(self.df, columns='A')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            fill_backward(self.df, columns=['nonexistent_column'])

    # Test drop_missing_data function
    def test_drop_missing_data(self):
        # Test dropping rows with missing data in all columns
        result = drop_missing_data(self.df.copy())
        self.assertEqual(len(result), 2)  # Only rows with no missing data remain

        # Test dropping rows with missing data in specific columns
        result = drop_missing_data(self.df.copy(), columns=['A'])
        self.assertEqual(len(result), 4)  # Rows with missing data in column A are dropped

        # Test with invalid input
        with self.assertRaises(TypeError):
            drop_missing_data("Not a DataFrame")

        with self.assertRaises(TypeError):
            drop_missing_data(self.df, columns='A')  # Columns parameter must be a list

        with self.assertRaises(ValueError):
            drop_missing_data(self.df, columns=['nonexistent_column'])

if __name__ == '__main__':
    unittest.main()