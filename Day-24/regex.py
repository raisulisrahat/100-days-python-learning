# Here I am showing Built-In Regular Expression or RegEx in python
# https://www.w3schools.com/python/python_regex.asp


import re

x = "This is a good idea"

# Search Functions
y = re.search("^This.*idea$", x)
if y:
  print("It's match!")
else:
  print("No match")

# Findall Functions
z = re.findall("Grate", x)
if z:
  print("It's match!")
else:
  print("No match")

# Split Functions
a = re.split("\s", x)
print(a)

# Sub Functions
b = re.sub("\s", "5", x)
print(b)

