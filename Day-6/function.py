# Here i am showing function in python

# create function 
def my_Newfunction():
    print("Hello World!")

# call function
my_Newfunction()

# Arguments
def my_function(fname):
    print(fname + " Islam")

my_function("Raisul")
my_function("Rahat")

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Raisul", "Islam")

# Arbitrary Arguments, *args
def my_function(*name):
  print("Your name is " + name[1])

my_function("Raisul", "Rahat", "Islam")

# Keyword Arguments
def my_function(fname, mname, lname):
    print("Your name is " + fname + " " + mname + " " + lname)

my_function("Raisul", mname="Islam", lname="Rahat")

# List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# pass Statement
def my_function():
   pass

