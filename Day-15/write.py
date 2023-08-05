# Here I am showing File Handling(write) Method python

# File write
file = open("writefile.txt", "a")
file.write(input("Write sometext: "))
file.close()

file = open("writefile.txt", "r")
print(file.read())

# Create a New File
file = open("newfile.txt", "x")
print("newfile created")
file.write(input("Write sometext: "))
file.close()

file = open("newfile.txt", "r")
print(file.read())