# Here I am showing Sorts in python

# Sorting Basics

Num = [1, 5, 7, 3, 11, 2, 6, 18]
print(sorted(Num))

ListNum = {1:'G', 5:'H', 7:'D', 3:'E', 11:'F', 2:'B', 6:'C', 18:'A'}
print(sorted(ListNum))

# Key Functions
x = "Hi I am Rahat."
print(sorted(x.split(), key=str.lower))

# reverse sorts
Num = [1, 5, 7, 3, 11, 2, 6, 18]
print(sorted(Num, reverse=True))