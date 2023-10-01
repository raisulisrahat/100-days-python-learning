# Here I am showing Matplotlib Day 2

# Matplotlib Pyplot Labels and Title
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("BP List")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# Matplotlib Pyplot Labels, Title and Marker
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 20, 70, 280, 90, 300, 310, 320, 330])

plt.plot(x, y, marker = 'X')
plt.title("BP List")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()
plt.show()