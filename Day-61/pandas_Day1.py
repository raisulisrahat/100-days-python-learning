# Here I am showing Pandas Day 1

import pandas as pd

arr = [1,2,3,4]
newarr = pd.Series(arr, index=['a','b','c','d'])
print(newarr)

print(newarr[['a', 'b']])

data = {
    'Name':['Rahat', 'Opi', 'Sakib'],
    'Age':[24, 23, 25]
}
df = pd.DataFrame(data, index=['i', 'ii', 'iii'])
print(df)

print(df.loc[['i']])