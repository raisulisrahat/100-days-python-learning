# Here I am showing numpy modules Day 3

import numpy as np

a = np.arange(6).reshape(3,2)
print(a)

# Array View
b = a.view()
print(b)

# Array Copy
c = b.copy()    
print(c)


# Shape of an Array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)              
print(arr.shape)

x = a,b,c.shape
print(x)