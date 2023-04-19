import wbgapi as wb

# Define the series, countries, and time period
series = ['NY.GDP.MKTP.CD', 'NY.GDP.MKTP.KD.ZG']
countries = ['BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'ITA', 'JPN', 'GBR', 'USA']
years = range(1970, 2023)

# Fetch the data as a pandas DataFrame
data = wb.data.DataFrame(series, countries, time=years)

# Print the resulting data
print(data.head(20))
