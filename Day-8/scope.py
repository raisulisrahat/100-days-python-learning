# Here I am showing Scope in python

# Local Scope
def myfunc():
    s = "apple"
    print(s)

myfunc()

# Function Inside Function
def myfunc():
    n = 15
    def myinnerfunc():
        print(n)
    myinnerfunc()

myfunc()

# Global Scope

a = 105
def newfunc():
    print(a)
newfunc()
print(a)

# Naming Variables
i = 18      # Global
def Ifunc():
    i = 27  # Local
    print(i)

Ifunc()
print(i)

# Global Keyword
x = 83
def myfunc():
    global x    #The global keyword makes the variable global.
    x = 75

myfunc()
print(x)