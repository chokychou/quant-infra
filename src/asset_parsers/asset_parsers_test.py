import os
import unittest
from test.data.data_import_test import load_test_data
import src.asset_parsers.backtest_to_asset_parser as todo


class DataImportTest(unittest.TestCase):

    data_files = load_test_data()

    def test_backtest_to_asset_parser(self):
        NotImplemented


if __name__ == "__main__":
    unittest.main()
