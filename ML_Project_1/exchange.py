import pandas as pd
from yahoo_fin import stock_info as si
import numpy as np

# Yen to USD exchange rate data:

def load_exchange_rates(start_date=None, end_date=None, csv_file='ML_Project_1/yen_usd_FRED.csv'):
    exchange_rates = pd.read_csv(csv_file, index_col='Date', parse_dates=True)
    exchange_rates.columns = ['EXJPUS']
    exchange_rates['EXJPUS'] = exchange_rates['EXJPUS'].replace('ND', np.nan).astype(float)
    exchange_rates['EXJPUS'].fillna(method='ffill', inplace=True)

    if start_date and end_date:
        exchange_rates = exchange_rates.loc[start_date:end_date]

    return exchange_rates

def convert_yen_to_usd(yen_data, exchange_rates):
    yen_usd = yen_data.copy()
    exchange_rates = exchange_rates.reindex(yen_usd.index, method='ffill')
    yen_usd['close_usd'] = yen_usd['close'] / (exchange_rates['EXJPUS'])  # Divide the close value by the exchange rate
    yen_usd.drop(columns=['close'], inplace=True)
    return yen_usd




# Euro to USD exchange rate data:

def load_euro_exchange_rates(start_date, end_date, csv_file='euro_to_usd.csv'):
    exchange_rates = pd.read_csv(csv_file, index_col='Date', parse_dates=True)

    start_date = max(exchange_rates.index[-1] + pd.Timedelta(days=1), pd.Timestamp(start_date))

    if start_date <= end_date:
        eur_usd = si.get_data('EURUSD=X', start_date=start_date, end_date=end_date)
        eur_usd = eur_usd[['close']].rename(columns={'close': 'USD'})
        exchange_rates = pd.concat([exchange_rates, eur_usd])

    return exchange_rates

def convert_euro_to_usd(data, exchange_rates):
    data_usd = data.copy()
    data_usd = data_usd.merge(exchange_rates, left_index=True, right_index=True, how='left')
    data_usd['USD'] = data_usd['USD'].interpolate(method='time')  # This line to interpolate missing exchange rate data
    data_usd.iloc[:, 0] = data_usd.iloc[:, 0] * data_usd['USD']
    data_usd.drop(columns=['USD'], inplace=True)
    return data_usd



