# Here I am showing Built-In Random module in Python 

import random

myList = ["Apple", "Samsung", "Dell", "HP", "Asus"]

print(random.choice(myList))

print(random.sample(myList, k=2))

a = 15
b = 17
print(random.gauss(a, b))

print("The contents of the random library are:")
print(dir(random))