import unittest
import pandas as pd
from data_validation import DataValidation

class TestData(unittest.TestCase):
    def test_missing_values(self):
        #list of lists
        data = {'required_col': ['a1', 'a2', 'a3'],
        'optional_col': ['b1', 'b2', 'b3'],
        'optional_col_2': ['c1', 'c2', 'c3']}
        df = pd.DataFrame(data)
        data_test =  DataValidation(df)
        actual_missing_values = data_test.get_missing_values(column = "required_col")
        expected_missing_values = 0
        assert actual_missing_values == expected_missing_values

    def test_missing_values(self):
        #list of lists
        data = {'required_col': ['a1', 'a1', 'a1'],
        'optional_col': ['b1', 'b2', 'b3'],
        'optional_col_2': ['c1', 'c2', 'c3']}
        df = pd.DataFrame(data)
        data_test =  DataValidation(df)
        actual_duplicate_values = data_test.get_unique_values(column = "required_col")
        expected_duplicate_values = 1
        assert actual_duplicate_values == expected_duplicate_values
