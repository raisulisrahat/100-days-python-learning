# Here I am showing Matplotlib Day 4

import numpy as np  
import matplotlib.pyplot as plt  
  
  
ax = plt.axes()  

x = np.linspace(0, 10, 1000)  
ax.plot(x, np.sin(x))  


from matplotlib import style  
  
style.use('ggplot')  
  
x = [5,8,10]  
y = [12,16,6]  
  
x2 = [6,9,11]  
y2 = [7,15,7]  
  
  
plt.bar(x, y, color = 'y', align='center')  
plt.bar(x2, y2, color='c', align='center')  
  
plt.title('Information')  
  
plt.ylabel('Y axis')  
plt.xlabel('X axis')  