# Here I am showing DevOps Project Day 2

import os
import re
import collections

# Define the log_directory and log_pattern as before

# Create a dictionary to store log entries by source
log_entries = collections.defaultdict(list)
log_directory = os.getcwd()
log_pattern = r'\[(.*?)\] (.*)'

# Loop through log files in the directory
for filename in os.listdir(log_directory):
    if filename.endswith(".log"):
        with open(os.path.join(log_directory, filename), 'r') as log_file:
            for line in log_file:
                match = re.match(log_pattern, line)
                if match:
                    timestamp, message = match.groups()
                    log_entries[filename].append((timestamp, message))

# Analyze the logs (e.g., count errors)
for source, entries in log_entries.items():
    error_count = sum(1 for timestamp, message in entries if "error" in message.lower())
    print(f"Log source: {source}, Error count: {error_count}")


