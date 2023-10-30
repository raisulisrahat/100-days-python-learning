# 
import psutil
import time

# Simulating a deployment process (Replace with actual deployment logic)
def deploy_application():
    print("Deploying application...")

    # Simulating deployment time
    time.sleep(3)
    print("Application deployed successfully.")

# Function to monitor system resources
def monitor_system():
    while True:
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        print(f"Current CPU usage: {cpu_percent}%")
        print(f"Current Memory usage: {memory_percent}%")
        print(f"Current Disk usage: {disk_usage}%")

        # Example: Trigger deployment if CPU usage is below 10% and memory usage is below 20%
        if cpu_percent < 10 and memory_percent < 20:
            deploy_application()

        time.sleep(3)  # Adjust the interval as needed

# Main function
if __name__ == "__main__":
    # Start the monitoring process
    monitor_system()
