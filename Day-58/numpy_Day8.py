# Here I am showing numpy modules Day 8

from numpy import random

x = random.uniform(size=(2, 3))
print(x)                        # Uniform Distribution

y = random.poisson(lam=2, size=10)
print(y)                        # Poisson Distribution

z = random.binomial(n=10, p=1, size=10)
print(z)                        # Binomial Distribution

a = random.pareto(a=2, size=(2, 3))
print(a)                        # Pareto Distribution

b = random.zipf(a=2, size=(2, 3))
print(b)                        # Zipf Distribution