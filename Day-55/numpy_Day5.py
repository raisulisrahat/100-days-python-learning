# Here I am showing numpy modules Day 5

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# Splitting NumPy Arrays
splarr = np.array_split(arr, 2, axis=2)
print(splarr)

# Split Into Arrays
print(splarr[0])
print(splarr[1])

# Searching Arrays
x = np.where(arr == 4)
print(x)

y = np.where(arr%2 == 1)
print(y)

# Search Sorted
arr = np.array([1,2,3])
z = np.searchsorted(arr, 3)

print(z)