import pandas as pd
import os

script_dir = os.getcwd()
print(script_dir)
# cars = pd.read_csv(os.path.normcase(os.path.join(script_dir, 'cars.csv')))
# /Users/james/dev/python/learningPython/cars.csv
cars = pd.read_csv('/Users/james/dev/python/learningPython/cars.csv')
print(cars)

# Print out country column as Pandas Series
print(cars['brand'])

# Print out country column as Pandas DataFrame
print(cars[['brand']])

# Print out DataFrame with country and drives_right columns
# print(cars[['brand', 'year']])