# Here i am showing Class/Objects in python

# Creating a Class
class newClass:
  x = 3
print(newClass)

# Creating a Object
class newClass:
  x = 7

p1 = newClass()
print(p1.x)

# The __init__() Function
class bio:
  def __init__(self, name, age):
    self.name = name
    self.age = age

b1 = bio("Rahat", 24)
print(b1.name)
print(b1.age)

# The __str__() Function
class bio:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

b1 = bio("Rahat", 24)
print(b1)

# Object Methods
class bio:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
       print("Hi I am " + self.name)

b1 = bio("Rahat", 24)
b1.myfunc()

# Customs self Parameter
class bio:
    def __init__(abc, name, age):
        abc.name = name
        abc.age = age
    def myfunc(abc):
       print("Hi I am " + abc.name + ". I am " + str(abc.age) +" years old.")

b1 = bio("Rahat", 25)
b1.myfunc()

