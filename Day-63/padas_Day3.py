# Here I am showing Pandas Day 3

import pandas as pd

dc = pd.read_csv('data.csv')
print(dc.head(10))


# Analyzing End 10 Data
dc = pd.read_csv('data.csv')
print(dc.tail(10))

# Data Cleaning

# 1.Empty cells
# 2.Data in wrong format
# 3.Wrong data
# 4.Duplicates

dc.dropna(inplace= True)
print(dc.to_string())