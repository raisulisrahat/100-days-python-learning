# Here I am showing Problem Solve Day 5

# System Information Reporting:
# Build a system information reporting tool that collects data about the system's hardware, software, and network configuration using the platform and os modules. The tool can generate detailed reports for system administrators.

import os
import platform
import socket
import psutil

# Function to get system information
def get_system_info():
    system_info = {}

    # Operating System Information
    system_info['OS'] = platform.system()
    system_info['OS Version'] = platform.version()
    system_info['OS Release'] = platform.release()

    # System Hostname
    system_info['Hostname'] = socket.gethostname()

    # Hardware Information
    system_info['Processor'] = platform.processor()
    system_info['CPU Cores'] = os.cpu_count()
    system_info['Architecture'] = platform.architecture()
    system_info['Memory (RAM)'] = round(psutil.virtual_memory().total / (1024. ** 3), 2)  # in GB

    # Network Information
    system_info['Local IP Address'] = socket.gethostbyname(socket.gethostname())

    return system_info

# Generate and print the system information report
if __name__ == "__main__":
    system_info = get_system_info()

    print("System Information Report")
    print("----------------------------")
    for key, value in system_info.items():
        print(f"{key}: {value}")
