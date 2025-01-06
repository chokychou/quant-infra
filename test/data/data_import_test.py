""" Data Import Test

Souce -> 1000_options_minutes_data
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 51840 entries, 0 to 51839
Data columns (total 21 columns):
#   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
0   order_book_id   51840 non-null  object        
1   datetime        51840 non-null  datetime64[ns]
2   open_interest   51840 non-null  float64       
3   total_turnover  51840 non-null  float64       
4   close           51840 non-null  float64       
5   high            51840 non-null  float64       
6   low             51840 non-null  float64       
7   volume          51840 non-null  float64       
8   trading_date    51840 non-null  datetime64[ns]
9   open            51840 non-null  float64       
10  option_type     51840 non-null  object        
11  mulitiplier     0 non-null      object        
12  strike_price    51840 non-null  float64       
13  maturity_date   51840 non-null  object        
14  margin          51840 non-null  int64         
15  delta           51840 non-null  float64       
16  gamma           51840 non-null  float64       
17  theta           51840 non-null  float64       
18  vega            51840 non-null  float64       
19  rho             51840 non-null  float64       
20  multiplier      51840 non-null  float64       
dtypes: datetime64[ns](2), float64(14), int64(1), object(4)
memory usage: 8.3+ MB
None

DataFrame description for 1000_options_minutes_data/minute_2022-09-21:
                datetime  open_interest  ...           rho  multiplier
count                51840   51840.000000  ...  51840.000000     51840.0
mean   2022-09-21 12:15:30     205.594734  ...     12.730378       100.0
min    2022-09-21 09:31:00       1.000000  ...  -4143.096558       100.0
25%    2022-09-21 10:30:45      28.000000  ...   -766.404569       100.0
50%    2022-09-21 12:15:30      65.000000  ...     -6.079868       100.0
75%    2022-09-21 14:00:15     180.000000  ...    665.544052       100.0
max    2022-09-21 15:00:00    2237.000000  ...   4070.629495       100.0
std                    NaN     357.359912  ...   1474.601169         0.0

[8 rows x 17 columns]
"""

import numpy as np 
import pandas as pd
import pyarrow as pa
import os
import unittest


def load_test_data():
    """Load test data from test/data directory."""
    data_dir = os.path.join(os.path.dirname(__file__))
    data_files = {}
    
    if os.path.exists(data_dir):
        for root, _, files in os.walk(data_dir):
            for filename in files:
                if filename.endswith('.feather'):
                    file_path = os.path.join(root, filename)
                    # Create relative path from data_dir for the dictionary key
                    rel_path = os.path.relpath(file_path, data_dir)
                    name = os.path.splitext(rel_path)[0]
                    data_files[name] = pd.read_feather(file_path)
                
    return data_files

class DataImportTest(unittest.TestCase):
    def test_load_test_data(self):
        """Test that test data can be loaded correctly. Verify each dataframe is not empty, has unique indices, and is a pandas DataFrame."""
        data_files = load_test_data()

        assert len(data_files) > 0, "No test data files loaded"
        assert isinstance(data_files, dict)
        
        for name, df in data_files.items():
            assert isinstance(df, pd.DataFrame), f"{name} is not a pandas DataFrame"
            assert not df.empty, f"{name} DataFrame is empty"
            assert df.index.is_unique, f"{name} has duplicate indices"


if __name__ == "__main__":
    unittest.main()
