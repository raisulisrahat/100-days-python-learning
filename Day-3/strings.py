# Here i am showing python string:

# string example:
print("Hello World!")   # "Hello World!" is a string

# Assing with veriable with strings:
a = "Hello World!"
print(a)

# Multi string with a variable:
a = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
molestiae quas vel sint commodi repudiandae consequuntur."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[7])

# Case string with lower and upper
a = "Hello World!"
print(a.lower())    # Lower case
print(a.upper())    # Upper Case

# Remove Whitespace
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))

# f string
Name = "Rahat"
Age = "24"
print(f"I am {Name}. I am {Age} years old.")