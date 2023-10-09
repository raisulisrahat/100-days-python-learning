# Here I am showing Project Matplotlib Day 10

import os
import matplotlib.pyplot as plt

class FilePlotter:
    def __init__(self, data_file):
        self.data_file = data_file

    def check_file_exists(self):
        try:
            if os.path.exists(self.data_file):
                return True
            else:
                print(f"File '{self.data_file}' does not exist.")
                return False
        except Exception as e:
            print(f"Error checking file existence: {e}")
            return False

    def read_data(self):
        try:
            with open(self.data_file, 'r') as file:
                data = file.readlines()
            return data
        except FileNotFoundError:
            print(f"File '{self.data_file}' not found.")
            return None
        except Exception as e:
            print(f"Error reading data from file: {e}")
            return None

    def plot_data(self, data):
        if data is None:
            return

        try:
            x = []
            y = []
            
            for line in data:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    x.append(parts[0])
                    y.append(int(parts[1]))
            
            plt.figure(figsize=(8, 6))  # Set figure size
            plt.plot(x, y, marker='o', linestyle='-', color='blue')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('File Data Plot')
            plt.grid(True)
            plt.show()
        except ValueError:
            print("Error parsing data. Ensure data format is correct.")

def main():
    print("Welcome to the File Data Plotter!")

    data_file = "data.txt"  # Replace with your file path

    file_plotter = FilePlotter(data_file)

    if file_plotter.check_file_exists():
        data = file_plotter.read_data()
        file_plotter.plot_data(data)

if __name__ == "__main__":
    main()
