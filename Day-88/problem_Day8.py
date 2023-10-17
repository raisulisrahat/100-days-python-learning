# Here I am showing Problem Solve Day 8

# Exception Handling and Recovery:
# Implement a Python script that monitors system errors and exceptions, such as unhandled crashes. When an exception occurs, the script should automatically recover or restart the affected process. Use the sys module to catch exceptions and subprocess to restart processes
import subprocess
import time

# Define the process to monitor and its command
process_command = "ping www.google.com"

def run_process():
    try:
        # Start the process
        process = subprocess.Popen(process_command, shell=True)
        process.wait()
    except Exception as e:
        print(f"Exception occurred: {e}")
        # Implement recovery logic here (e.g., restarting the process)

def main():
    while True:
        try:
            run_process()
        except Exception as e:
            print(f"Recovery failed: {e}")
        # Wait for a while before attempting to restart the process
        time.sleep(10)

if __name__ == "__main__":
    main()
