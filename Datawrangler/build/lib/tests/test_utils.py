import unittest
import pandas as pd
import os
from datawrangler.utils import load_data, save_cleaned_data, log_changes

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Setup for testing
        self.csv_file = 'test_data.csv'
        self.excel_file = 'test_data.xlsx'
        self.json_file = 'test_data.json'
        self.sql_file = 'test_data.sqlite'
        self.log_file = 'test_log.log'
        self.data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        
        # Create test files
        self.data.to_csv(self.csv_file, index=False)
        self.data.to_excel(self.excel_file, index=False)

    def tearDown(self):
        # Clean up after testing
        for file in [self.csv_file, self.excel_file, self.json_file, self.sql_file, self.log_file]:
            if os.path.exists(file):
                os.remove(file)

    # Test load_data function
    def test_load_data_csv(self):
        # Test loading a CSV file
        result = load_data(self.csv_file, file_type='csv')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(result.shape, (3, 2))  # Should match the test data shape

    def test_load_data_excel(self):
        # Test loading an Excel file
        result = load_data(self.excel_file, file_type='excel')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(result.shape, (3, 2))  # Should match the test data shape

    def test_load_data_file_not_found(self):
        # Test loading a file that doesn't exist
        with self.assertRaises(FileNotFoundError):
            load_data('nonexistent_file.csv', file_type='csv')

    def test_load_data_invalid_type(self):
        # Test with an unsupported file type
        with self.assertRaises(ValueError):
            load_data(self.csv_file, file_type='unsupported')

    # Test save_cleaned_data function
    def test_save_cleaned_data_csv(self):
        # Test saving to CSV
        save_cleaned_data(self.data, self.csv_file, file_format='csv')
        self.assertTrue(os.path.exists(self.csv_file))

    def test_save_cleaned_data_excel(self):
        # Test saving to Excel
        save_cleaned_data(self.data, self.excel_file, file_format='excel')
        self.assertTrue(os.path.exists(self.excel_file))

    def test_save_cleaned_data_json(self):
        # Test saving to JSON
        save_cleaned_data(self.data, self.json_file, file_format='json')
        self.assertTrue(os.path.exists(self.json_file))

    def test_save_cleaned_data_sql(self):
        # Test saving to SQL
        save_cleaned_data(self.data, self.sql_file, file_format='sql')
        self.assertTrue(os.path.exists(self.sql_file))

    def test_save_cleaned_data_invalid_format(self):
        # Test with an unsupported file format
        with self.assertRaises(ValueError):
            save_cleaned_data(self.data, 'test.txt', file_format='txt')

    # Test log_changes function
    def test_log_changes(self):
        # Test logging a change
        log_changes("Test log entry", self.log_file)
        with open(self.log_file, 'r') as log:
            content = log.read()
        self.assertIn("Test log entry", content)

    def test_log_changes_invalid_log_file(self):
        # Test with a non-string log file path
        with self.assertRaises(TypeError):
            log_changes("Test log entry", log_file=123)

if __name__ == '__main__':
    unittest.main()