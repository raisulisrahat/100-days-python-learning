# Here I am showing numpy modules Day 7


from numpy import random

arr = random.choice([5,6,7,9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(arr)

arr = random.binomial(n=10, p=0.6, size=100)
print(arr)

# Normal Distribution
x = random.normal(size=(3,5))
print(x)