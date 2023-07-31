"""
| 1 | Print, Input and variable
| 2 | Data types and Operators 
| 3 | String and Condition 
| 4 | Lists, Sets and Tuples
"""

myList = ["Hello", 15.5, 47, "Rahat", 4.6, True, False, 24, "Age", 41]

# convert with set
x = set(myList)
print(x)

# convert with tuple
myTuple = tuple(x)
print(myTuple)

# Find only string
string_list = []
for item in myTuple:
    if isinstance(item, str):
        string_list.append(item)

print(string_list)

# Find only Integer
integer_list = []
for item in myTuple:
    if isinstance(item, int):
        integer_list.append(item)

print(integer_list)

# Find only bool
bool_list = []
for item in myTuple:
    if isinstance(item, bool):
        bool_list.append(item)

print(bool_list)

# Find only float
float_list = []
for item in myTuple:
    if isinstance(item, float):
        float_list.append(item)

print(float_list)