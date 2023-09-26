# Here I am showing Pandas Day 7

import pandas as pd
import numpy as np

# Read the CSV data into a DataFrame
df = pd.read_csv('Sheet1.csv')

# Add a 'GPA' column to the DataFrame
df['GPA'] = [5, 5, 4.7, 4, 4.2, 4.7, 4.5, 4.8, 4.7, 4.7]

# Display the entire DataFrame
print(df)

# Calculate and print basic statistics for the 'GPA' column
print("GPA Statistics:")
print(df['GPA'].describe())

# Filter rows based on a condition (e.g., GPA greater than 4.5)
filtered_df = df[df['GPA'] > 4.5]
print("Filtered DataFrame:")
print(filtered_df)

# Group the DataFrame by the 'Class' column and calculate the mean GPA for each class
class_mean_gpa = df.groupby('Class')['GPA'].mean()
print("Mean GPA by Class:")
print(class_mean_gpa)

# Save the modified DataFrame to a new CSV file
df.to_csv('New_Sheet1.csv', index=False)