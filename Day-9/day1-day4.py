"""
| 1 | Print, Input and variable
| 2 | Data types and Operators 
| 3 | String and Condition 
| 4 | Lists, Sets and Tuples
"""

myList = ["Hello", 15.5, 47, "Rahat", 4.6, True, False, 24, "Age", 41]

x = set(myList)
print(x)

myTuple = tuple(x)
print(myTuple)

string_list = [] 
for item in myTuple:
    if isinstance(myTuple, str):
        string_list.append(item)

print(string_list)