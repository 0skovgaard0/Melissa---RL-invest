# Collecting, Cleaning, and Preprocessing EFT Commodities with Yahoo_fin API and auto update it:
from yahoo_fin.stock_info import get_data
import pandas as pd

# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# USO (crude oil futures) data from Yahoo Finance:
USO_daily = get_data("USO", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(USO_daily.head())

# GLD (Gold) data from Yahoo Finance:
GLD_daily = get_data("GLD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(GLD_daily.head())

# SLV (Silver) data from Yahoo Finance:
SLV_daily = get_data("SLV", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(SLV_daily.head())

# DBB (industrial metals, such as aluminum, copper, and zinc) data from Yahoo Finance:
DBB_daily = get_data("DBB", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(DBB_daily.head())

# DBA (agricultural commodities, such as corn, soybeans, wheat, and sugar) data from Yahoo Finance:
DBA_daily = get_data("DBA", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(DBA_daily.head())

# GSG (commodities across energy, metals, and agriculture sectors) data from Yahoo Finance:
GSG_daily = get_data("GSG", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(GSG_daily.head())


