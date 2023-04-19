# import pandas as pd
# import datetime
# from yahoo_fin.stock_info import get_data
# from fredapi import Fred


# class BondData:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.fred = Fred(api_key=self.api_key)

#     def fetch_yahoo_data(self, ticker, start_date, end_date):
#         return get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=True, interval="1d")

#     def fetch_fred_data(self, series_id, start_date, end_date):
#         return pd.DataFrame(self.fred.get_series(series_id, start_date, end_date), columns=[series_id])

#     def print_data(self, data):
#         print(data.head())


# if __name__ == "__main__":
#     api_key = "af08e5017b1a9d6a033648512f73c60c"
#     bond_data = BondData(api_key)

#     start_date = "01/01/1970"
#     end_date = "10/04/2023"

#     AGG_data = bond_data.fetch_yahoo_data("AGG", start_date, end_date)
#     BNDW_data = bond_data.fetch_yahoo_data("BNDW", start_date, end_date)
#     SHY_data = bond_data.fetch_yahoo_data("SHY", start_date, end_date)
#     TLT_data = bond_data.fetch_yahoo_data("TLT", start_date, end_date)
#     LQD_data = bond_data.fetch_yahoo_data("LQD", start_date, end_date)
#     TIP_data = bond_data.fetch_yahoo_data("TIP", start_date, end_date)
#     T5YIE_data = bond_data.fetch_fred_data("T5YIE", start_date, end_date)
#     T10YIE_data = bond_data.fetch_fred_data("T10YIE", start_date, end_date)

#     # Access and manipulate data for each asset using their respective variable names
#     print("AGG Data:")
#     print(AGG_data.head())

#     print("BNDW Data:")
#     print(BNDW_data.head())


# import pandas as pd
# import numpy as np
# from scipy import stats
# import datetime
# from yahoo_fin.stock_info import get_data
# from fredapi import Fred


# class BondData:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.fred = Fred(api_key=self.api_key)

#     def fetch_yahoo_data(self, ticker, start_date, end_date):
#         data = get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=True, interval="1d")
#         return data["adjclose"]

#     def fetch_fred_data(self, series_id, start_date, end_date):
#         data = self.fred.get_series(series_id, start_date, end_date)
#         return pd.Series(data, name=series_id)

#     def check_data(self, data):
#         # Convert data to a numeric dtype
#         data = pd.to_numeric(data, errors="coerce")

#         # Check for null or NaN values
#         if data.isna().values.any():
#             print("The dataset contains null or NaN values.")

#         # Check for non-numerical values
#         elif not pd.api.types.is_numeric_dtype(data):
#             print("The dataset contains non-numerical values.")

#         # Check for outliers using the Z-score method
#         else:
#             z_scores = np.abs(stats.zscore(data))
#             threshold = 3
#             outliers = np.where(z_scores > threshold)
#             if len(outliers[0]) > 0:
#                 print("The dataset contains outliers.")

#         # Print the first few rows of the dataset
#         print(data.head())


# if __name__ == "__main__":
#     api_key = "af08e5017b1a9d6a033648512f73c60c"
#     bond_data = BondData(api_key)

#     start_date = "01/01/1970"
#     end_date = "10/04/2023"

#     AGG_data = bond_data.fetch_yahoo_data("AGG", start_date, end_date)
#     BNDW_data = bond_data.fetch_yahoo_data("BNDW", start_date, end_date)
#     SHY_data = bond_data.fetch_yahoo_data("SHY", start_date, end_date)
#     TLT_data = bond_data.fetch_yahoo_data("TLT", start_date, end_date)
#     LQD_data = bond_data.fetch_yahoo_data("LQD", start_date, end_date)
#     TIP_data = bond_data.fetch_yahoo_data("TIP", start_date, end_date)
#     T5YIE_data = bond_data.fetch_fred_data("T5YIE", start_date, end_date)
#     T10YIE_data = bond_data.fetch_fred_data("T10YIE", start_date, end_date)

#     # Check each dataset for null, NaN, outliers, or non-numerical data:
#     bond_data.check_data(AGG_data)
#     bond_data.check_data(BNDW_data)
#     bond_data.check_data(SHY_data)
#     bond_data.check_data(TLT_data)
#     bond_data.check_data(LQD_data)
#     bond_data.check_data(TIP_data)
#     bond_data.check_data(T5YIE_data)
#     bond_data.check_data(T10YIE_data)


import pandas as pd
import numpy as np
from scipy import stats
import datetime
from yahoo_fin.stock_info import get_data
from fredapi import Fred


class BondData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.fred = Fred(api_key=self.api_key)

    def fetch_yahoo_data(self, ticker, start_date, end_date):
        return get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=True, interval="1d")

    def fetch_fred_data(self, series_id, start_date, end_date):
        return pd.DataFrame(self.fred.get_series(series_id, start_date, end_date), columns=[series_id])

    def check_data(self, data):
        # Check for null or NaN values in open, adjclose, and volume columns
        if data[['open', 'adjclose', 'volume']].isna().values.any():
            print("The dataset contains null or NaN values in open, adjclose, or volume columns.")

        # Check for non-numerical values in open, adjclose, and volume columns
        elif not pd.api.types.is_numeric_dtype(data['open']) or not pd.api.types.is_numeric_dtype(data['adjclose']) or not pd.api.types.is_numeric_dtype(data['volume']):
            print("The dataset contains non-numerical values in open, adjclose, or volume columns.")

        # Check for outliers in open and adjclose columns using the Z-score method
        else:
            z_scores_open = np.abs(stats.zscore(data['open']))
            z_scores_adjclose = np.abs(stats.zscore(data['adjclose']))
            threshold = 3
            outliers_open = np.where(z_scores_open > threshold)
            outliers_adjclose = np.where(z_scores_adjclose > threshold)
            if len(outliers_open[0]) > 0 or len(outliers_adjclose[0]) > 0:
                print("The dataset contains outliers in open or adjclose columns.")

        # Print the first few rows of the dataset
        print(data.head())

if __name__ == "__main__":
    api_key = "af08e5017b1a9d6a033648512f73c60c"
    bond_data = BondData(api_key)

    start_date = "01/01/1970"
    end_date = "10/04/2023"

    AGG_data = bond_data.fetch_yahoo_data("AGG", start_date, end_date)
    BNDW_data = bond_data.fetch_yahoo_data("BNDW", start_date, end_date)
    SHY_data = bond_data.fetch_yahoo_data("SHY", start_date, end_date)
    TLT_data = bond_data.fetch_yahoo_data("TLT", start_date, end_date)
    LQD_data = bond_data.fetch_yahoo_data("LQD", start_date, end_date)
    TIP_data = bond_data.fetch_yahoo_data("TIP", start_date, end_date)

    # Check each dataset for null, NaN, outliers, or non-numerical data in open, adjclose, or volume columns:
    bond_data.check_data(AGG_data)
    bond_data.check_data(BNDW_data)
    bond_data.check_data(SHY_data)
    bond_data.check_data(TLT_data)
    bond_data.check_data(LQD_data)
    bond_data.check_data(TIP_data)


