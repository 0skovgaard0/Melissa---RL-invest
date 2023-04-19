# We will explore Yahoo_fin API to get data Financial data from Yahoo and auto update it:
from yahoo_fin.stock_info import get_data
import pandas as pd


# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# Collecting the S&P 500 data from Yahoo Finance:
sp500_daily = get_data("^GSPC", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(sp500_daily.head())

# ^RUT (Russell 2000) data from Yahoo Finance:
RUT2000_daily = get_data("^RUT", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(RUT2000_daily.head())

# ^IXIC (NASDAQ Composite) data from Yahoo Finance:
IXIC_daily = get_data("^IXIC", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(IXIC_daily.head())

# Amazon stock data from Yahoo Finance:
# amazon_weekly= get_data("amzn", start_date="15/05/1997", end_date="12/04/2019", index_as_date = True, interval="1mo")
# print(amazon_weekly.head())