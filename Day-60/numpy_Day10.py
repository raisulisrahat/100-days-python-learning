# Here I am showing Numpy Day 10

import numpy as np

num = [-3.2562, 3.571]

# Primarily five ways of rounding off decimals in NumPy
arrtrc = np.trunc(num)
print(arrtrc)

arrfix = np.fix(num)
print(arrfix)

arrrou = np.round(num)
print(arrrou)

arrfloor = np.floor(num)
print(arrfloor)

arrceil = np.ceil(num)
print(arrceil)

