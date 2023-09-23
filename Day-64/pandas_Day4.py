# Here I am showing Pandas Day 4

import pandas as pd
import numpy as np

data = np.array([1,2,3,4,5,6,7])
x = pd.Series(data)
print(x)

data2 = {'Item 1': pd.DataFrame(np.random.rand(4,3)), 
         'Item 2': pd.DataFrame(np.random.rand(4,2))}
y = pd.concat(data2)
print(y)