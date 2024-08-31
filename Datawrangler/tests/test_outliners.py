import unittest
import pandas as pd
import numpy as np
from datawrangler.outliners import (
    detect_outliers,
    remove_outliers,
    cap_outliers,
    replace_outliers
)

class TestOutliners(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 100],  # Outlier in A
            'B': [1, 2, 2, 2, 2],
            'C': [1.0, 2.0, 3.0, 4.0, 5.0],  # No outliers
            'D': [10, 12, 13, 14, 1000]  # Outlier in D
        })

    # Test detect_outliers function
    def test_detect_outliers(self):
        # Test with IQR method
        result = detect_outliers(self.df, method='IQR')
        self.assertIn('A', result)
        self.assertIn('D', result)
        self.assertEqual(list(result['A']), [4])  # Outlier index for column A
        self.assertEqual(list(result['D']), [4])  # Outlier index for column D

        # Test with Z-score method
        result = detect_outliers(self.df, method='Z-score')
        self.assertIn('A', result)
        self.assertIn('D', result)
        self.assertEqual(list(result['A']), [4])  # Outlier index for column A
        self.assertEqual(list(result['D']), [4])  # Outlier index for column D

        # Test with non-existent method
        with self.assertRaises(ValueError):
            detect_outliers(self.df, method='invalid_method')

        # Test with invalid input
        with self.assertRaises(TypeError):
            detect_outliers("Not a DataFrame", method='IQR')

    # Test remove_outliers function
    def test_remove_outliers(self):
        # Test removing outliers with IQR method
        result = remove_outliers(self.df.copy(), method='IQR')
        self.assertEqual(len(result), 3)  # Outliers should be removed

        # Test removing outliers with Z-score method
        result = remove_outliers(self.df.copy(), method='Z-score')
        self.assertEqual(len(result), 3)  # Outliers should be removed

        # Test with non-existent method
        with self.assertRaises(ValueError):
            remove_outliers(self.df.copy(), method='invalid_method')

        # Test with invalid input
        with self.assertRaises(TypeError):
            remove_outliers("Not a DataFrame", method='IQR')

    # Test cap_outliers function
    def test_cap_outliers(self):
        # Test capping outliers with IQR method
        result = cap_outliers(self.df.copy(), method='IQR')
        self.assertNotIn(100, result['A'])  # Outlier should be capped
        self.assertNotIn(1000, result['D'])  # Outlier should be capped

        # Test with non-existent method (should raise ValueError)
        with self.assertRaises(ValueError):
            cap_outliers(self.df.copy(), method='Z-score')  # Currently supports only 'IQR'

        # Test with invalid input
        with self.assertRaises(TypeError):
            cap_outliers("Not a DataFrame", method='IQR')

    # Test replace_outliers function
    def test_replace_outliers(self):
        # Test replacing outliers with median
        result = replace_outliers(self.df.copy(), method='median')
        self.assertEqual(result['A'][4], self.df['A'][:4].median())  # Outlier replaced with median
        self.assertEqual(result['D'][4], self.df['D'][:4].median())  # Outlier replaced with median

        # Test replacing outliers with mean
        result = replace_outliers(self.df.copy(), method='mean')
        self.assertEqual(result['A'][4], self.df['A'][:4].mean())  # Outlier replaced with mean
        self.assertEqual(result['D'][4], self.df['D'][:4].mean())  # Outlier replaced with mean

        # Test with non-existent method
        with self.assertRaises(ValueError):
            replace_outliers(self.df.copy(), method='invalid_method')

        # Test with invalid input
        with self.assertRaises(TypeError):
            replace_outliers("Not a DataFrame", method='median')

if __name__ == '__main__':
    unittest.main()