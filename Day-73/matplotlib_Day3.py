# Here I am showing Matplotlib Day 3

import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,30,60,40])
y = np.array([11,5,30,48,20])

plt.subplot(1,2,1)
plt.plot(x,y)

# Plot 2 Women
a = np.array([10,11,15,23,50])
b = np.array([15,22,18,41,65])
plt.subplot(1,2,2)
plt.plot(a,b)
plt.grid()
plt.show()

# Matplotlib Pie Charts9
plt.title("Man Ages")

x = np.array([10,20,30,60,40])

plt.xlabel('Man')
plt.pie(x)
plt.show()