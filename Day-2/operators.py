# Here I am showing python operators.

"""
Arithmetic operators: +, -, *, /, %, **, //
Assignment operators: =, +=, -=, *=, /=, %=, **=, //=, |=, &=, ^=, <<=, >>=
Comparison operators: ==, !=, >, <, >=, <=
Logical operators: and, or, not
Identity operators: is, is not
Membership operators: in, not in
Bitwise operators: &, |, ~, <<, >>, ^
"""
# Arithmetic operators: 

x = 6
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment operators:

x = 6
print(x)

x = 6
x += 5
print(x)

x = 6
x -= 5
print(x)

x = 6
x *= 5
print(x)

x = 6
x /= 5
print(x)

x = 6
x %= 5
print(x)

x = 6
x **= 5
print(x)

x = 6
x //= 5
print(x)

x = 6
x |= 5
print(x)

x = 6
x &= 5
print(x)

x = 6
x ^= 5
print(x)

x = 6
x <<= 5
print(x)

x = 6
x >>= 5
print(x)

# Comparison operators:
x = 5
y = 4

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical operators:
x = 5
print(x < 5 and  x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and  x < 10))

# Membership operators:
x = ["A", "B"]
y = ["A", "B"]
print(x is y)
print(x is not y)

# Bitwise operators:
x = 6
y = 4

print(x & y) 
print(x | y) 
print(~y) 
print(x >> y) 
print(x << y) 
print(x ^ y) 