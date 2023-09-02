# Here I am showing OS modules

import os

# Get and print the process ID (PID)
pid = os.getpid()
print(f"Your PID is: {pid}")

# Create a folder with user input
folder_name = input("Enter a folder name: ")
os.mkdir(folder_name)
print(f"Folder '{folder_name}' created successfully.")

# Get and print the system information
system_info = os.system('version')
print(f"Your system information is: {system_info}")

# Get and print the current login username
login = os.getlogin()
print(f"You are logged in as: {login}")
