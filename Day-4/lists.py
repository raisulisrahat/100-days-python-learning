# Here i am showing python lists
fruitsList = ["apple", "banana", "mango", "malon", "orange", "kiwi", "cherry"]
# itemCall     0        1         2        3        4         5       6
print(fruitsList)   # printing fruitslist

# List length
print(len(fruitsList))  # Counting item list length 

# Access list item
print(fruitsList[1])    # Item list call only 1

# Negative item
print(fruitsList[-1])   # Negative indexing means starting from the end of the list.

# Range of Indexes
print(fruitsList[4:]) # collect list item 0 to 4
print(fruitsList[:5])   # collect list item 0 to 4 and item 5 not included
print(fruitsList[3:5])  # collect list item 3 to 4 and item 5 not included
print(fruitsList[-4:-1])    # items from index -4 (included) to index -1 (excluded)

# Add iteam
fruitsList.append("Stoberry")   # Add new fruits
print(fruitsList)

