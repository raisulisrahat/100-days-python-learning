# Here I am showing Email Sender Project on python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, message):
        try:
            # Create an SMTP connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Create and send the email
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            server.sendmail(self.sender_email, recipient_email, msg.as_string())
            server.quit()

            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    print("Welcome to the Email Sender!")

    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    sender_email = "your_email@example.com"  # Replace with your sender email
    sender_password = "your_password"  # Replace with your sender password

    email_sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)

    while True:
        print("\nMenu:")
        print("1. Send an email")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            recipient_email = input("Enter recipient's email: ")
            subject = input("Enter email subject: ")
            message = input("Enter email message: ")

            email_sender.send_email(recipient_email, subject, message)
        elif choice == '2':
            print("Exiting the Email Sender.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
