# Here I showing Logging Project in python 

import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_info(self, message):
        logging.info(message)

    def log_warning(self, message):
        logging.warning(message)

    def log_error(self, message):
        logging.error(message)

def main():
    print("Welcome to the Logging Project!")

    log_file = "app.log"
    logger = Logger(log_file)

    while True:
        print("\nMenu:")
        print("1. Log an INFO message")
        print("2. Log a WARNING message")
        print("3. Log an ERROR message")
        print("4. View log file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter an INFO message: ")
            logger.log_info(message)
            print("INFO message logged.")
        elif choice == '2':
            message = input("Enter a WARNING message: ")
            logger.log_warning(message)
            print("WARNING message logged.")
        elif choice == '3':
            message = input("Enter an ERROR message: ")
            logger.log_error(message)
            print("ERROR message logged.")
        elif choice == '4':
            try:
                with open(log_file, 'r') as file:
                    print("Log File Content:")
                    print(file.read())
            except FileNotFoundError:
                print("Log file not found.")
        elif choice == '5':
            print("Exiting the Logging Project.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
