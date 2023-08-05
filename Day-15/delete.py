# Here I am showing File Handling(delete) Method python
import os
file = os.remove("deletefile.txt")
print(file)

# file delete with conditions
if os.path.exists("deletefile.txt"):
    file
else:
    print("File Not found")

