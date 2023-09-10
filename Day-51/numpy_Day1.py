# Here I am showing numpy modules Day 1

import numpy as np
print(np.__version__)

# Access 1-D 
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr[0])         # Access the first element

# Access 2-D 
arr = np.array([[1, 2, 3, 4, 5], [6,7,8,9,0]])

print(arr)
print(arr[1,1])          # Access the element in the second row and second column

# Access 3-D 
arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

print(arr)
print(arr[0,2,2])     # Access the single element in the 3-D array