import unittest
import pandas as pd
import numpy as np
from datawrangler.exploration import (
    describe_data,
    plot_histogram,
    plot_scatter,
    check_data_integrity,
    data_quality_report
)

class TestExploration(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'numeric_col': [1, 2, 3, 4, 5],
            'string_col': ['a', 'b', 'c', 'd', 'e'],
            'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
            'date_col': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
            'mixed_col': [1, 'two', 3, 4.0, 'five']
        })
    
    # Test describe_data function
    def test_describe_data(self):
        # Test with valid DataFrame
        result = describe_data(self.df)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertIn('numeric_col', result.columns)

        # Test with invalid input
        with self.assertRaises(TypeError):
            describe_data("Not a DataFrame")

    # Test plot_histogram function
    def test_plot_histogram(self):
        # Test with valid numeric column
        plot_histogram(self.df, 'numeric_col')  # Should plot without errors

        # Test with non-numeric column
        with self.assertRaises(ValueError):
            plot_histogram(self.df, 'string_col')

        # Test with non-existing column
        with self.assertRaises(ValueError):
            plot_histogram(self.df, 'nonexistent_col')

        # Test with invalid input
        with self.assertRaises(TypeError):
            plot_histogram("Not a DataFrame", 'numeric_col')

        with self.assertRaises(TypeError):
            plot_histogram(self.df, 123)  # Column name must be a string

    # Test plot_scatter function
    def test_plot_scatter(self):
        # Test with valid numeric columns
        plot_scatter(self.df, 'numeric_col', 'float_col')  # Should plot without errors

        # Test with one non-numeric column
        with self.assertRaises(ValueError):
            plot_scatter(self.df, 'numeric_col', 'string_col')

        # Test with non-existing column
        with self.assertRaises(ValueError):
            plot_scatter(self.df, 'numeric_col', 'nonexistent_col')

        # Test with invalid input
        with self.assertRaises(TypeError):
            plot_scatter("Not a DataFrame", 'numeric_col', 'float_col')

        with self.assertRaises(TypeError):
            plot_scatter(self.df, 'numeric_col', 123)  # Column names must be strings

    # Test check_data_integrity function
    def test_check_data_integrity(self):
        # Test with valid DataFrame
        result = check_data_integrity(self.df)
        self.assertIsInstance(result, dict)
        self.assertIn('missing_values', result)
        self.assertIn('duplicates', result)
        self.assertIn('outliers', result)

        # Test with invalid input
        with self.assertRaises(TypeError):
            check_data_integrity("Not a DataFrame")

    # Test data_quality_report function
    def test_data_quality_report(self):
        # Test with valid DataFrame
        result = data_quality_report(self.df)
        self.assertIsInstance(result, dict)
        self.assertIn('missing_values_summary', result)
        self.assertIn('duplicates_summary', result)
        self.assertIn('outliers_summary', result)

        # Test with invalid input
        with self.assertRaises(TypeError):
            data_quality_report("Not a DataFrame")

if __name__ == '__main__':
    unittest.main()