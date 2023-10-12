# Here I am showing Problem Solve Day 3


# Deployment Script:
# Create a Python script to automate the deployment of a web application, including tasks like pulling code from a version control system and restarting the application server.

import os
import subprocess

# Configuration variables
repository_url = "https://github.com/raisulisrahat/Assignment-2.git"
web_app_directory = "C:/Program Files (x86)/nginx/html"
app_service_name = "nginx"

# Function to update the web application
def update_web_app():
    try:
        # Change to the web application directory
        os.chdir(web_app_directory)

        # Pull the latest code from the Git repository
        subprocess.call(["git", "pull"])

        # Restart the application service (e.g., using systemd)
        subprocess.call(["systemctl", "restart", app_service_name])

        print("Deployment successful.")
    except Exception as e:
        print(f"Deployment error: {str(e)}")

if __name__ == "__main__":
    update_web_app()