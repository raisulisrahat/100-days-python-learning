# Here I am showing numpy modules Day 6

import numpy as np
from numpy import random

rng = np.random.default_rng(1)  # Providing a seed of 1
random_number = rng.random()
print(random_number)

# Generating Permutation Arrays
arr = np.array([1,4,6,7])
print(random.permutation(arr))