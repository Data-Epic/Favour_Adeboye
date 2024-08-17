import unittest
import pandas as pd
from datawrangler.cleaning import drop_missing_data, fill_missing_data, remove_duplicates

class TestCleaning(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': ['a', None, 'c', 'd'],
            'C': [None, 2.5, 3.5, 4.5]
        })

    def test_drop_missing_data(self):
        result = drop_missing_data(self.df, columns=['A'])
        self.assertEqual(result.shape[0], 3)

    def test_fill_missing_data(self):
        result = fill_missing_data(self.df, columns=['B'], value='missing')
        self.assertEqual(result['B'].iloc[1], 'missing')

    def test_remove_duplicates(self):
        df = pd.DataFrame({
            'A': [1, 2, 2, 4],
            'B': ['a', 'b', 'b', 'd']
        })
        result = remove_duplicates(df)
        self.assertEqual(result.shape[0], 3)

if __name__ == '__main__':
    unittest.main()