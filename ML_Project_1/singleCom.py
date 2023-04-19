# We will explore Yahoo_fin API to get data Financial data from Yahoo and auto update it:
from yahoo_fin.stock_info import get_data
import pandas as pd


# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# CL=F (Crude Oil) data from Yahoo Finance:
Crude_Oil_daily = get_data("CL=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Crude_Oil_daily.head())

# GC=F (Gold) data from Yahoo Finance:
Gold_daily = get_data("GC=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Gold_daily.head())

# SI=F (Silver) data from Yahoo Finance:
Silver_daily = get_data("SI=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Silver_daily.head())

# HG=F (Copper) data from Yahoo Finance:
Copper_daily = get_data("HG=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Copper_daily.head())

# ALI=F (Aluminum) data from Yahoo Finance:
Aluminum_daily = get_data("ALI=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Aluminum_daily.head())

# ZC=F (Corn) data from Yahoo Finance:
Corn_daily = get_data("ZC=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Corn_daily.head())

# ZS=F (Soybeans) data from Yahoo Finance:
Soybeans_daily = get_data("ZS=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Soybeans_daily.head())

# KC=F (Coffee) data from Yahoo Finance:
Coffee_daily = get_data("KC=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Coffee_daily.head())

# CC=F (Cocoa) data from Yahoo Finance:
Cocoa_daily = get_data("CC=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Cocoa_daily.head())

# SB=F (Sugar) data from Yahoo Finance:
Sugar_daily = get_data("SB=F", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(Sugar_daily.head())

