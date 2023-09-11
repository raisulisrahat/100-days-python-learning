# Here I am showing numpy modules Day 2

import numpy as np
#  creating a basic array methods

a = np.zeros(2)
print(a)

arr = np.array([1, 2, 3, 4, 5, 6, 6, 10, 11, 12, 7, 8, 9])
print(arr)

a = np.ones(11)
print(a)

a = np.empty(2)
print(a)

a = np.arange(4)
print(a)

a = np.arange(2, 9, 2)
print(a)

a = np.linspace(0, 10, num=5)
print(a)

a = np.sort(arr)
print(a)