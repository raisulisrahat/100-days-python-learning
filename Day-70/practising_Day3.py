# Here I showing Numpay Random Pandas and String Day 3

import numpy as np
import pandas as pd
import random
import string

class DataGenerator:
    def __init__(self, data_file):
        self.data_file = data_file

    def generate_data(self, num_rows):
        random.seed(42)  # Seed for reproducibility

        # Generate random data
        data = {
            'ID': [i + 1 for i in range(num_rows)],
            'Name': [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(num_rows)],
            'Value1': [random.randint(1, 100) for _ in range(num_rows)],
            'Value2': [random.uniform(0, 1) for _ in range(num_rows)],
        }

        return pd.DataFrame(data)

    def save_to_csv(self, data):
        data.to_csv(self.data_file, index=False)
        print(f"Data saved to '{self.data_file}'")

    def analyze_data(self, data):
        if data is None:
            return

        # Calculate basic statistics using NumPy
        mean_value1 = np.mean(data['Value1'])
        mean_value2 = np.mean(data['Value2'])
        max_value1 = np.max(data['Value1'])
        min_value2 = np.min(data['Value2'])

        # Display the results
        print("Data Analysis Results:")
        print(f"Mean Value1: {mean_value1}")
        print(f"Mean Value2: {mean_value2}")
        print(f"Max Value1: {max_value1}")
        print(f"Min Value2: {min_value2}")

def main():
    print("Welcome to the Data Generator and Analyzer!")

    data_file = "data.csv"
    num_rows = 10  # Number of rows of data to generate

    data_generator = DataGenerator(data_file)

    # Generate random data and save it to a CSV file
    generated_data = data_generator.generate_data(num_rows)
    data_generator.save_to_csv(generated_data)

    # Analyze the generated data
    data_to_analyze = data_generator.generate_data(num_rows)  # You can load data from the CSV file for analysis
    data_generator.analyze_data(data_to_analyze)

if __name__ == "__main__":
    main()
