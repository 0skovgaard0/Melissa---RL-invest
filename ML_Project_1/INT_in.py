# Collecting, Cleaning, and Preprocessing International indicies with Yahoo_fin API and auto update it:
from yahoo_fin.stock_info import get_data
from yahoo_fin import stock_info as si
import pandas as pd
from exchange import load_exchange_rates, convert_yen_to_usd, load_euro_exchange_rates, convert_euro_to_usd
from datetime import datetime, date


# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# MSCI (large and mid-cap equities across 23 developed markets countries) data from Yahoo Finance:
MSCI_daily = get_data("MSCI", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(MSCI_daily.head())

# EEM (large and mid-cap equities across 26 emerging markets countries) data from Yahoo Finance:
EEM_daily = get_data("EEM", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(EEM_daily.head())

# VEU (large and mid-cap equities in developed and emerging markets) data from Yahoo Finance:
VEU_daily = get_data("VEU", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(VEU_daily.head())

# IOO (S&P Global 100) data from Yahoo Finance:
IOO_daily = get_data("IOO", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(IOO_daily.head())

# DGT (Dow Jones Global Titans 50 Index) data from Yahoo Finance:
DGT_daily = get_data("DGT", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(DGT_daily.head())


# Load exchange rates (from exchange.py)
exchange_rates_yen = load_exchange_rates(datetime.strptime("1970-01-01", '%Y-%m-%d'), datetime.strptime("2023-10-04", '%Y-%m-%d'))

# ^N300 (Nikkei 300) data from Yahoo Finance: THIS ONE IS IN JAPANESE YEN
N300_daily = si.get_data("^N300", start_date="01/01/1970", end_date="10/04/2023", index_as_date=True, interval="1d")
print(N300_daily.head())

# Convert N300 data to USD
N300_daily_usd = convert_yen_to_usd(N300_daily[['close']], exchange_rates_yen)
N300_daily_usd.rename(columns={"close_usd": "close"}, inplace=True)
print("\nData for Nikkei 300 in USD:")
print(N300_daily_usd.head())

# ^N225 (Nikkei 225) data from Yahoo Finance: THIS ONE IS IN JAPANESE YEN
N225_daily = si.get_data("^N225", start_date="04/01/1971", end_date="10/04/2023", index_as_date=True, interval="1d")
print(N225_daily.head())

# Convert N225 data to USD
N225_daily_usd = convert_yen_to_usd(N225_daily[['close']], exchange_rates_yen)
N225_daily_usd.rename(columns={"close_usd": "close"}, inplace=True)
print("\nData for Nikkei 225 in USD:")
print(N225_daily_usd.head())


# Setting a local start date for the "stoxx_start_date", as this is when we have currency conversion data for EUR to USD
stoxx_start_date = pd.Timestamp(date(1999, 1, 4))
stoxx_end_date = pd.Timestamp(date(2023, 10, 4))

# ^STOXX (Stoxx Europe 600) data from Yahoo Finance: THIS ONE IS IN EURO
STOXX_daily = get_data("^STOXX", start_date=stoxx_start_date, end_date=stoxx_end_date, index_as_date=True, interval="1d")
# print("\nData for Stoxx Europe 600:")
# print(STOXX_daily.head())

# Load exchange rates (from exchange.py)
exchange_rates_euro = load_euro_exchange_rates(stoxx_start_date, stoxx_end_date)

# Convert STOXX data to USD
STOXX_daily_usd = convert_euro_to_usd(STOXX_daily[['close']], exchange_rates_euro)
STOXX_daily_usd.rename(columns={"close": "close_usd"}, inplace=True)
# print("\nData for Stoxx Europe 600 in USD:")
# print(STOXX_daily_usd.head())

