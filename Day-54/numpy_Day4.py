# Here I am showing numpy modules Day 3

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for a in arr:
    print(a)

# 
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types
for y in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(y)

# Enumerated Iteration Using ndenumerate()
for nuId, z in np.ndenumerate(arr):
    print(nuId, z)

