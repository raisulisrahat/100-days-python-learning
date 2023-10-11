# Here I am showing Problem Solve Day 1

# Log Analysis:
# Write a Python script that parses log files and extracts specific error messages, then sends alerts when critical errors are detected.

import re
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up logging to read from a log file
log_file_path = "your_log_file.log"
logging.basicConfig(filename=log_file_path, level=logging.ERROR)

# Define the regular expression pattern to match critical errors
error_pattern = r"\[ERROR\] (.*)"

# Function to extract and send alerts for critical errors
def analyze_log_and_alert():
    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                match = re.search(error_pattern, line)
                if match:
                    error_message = match.group(1)
                    send_alert(error_message)
    except Exception as e:
        print(f"Error reading log file: {str(e)}")

# Function to send alerts via email
def send_alert(error_message):
    sender_email = "risulislam089@gmail.com"
    receiver_email = "bulletsblack4@gmail.com"
    password = "---"

    subject = "Critical Error Alert"
    body = f"Critical error detected: {error_message}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Alert sent successfully.")
    except Exception as e:
        print(f"Error sending alert: {str(e)}")

# Run the log analysis and alerting
analyze_log_and_alert()
