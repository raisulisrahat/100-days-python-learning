# Here I am showing Pandas Day 2

import pandas as pd

# Read CSV data
dc = pd.read_csv('data.csv')
print(dc.to_string())

# Read Json data
dj = pd.read_json('data.json')
print(dj.to_string())