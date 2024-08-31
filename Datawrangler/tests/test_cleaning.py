import unittest
import pandas as pd
from datawrangler.cleaning import remove_duplicates, clean_text, correct_data_formats, correct_outliers


class TestCleaning(unittest.TestCase):

    def setUp(self):
        # Sample DataFrames for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 2, 4, 5],
            'B': ['foo', 'bar', 'bar', 'baz', 'qux'],
            'C': ['Text with spaces  ', 'Another text', 'Another text', 'Special chars!@#$', 'LOWERCASE'],
            'D': [10, 15, 20, 25, 30]
        })

    # Test remove_duplicates function
    def test_remove_duplicates(self):
        # Test with all columns (default)
        result = remove_duplicates(self.df)
        self.assertEqual(len(result), 4)  # Expected length after removing duplicates

        # Test with a subset of columns
        result = remove_duplicates(self.df, subset=['A', 'B'])
        self.assertEqual(len(result), 4)  # Expected length after removing duplicates
        
        # Test with no duplicates
        no_dup_df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['foo', 'bar', 'baz', 'qux', 'quux']
        })
        result = remove_duplicates(no_dup_df)
        self.assertEqual(len(result), 5)  # Expected length with no duplicates

        # Test with invalid input
        with self.assertRaises(TypeError):
            remove_duplicates("Not a DataFrame")

        with self.assertRaises(TypeError):
            remove_duplicates(self.df, subset='Not a list')

        with self.assertRaises(ValueError):
            remove_duplicates(self.df, subset=['NonExistentColumn'])

    # Test clean_text function
    def test_clean_text(self):
        # Test default behavior
        result = clean_text(self.df, 'C')
        self.assertEqual(result['C'][0], 'text with spaces')
        self.assertEqual(result['C'][3], 'special chars')
        
        # Test without removing special characters
        result = clean_text(self.df, 'C', remove_special_chars=False)
        self.assertEqual(result['C'][3], 'special chars!@#$')
        
        # Test with invalid input
        with self.assertRaises(TypeError):
            clean_text("Not a DataFrame", 'C')
        
        with self.assertRaises(TypeError):
            clean_text(self.df, 1)  # Column name must be a string

        with self.assertRaises(ValueError):
            clean_text(self.df, 'NonExistentColumn')

    # Test correct_data_formats function
    def test_correct_data_formats(self):
        # Test with valid format function
        result = correct_data_formats(self.df, 'A', format_func=str)
        self.assertTrue(all(isinstance(x, str) for x in result['A']))
        
        # Test with a custom format function
        format_func = lambda x: x * 2
        result = correct_data_formats(self.df, 'A', format_func)
        self.assertTrue(all(result['A'] == pd.Series([2, 4, 4, 8, 10])))

        # Test with invalid input
        with self.assertRaises(TypeError):
            correct_data_formats("Not a DataFrame", 'A', format_func=str)

        with self.assertRaises(TypeError):
            correct_data_formats(self.df, 1, format_func=str)  # Column name must be a string

        with self.assertRaises(ValueError):
            correct_data_formats(self.df, 'NonExistentColumn', format_func=str)

        with self.assertRaises(TypeError):
            correct_data_formats(self.df, 'A', format_func="NotCallable")

    # Test correct_outliers function
    def test_correct_outliers(self):
        # Test with valid bounds
        result = correct_outliers(self.df, 'D', lower_bound=15, upper_bound=25)
        self.assertEqual(result['D'].min(), 15)
        self.assertEqual(result['D'].max(), 25)
        
        # Test with equal bounds
        result = correct_outliers(self.df, 'D', lower_bound=20, upper_bound=20)
        self.assertTrue(all(result['D'] == 20))
        
        # Test with invalid input
        with self.assertRaises(TypeError):
            correct_outliers("Not a DataFrame", 'D', lower_bound=15, upper_bound=25)

        with self.assertRaises(TypeError):
            correct_outliers(self.df, 1, lower_bound=15, upper_bound=25)  # Column name must be a string

        with self.assertRaises(ValueError):
            correct_outliers(self.df, 'NonExistentColumn', lower_bound=15, upper_bound=25)

        with self.assertRaises(TypeError):
            correct_outliers(self.df, 'D', lower_bound='Not a number', upper_bound=25)

        with self.assertRaises(ValueError):
            correct_outliers(self.df, 'D', lower_bound=30, upper_bound=15)  # Lower bound greater than upper bound

if __name__ == '__main__':
    unittest.main()