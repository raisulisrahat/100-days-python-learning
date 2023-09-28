# Here I am showing Pandas and Numpy Practising Project Day 2

import numpy as np
import pandas as pd

class DataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_data(self):
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            print(f"File '{self.data_file}' not found.")
            return None

    def analyze_data(self, data):
        if data is None:
            return

        while True:
            print("\nMenu:")
            print("1. Calculate mean")
            print("2. Calculate median")
            print("3. Calculate minimum value")
            print("4. Calculate maximum value")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                mean = np.mean(data['Value'])
                print(f"Mean: {mean}")
            elif choice == '2':
                median = np.median(data['Value'])
                print(f"Median: {median}")
            elif choice == '3':
                min_value = np.min(data['Value'])
                print(f"Minimum Value: {min_value}")
            elif choice == '4':
                max_value = np.max(data['Value'])
                print(f"Maximum Value: {max_value}")
            elif choice == '5':
                print("Exiting the Data Analyzer.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

def main():
    print("Welcome to the Data Processor!")

    data_file = "data.csv"  # Replace with your CSV file path
    data_processor = DataProcessor(data_file)

    data = data_processor.read_data()
    data_processor.analyze_data(data)

if __name__ == "__main__":
    main()
