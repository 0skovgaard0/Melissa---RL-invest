# # Collecting, Cleaning, and Preprocessing Crypto currencies with Yahoo_fin API and auto update it:
# from yahoo_fin.stock_info import get_data
# import pandas as pd


# # Start date is set to 1970, as when we want to start tracking and training our Machine "Melissa" even though not all assets have data that far back.
# # BTC-USD (Bitcoin) data from Yahoo Finance:

# BTC_USD_daily = get_data("BTC-USD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(BTC_USD_daily.head())

# # ETH-USD (Ethereum) data from Yahoo Finance:
# ETH_USD_daily = get_data("ETH-USD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(ETH_USD_daily.head())

# # LTC-USD (Litecoin) data from Yahoo Finance:
# LTC_USD_daily = get_data("LTC-USD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(LTC_USD_daily.head())

# # XRP-USD (Ripple) data from Yahoo Finance:
# XRP_USD_daily = get_data("XRP-USD", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(XRP_USD_daily.head())

# # GDLC (The Grayscale Digital Large Cap Fund) data from Yahoo Finance:
# GDLC_daily = get_data("GDLC", start_date="01/01/1970", end_date="10/04/2023", index_as_date = True, interval="1d")
# print(GDLC_daily.head())


import pandas as pd
from yahoo_fin.stock_info import get_data


class CryptoData:
    def __init__(self):
        pass

    def fetch_crypto_data(self, ticker, start_date, end_date):
        return get_data(ticker, start_date=start_date, end_date=end_date, index_as_date=True, interval="1d")

    def print_data(self, data):
        print(data.head())


if __name__ == "__main__":
    crypto_data = CryptoData()

    start_date = "01/01/1970"
    end_date = "10/04/2023"

    tickers_crypto = ["BTC-USD", "ETH-USD", "LTC-USD", "XRP-USD", "GDLC"]

    for ticker in tickers_crypto:
        data = crypto_data.fetch_crypto_data(ticker, start_date, end_date)
        crypto_data.print_data(data)

