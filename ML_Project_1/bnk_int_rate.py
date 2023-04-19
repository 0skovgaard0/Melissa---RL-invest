# # # Collecting, Cleaning, and Preprocessing Bank Interest Rates with FRED (Federal Reserve Economic Data) API and auto update it:
# from fredapi import Fred
# import datetime
# import pandas as pd


# # Set API key and create a Fred instance
# api_key = "af08e5017b1a9d6a033648512f73c60c"
# fred = Fred(api_key=api_key)

# # Set start and end dates
# start_date = datetime.date(1970, 1, 1)
# end_date = datetime.date(2023, 10, 4)

# # Retrieve data for each series
# series_ids = ["LIOR3M", "FEDFUNDS", "GS10", "GS2", "DTB3"]

# # Fetch data for LIOR3M from FRED
# LIOR3M_data = pd.DataFrame(fred.get_series("LIOR3M", start_date, end_date), columns=["LIOR3M"])
# print("Data for 3-Month LIBOR based on USD (LIOR3M):")
# print(LIOR3M_data.head())

# # Fetch data for FEDFUNDS from FRED
# FEDFUNDS_data = pd.DataFrame(fred.get_series("FEDFUNDS", start_date, end_date), columns=["FEDFUNDS"])
# print("\nData for Effective Federal Funds Rate:")
# print(FEDFUNDS_data.head())

# # Fetch data for GS10 from FRED
# GS10_data = pd.DataFrame(fred.get_series("GS10", start_date, end_date), columns=["GS10"])
# print("\nData for 10-Year Treasury Constant Maturity Rate:")
# print(GS10_data.head())

# # Fetch data for GS2 from FRED
# GS2_data = pd.DataFrame(fred.get_series("GS2", start_date, end_date), columns=["GS2"])
# print("\nData for 2-Year Treasury Constant Maturity Rate:")
# print(GS2_data.head())

# # Fetch data for DTB3 from FRED
# DTB3_data = pd.DataFrame(fred.get_series("DTB3", start_date, end_date), columns=["DTB3"])
# print("\nData for 3-Month Treasury Bill Rate:")
# print(DTB3_data.head())

# # Fetch data for ECB Main Refinancing Operations Rate from FRED
# ECB_rate_data = pd.DataFrame(fred.get_series("IRSTCI01EZM156N", start_date, end_date), columns=["IRSTCI01EZM156N"])
# print("Data for European Central Bank (ECB) Main Refinancing Operations Rate:")
# print(ECB_rate_data.head()) 

# # Fetch data for BoJ Policy Rate from FRED
# BoJ_rate_data = pd.DataFrame(fred.get_series("IRSTCB01JPM156N", start_date, end_date), columns=["IRSTCB01JPM156N"])
# print("\nData for Bank of Japan (BoJ) Policy Rate:")
# print(BoJ_rate_data.head())

from fredapi import Fred
import pandas as pd
import numpy as np
from scipy import stats
import datetime


class BankData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.fred = Fred(api_key=self.api_key)
        self.series_ids = ["LIOR3M", "FEDFUNDS", "GS10", "GS2", "DTB3", "T5YIE", "T10YIE"]
        self.data = {}

    def fetch_data(self):
        start_date = datetime.date(1970, 1, 1)
        end_date = datetime.date.today()

        for series_id in self.series_ids:
            if series_id in ["LIOR3M", "FEDFUNDS", "GS10", "GS2", "DTB3"]:
                self.data[series_id] = pd.DataFrame(self.fred.get_series(series_id, start_date, end_date),
                                                    columns=[series_id])
            else:
                self.data[series_id] = pd.DataFrame(self.fred.get_series(series_id, start_date, end_date),
                                                    columns=[series_id], dtype=np.float64)

    def clean_data(self):
        for series_id in self.series_ids:
            data = self.data[series_id]

            # Check for null or NaN values
            if data.isna().values.any():
                print("The dataset for", series_id, "contains null or NaN values.")

            # Check for non-numerical values
            elif not data.apply(pd.to_numeric, errors='coerce').notnull().values.all():
                print("The dataset for", series_id, "contains non-numerical values.")

            # Check for outliers using the Z-score method
            else:
                z_scores = np.abs(stats.zscore(data))
                threshold = 3
                outliers = np.where(z_scores > threshold)
                if len(outliers[0]) > 0:
                    print("The dataset for", series_id, "contains outliers.")

    def print_data(self):
        total_rows = sum(len(data) for data in self.data.values())
        total_cols = sum(len(data.columns) for data in self.data.values())
        return total_rows, total_cols

if __name__ == "__main__":
    api_key = "af08e5017b1a9d6a033648512f73c60c"
    bank_data = BankData(api_key)

    # Fetch data for all series
    bank_data.fetch_data()

    # Clean and check data for all series
    bank_data.clean_data()

    # Print data for all series
    total_rows, total_cols = bank_data.print_data()
    print(f"Total rows: {total_rows}, Total columns: {total_cols}")
