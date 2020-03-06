# Getting Started with Pandas
import pandas as pd

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# 1. The lowest total precipitation over the year
total_city = totals.sum(axis=1)
minCity = total_city.idxmin()
print('City with lowest total precipitation:')
print(minCity)

# 2. The average precipitation in these locations for each month
total_month = totals.sum(axis=0)
count_month = counts.sum(axis=0)
averages_month = total_month / count_month
print(averages_month)

# 3. The average daily precipitation for each city
count_city = counts.sum(axis=1)
averages_city = total_city / count_city
print(averages_city)