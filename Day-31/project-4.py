# Here i am showing the Day 24 practice project

# Email Validator
import re

class EmailValidator:
    def __init__(self):
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def is_valid_email(self, email):
        return self.email_pattern.match(email)

def main():
    print("Welcome to the Email Validator!")

    email_validator = EmailValidator()

    while True:
        email = input("Enter an email address: ")

        if email_validator.is_valid_email(email):
            print("Valid email address.")
        else:
            print("Invalid email address.")

        choice = input("Do you want to validate another email? (y/n): ")

        if choice.lower() != 'y':
            print("Exiting the Email Validator.")
            break

if __name__ == "__main__":
    main()

