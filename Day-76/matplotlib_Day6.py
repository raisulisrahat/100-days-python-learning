# Here I am showing Project Matplotlib Day 6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(self):
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            print(f"File '{self.data_file}' not found.")
            return None

    def analyze_data(self, data):
        if data is None:
            return

        # Calculate basic statistics using NumPy
        mean_value = np.mean(data['Value'])
        median_value = np.median(data['Value'])
        std_deviation = np.std(data['Value'])

        return mean_value, median_value, std_deviation

    def plot_data(self, data):
        plt.figure(figsize=(8, 6))  # Set figure size

        plt.hist(data['Value'], bins=20, color='skyblue', edgecolor='black')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.grid(True)
        plt.show()

def main():
    print("Welcome to the Data Analyzer and Plotter!")

    data_file = "data.csv"  # Replace with your CSV file path
    data_analyzer = DataAnalyzer(data_file)

    data = data_analyzer.load_data()
    if data is not None:
        mean, median, std_dev = data_analyzer.analyze_data(data)
        print("Data Analysis Results:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Standard Deviation: {std_dev}")
        
        data_analyzer.plot_data(data)

if __name__ == "__main__":
    main()
