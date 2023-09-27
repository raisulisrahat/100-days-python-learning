# Here I am showing Pandas & Numpy 

import numpy as np
import pandas as pd

class DataAnalyzer:
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
        
        # Calculate basic statistics using NumPy
        mean = np.mean(data['Value'])
        median = np.median(data['Value'])
        min_value = np.min(data['Value'])
        max_value = np.max(data['Value'])

        # Display the results
        print("Data Analysis Results:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Minimum Value: {min_value}")
        print(f"Maximum Value: {max_value}")

def main():
    print("Welcome to the Data Analyzer!")

    data_file = "data.csv"  # Replace with your CSV file path
    data_analyzer = DataAnalyzer(data_file)

    data = data_analyzer.read_data()
    data_analyzer.analyze_data(data)

if __name__ == "__main__":
    main()
