import unittest
import pandas as pd
from datawrangler.manipulation import add_new_column, filter_rows, group_and_aggregate

class TestManipulation(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': ['a', 'b', 'c', 'd'],
            'C': [2.5, 3.5, 4.5, 5.5]
        })

    def test_add_new_column(self):
        result = add_new_column(self.df, 'D', 0)
        self.assertIn('D', result.columns)

        with self.assertRaises(TypeError):
            add_new_column("Not a DataFrame", 'D', 0)

        with self.assertRaises(TypeError):
            add_new_column(self.df, 5, 0)

        with self.assertRaises(ValueError):
            add_new_column(self.df, 'A', 0)

    def test_filter_rows(self):

        result = filter_rows(self.df, 'A > 2')
        self.assertEqual(result.shape[0], 2)

        with self.assertRaises(TypeError):
            filter_rows("Not a DataFrame", 'A > 2')

        with self.assertRaises(TypeError):
            filter_rows(self.df, 5)

        with self.assertRaises(ValueError):
            filter_rows(self.df, 'invalid condition')

    def test_group_and_aggregate(self):
        df = pd.DataFrame({
            'A': ['foo', 'foo', 'bar', 'bar'],
            'B': ['one', 'two', 'one', 'two'],
            'C': [1, 2, 3, 4],
            'D': [10, 20, 30, 40]
        })
 
        result = group_and_aggregate(df, group_by=['A', 'B'], agg_dict={'C': 'sum', 'D': 'mean'})
        self.assertEqual(result.shape[0], 4)
   
        with self.assertRaises(TypeError):
            group_and_aggregate("Not a DataFrame", group_by=['A'], agg_dict={'C': 'sum'})

        with self.assertRaises(TypeError):
            group_and_aggregate(df, group_by='A', agg_dict={'C': 'sum'})
     
        with self.assertRaises(TypeError):
            group_and_aggregate(df, group_by=['A'], agg_dict=['C', 'sum'])

        with self.assertRaises(ValueError):
            group_and_aggregate(df, group_by=['Z'], agg_dict={'C': 'sum'})

if __name__ == '__main__':
    unittest.main()
