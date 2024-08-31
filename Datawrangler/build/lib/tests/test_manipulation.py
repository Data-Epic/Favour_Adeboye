import unittest
import pandas as pd
from datawrangler.manipulation import (
    add_new_column,
    filter_rows,
    group_and_aggregate,
    create_interaction_features,
    normalize_features
)

class TestManipulation(unittest.TestCase):

    def setUp(self):
        # Setup a sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': ['foo', 'bar', 'baz', 'qux', 'quux'],
            'D': [10, 15, 20, 25, 30]
        })

    # Test add_new_column function
    def test_add_new_column(self):
        # Test adding a new column with a constant value
        result = add_new_column(self.df, 'E', 10)
        self.assertIn('E', result.columns)
        self.assertTrue((result['E'] == 10).all())

        # Test adding a new column with a list
        result = add_new_column(self.df, 'F', [1, 2, 3, 4, 5])
        self.assertIn('F', result.columns)
        self.assertListEqual(result['F'].tolist(), [1, 2, 3, 4, 5])

        # Test adding a column that already exists
        with self.assertRaises(ValueError):
            add_new_column(self.df, 'A', 10)

        # Test with invalid input
        with self.assertRaises(TypeError):
            add_new_column("Not a DataFrame", 'G', 10)

        with self.assertRaises(TypeError):
            add_new_column(self.df, 123, 10)  # Column name must be a string

    # Test filter_rows function
    def test_filter_rows(self):
        # Test filtering rows with a valid condition
        result = filter_rows(self.df, 'A > 3')
        self.assertEqual(len(result), 2)
        self.assertListEqual(result['A'].tolist(), [4, 5])

        # Test filtering rows with a condition on a string column
        result = filter_rows(self.df, "C == 'foo'")
        self.assertEqual(len(result), 1)
        self.assertEqual(result['C'].tolist()[0], 'foo')

        # Test with invalid condition string
        with self.assertRaises(ValueError):
            filter_rows(self.df, 'invalid condition')

        # Test with invalid input
        with self.assertRaises(TypeError):
            filter_rows("Not a DataFrame", 'A > 3')

        with self.assertRaises(TypeError):
            filter_rows(self.df, 123)  # Condition must be a string

    # Test group_and_aggregate function
    def test_group_and_aggregate(self):
        # Test grouping by one column and aggregating
        agg_dict = {'B': 'mean', 'D': 'sum'}
        result = group_and_aggregate(self.df, ['A'], agg_dict)
        self.assertEqual(len(result), 5)
        self.assertEqual(result.loc[result['A'] == 1, 'B'].values[0], 5)
        self.assertEqual(result.loc[result['A'] == 1, 'D'].values[0], 10)

        # Test grouping by multiple columns
        agg_dict = {'B': 'sum'}
        result = group_and_aggregate(self.df, ['A', 'C'], agg_dict)
        self.assertEqual(len(result), 5)
        self.assertEqual(result.loc[result['A'] == 1, 'B'].values[0], 5)

        # Test with invalid group_by parameter
        with self.assertRaises(TypeError):
            group_and_aggregate(self.df, 'A', agg_dict)  # group_by should be a list

        # Test with non-existent columns
        with self.assertRaises(ValueError):
            group_and_aggregate(self.df, ['nonexistent_column'], agg_dict)

        # Test with invalid aggregation dictionary
        with self.assertRaises(TypeError):
            group_and_aggregate(self.df, ['A'], 'invalid dict')

    # Test create_interaction_features function
    def test_create_interaction_features(self):
        # Test creating interaction features
        result = create_interaction_features(self.df, [('A', 'B')])
        self.assertIn('A_x_B', result.columns)
        self.assertListEqual(result['A_x_B'].tolist(), [5, 8, 9, 8, 5])

        # Test with multiple interaction pairs
        result = create_interaction_features(self.df, [('A', 'B'), ('A', 'D')])
        self.assertIn('A_x_B', result.columns)
        self.assertIn('A_x_D', result.columns)

        # Test with invalid column pairs
        with self.assertRaises(TypeError):
            create_interaction_features(self.df, 'A, B')  # column_pairs should be a list of tuples

        # Test with non-existent columns
        with self.assertRaises(ValueError):
            create_interaction_features(self.df, [('A', 'nonexistent_column')])

    # Test normalize_features function
    def test_normalize_features(self):
        # Test normalizing a numeric column
        result = normalize_features(self.df, ['A'])
        self.assertTrue(result['A'].min() == 0.0)
        self.assertTrue(result['A'].max() == 1.0)

        # Test normalizing multiple columns
        result = normalize_features(self.df, ['A', 'B'])
        self.assertTrue(result['B'].min() == 0.0)
        self.assertTrue(result['B'].max() == 1.0)

        # Test with invalid columns list
        with self.assertRaises(TypeError):
            normalize_features(self.df, 'A')  # columns should be a list

        # Test with non-existent columns
        with self.assertRaises(ValueError):
            normalize_features(self.df, ['nonexistent_column'])

        # Test with non-numeric column
        with self.assertRaises(ValueError):
            normalize_features(self.df, ['C'])  # C is not numeric

if __name__ == '__main__':
    unittest.main()