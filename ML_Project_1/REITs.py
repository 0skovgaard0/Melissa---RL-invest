# Collecting, Cleaning, and Preprocessing REITs with Yahoo_fin API and auto update it:
from yahoo_fin.stock_info import get_data
import pandas as pd


# Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# AVB (Multi Family properties in the US) data from Yahoo Finance:
AVB_daily = get_data("AVB", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(AVB_daily.head())

# BXP (Class A office properties in major US cities) data from Yahoo Finance:
BXP_daily = get_data("BXP", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(BXP_daily.head())

# SPG (Focused on Shopping malls and Premium outlets) data from Yahoo Finance:
SPG_daily = get_data("SPG", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(SPG_daily.head())

# PLD (Logistics and distribution centers) data from Yahoo Finance:
PLD_daily = get_data("PLD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(PLD_daily.head())

# VTR (healthcare properties, including senior living communities, medical office buildings, and research facilities) data from Yahoo Finance:
VTR_daily = get_data("VTR", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(VTR_daily.head())

# EQIX (Operates data centers across the globe) data from Yahoo Finance:
EQIX_daily = get_data("EQIX", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(EQIX_daily.head())

# DLR (Data centers and digital infrastructure) data from Yahoo Finance:
DLR_daily = get_data("DLR", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")

# WPC (Invests in various property types, including industrial, retail, and office) data from Yahoo Finance:
WPC_daily = get_data("WPC", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(WPC_daily.head())

# VNO (Invests in a mix of office, retail, and residential properties, primarily in New York City) data from Yahoo Finance:
VNO_daily = get_data("VNO", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
print(VNO_daily.head())

