import os
import unittest
from test.data.data_import_test import load_test_data
import src.asset_parsers.backtest_to_asset_parser as todo


class DataImportTest(unittest.TestCase):

    data_files = load_test_data()

    def test_backtest_to_asset_parser(self):
        for name, df in self.data_files.items():
            print(df.order_book_id)
        assert False


if __name__ == "__main__":
    unittest.main()
