# Here I am showing Pandas Day 6


import pandas as pd

df = pd.read_csv("Sheet1.csv", index_col="Class")
print(df)



import pandas as pd

df = pd.read_csv("Sheet1.csv", index_col="Class")
d = df["Subject Division"]
print(d)
