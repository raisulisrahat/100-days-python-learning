# Here I am showing Project Matplotlib Day 9

import random
import matplotlib.pyplot as plt

class RandomPlotter:
    def __init__(self, num_points):
        self.num_points = num_points

    def generate_data(self):
        try:
            random.seed(42)  # Seed for reproducibility

            x = [i for i in range(self.num_points)]
            y = [random.randint(0, 100) for _ in range(self.num_points)]

            return x, y
        except Exception as e:
            print(f"Error generating data: {e}")
            return None

    def plot_data(self, x, y):
        if x is None or y is None:
            return

        try:
            plt.figure(figsize=(8, 6))  # Set figure size
            plt.plot(x, y, marker='o', linestyle='-', color='blue')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('Random Data Plot')
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"Error plotting data: {e}")

def main():
    print("Welcome to the Random Data Plotter!")

    num_points = 50  # Number of data points to generate

    random_plotter = RandomPlotter(num_points)

    x, y = random_plotter.generate_data()
    random_plotter.plot_data(x, y)

if __name__ == "__main__":
    main()

