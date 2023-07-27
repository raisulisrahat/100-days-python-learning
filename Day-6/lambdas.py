# Here i am showing lambdas in python

# Lambdas
x = lambda a:a*10
print(x(5))

# Lambda Functions
def myfunc(n):
  return lambda a:a*n
mydoubler = myfunc(2)

print(mydoubler(10))