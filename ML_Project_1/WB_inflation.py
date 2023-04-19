# We will import the WB_inflation.CSV file and modify the date to be useful for our Melissa's RL Machine project:
# Let's use wbgapi to collect Inflation, consumer prices (annual %) (FP.CPI.TOTL.ZG) data from The World Bank:
import wbgapi as wb

# Get the data for the series FP.CPI.TOTL.ZG, define country, series, and year range:
series = ['FP.CPI.TOTL.ZG']
countries = ['BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'ITA', 'JPN', 'GBR', 'USA']
years = range(1970, 2023)

# Fetch the data as a pandas DataFrame
data = wb.data.DataFrame(series, countries, time=years)

# Print the resulting data
print(data.head(10))

