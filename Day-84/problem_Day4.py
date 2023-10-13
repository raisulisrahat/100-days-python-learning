# Here I am showing Problem Solve Day 4

# Parsing Custom Log Files:
# Create a Python script that reads and parses log files with custom log entry formats. Use regex to extract relevant information from log entries and organize them into a structured Pandas DataFrame.

import re
import pandas as pd

# Define the log entry format
log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'

# Create an empty list to store log data
log_data = []

# Open and read the log file
with open('custom_log.txt', 'r') as log_file:
    for line in log_file:
        match = re.match(log_pattern, line)
        if match:
            timestamp, log_level, message = match.groups()
            log_data.append([timestamp, log_level, message])

# Create a Pandas DataFrame from the log data
df = pd.DataFrame(log_data, columns=['Timestamp', 'Log Level', 'Message'])

# Convert the 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Print the DataFrame
print(df)
