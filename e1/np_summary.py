# Getting Started with NumPy
import numpy as np

data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

# 1. The lowest total precipitation over the year
total_city = totals.sum(axis=1)
minIndex = total_city.argmin()
print('Row with lowest total precipitation:')
print(minIndex)

# 2. The average precipitation in these locations for each month
total_month = totals.sum(axis=0)
count_month = counts.sum(axis=0)
averages_month = total_month / count_month
print('Average precipitation in each month:')
print(averages_month)

# 3. The average daily precipitation for each city
count_city = counts.sum(axis=1)
averages_city = total_city / count_city
print('Average precipitation in each city:')
print(averages_city)

# 4.  The total precipitation for each quarter in each city
rows = totals.shape[0]
new_totals = totals.reshape(4*rows,3)
total_city_quarter = new_totals.sum(axis=1).reshape(rows,4)
print('Quarterly precipitation totals:')
print(total_city_quarter)
