# Here I will show you How to use Input in python. Input are related with print

input("What is your name?") # Only ask it input.
 
print(input("What is your name?")) # If I write the input in print parameter. you will get the output

# Input lenth
print(len(input("Your Name:\n"))) # You can identify the input lenth


# input in data types:

"""
Data types: string, integer, float, bool, list 
"""
print(input("What is Your name?\n:"))   # if wirte a string No need speacify the string, integer, float and bool
print(int(input("How Old are You?\n:")))    # If you write a integer wirte int then call input. You can write integer input only You can't write string float, bool get the error
print(float(input("What is your CGPA?\n:")))    # If you write a float wirte int then call input. You can write Float input only, You can't write string integer, bool get the error


# print the input with text data
print("Ans: I am " + input("What is Your name?\n:"))
print("Ans: I am " +str(int(input("How Old are You?\n:")))+ " Old")
print("My CGPA grade is " +str(float(input("What is your CGPA?\n:"))))