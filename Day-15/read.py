# Here I am showing File Handling(read) Method python

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist

# file read
file = open("readfile.txt", "r")
read = file.read()
print(read)
file.close()

# File len
size = len(read)
print(size)

# Readline
file = open("readfile.txt", "r")
print(file.readline())
file.close

# Loop
file = open("readfile.txt", "r")
for x in file:
  print(x)