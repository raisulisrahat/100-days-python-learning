# Here i am showing the loops in python

# while loop
i = 1
while i < 12:
    print(i)
    i += 1

# while loop with conditions
a = 0
while a < 6:
    a += 1
    if a == 3:
        print(a, "is working")
    else:
        print(a, "not working")

# while with continue
b = 0
while b < 5:
    b += 1
    if b <= 2:
        continue
    print(b, "is working")

# while loop with break
c = 1
while c < 6:
    print(c, "is working.")
    if (c == 3):
        break
    c += 1

# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# for loop with brack
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# for loop with continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# for loop with conditions
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        print(x, "is working")
    else:
        print(x, "not working")

# for loop with range 
for x in range(6):
  print(x)

# for nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)