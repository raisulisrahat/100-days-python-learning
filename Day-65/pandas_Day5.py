# Here I am showing Pandas Day 5

import pandas as pd

df = pd.read_csv("Sheet1.csv")
print(df)

# Create a new DataFrame with the desired data
new_data = {
    'Roll': [11, 12, 13],
    'Name': ['K', 'L', 'M'],
    'Class': ['XI', 'XI', 'XI'],
    'Subject Division': ['Commerce', 'Arts', 'Science']
}
newdf = pd.DataFrame(new_data)

# Save the new DataFrame to a new CSV file (optional)
newdf.to_csv("new_data.csv", index=False)

# Select columns of boolean data type in the new DataFrame
bool_data = newdf.select_dtypes(include=bool)
print("Boolean Data:")
print(bool_data)

# Select columns excluding int64 data type in the new DataFrame
int_data = newdf.select_dtypes(exclude=['int64'])
print("Non-integer Data:")
print(int_data)