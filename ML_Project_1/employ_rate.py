# Collecting, Cleaning, and Preprocessing Bonds with Yahoo_fin API and auto update it:
from fredapi import Fred
import datetime
import pandas as pd

# Set API key and create a Fred instance
api_key = "af08e5017b1a9d6a033648512f73c60c"
fred = Fred(api_key=api_key)

# Set start and end dates
start_date = datetime.date(1970, 1, 1)
end_date = datetime.date(2023, 10, 4)

# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# UNRATE (Unemployment Rate) data from FRED
UNRATE_daily = pd.DataFrame(fred.get_series("UNRATE", start_date, end_date), columns=["UNRATE"])
print("\nData for Unemployment Rate:")
print(UNRATE_daily.head())

# LREM64TTUSM156S (Employment Rate: Aged 15-64: All Persons for the United States) data from FRED:
LREM64TTUSM156S_daily = pd.DataFrame(fred.get_series("LREM64TTUSM156S", start_date, end_date), columns=["LREM64TTUSM156S"])
print("\nData for Employment Rate:")
print(LREM64TTUSM156S_daily.head())