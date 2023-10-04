# Here I am showing Matplotlib Day 5

import numpy as np
import matplotlib.pyplot as plt

class DataPlotter:
    def generate_data(self):
        x = np.linspace(0, 10, 100)  # Generate 100 data points from 0 to 10
        y1 = np.sin(x)  # Sine wave data
        y2 = np.cos(x)  # Cosine wave data
        return x, y1, y2

    def plot_data(self, x, y1, y2, plot_type):
        plt.figure(figsize=(8, 6))  # Set figure size

        if plot_type == 'line':
            plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='-', linewidth=2)
            plt.plot(x, y2, label='Cosine Wave', color='red', linestyle='--', linewidth=2)
        elif plot_type == 'scatter':
            plt.scatter(x, y1, label='Sine Wave', color='green', marker='o', s=20)
            plt.scatter(x, y2, label='Cosine Wave', color='orange', marker='x', s=20)
        else:
            print("Invalid plot type. Please choose 'line' or 'scatter'.")
            return

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(f'{plot_type.capitalize()} Plot of Sine and Cosine Waves')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    print("Welcome to the Data Plotter!")

    data_plotter = DataPlotter()

    while True:
        print("\nMenu:")
        print("1. Line Plot")
        print("2. Scatter Plot")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            x, y1, y2 = data_plotter.generate_data()
            data_plotter.plot_data(x, y1, y2, 'line')
        elif choice == '2':
            x, y1, y2 = data_plotter.generate_data()
            data_plotter.plot_data(x, y1, y2, 'scatter')
        elif choice == '3':
            print("Exiting the Data Plotter.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
