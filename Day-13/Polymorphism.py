# Here I am showing Polymorphism in python

# Function Polymorphism
# String
x = "Hi, I am Rahat."
print(len(x))

# Tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Dictionary
Bio = {
    "Name": "Rahat",
    "Age" : 24,
    "Address" : "Dhaka",
    "Blood": "O+",
    "Nationality" : "Bangladeshi"
}
print(len(Bio))

# Class Polymorphism
class Processor:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Processor is perfect for you")

class Motherboard:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Motherboard is perfect for you")

class RAM:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("RAM is perfect for you")

cpu1 = Processor("Core i7", "13700K")       
mb1 = Motherboard("ASUS", "B760-PLUS") 
ram1 = RAM("G.Skill", "Z NEO 32GB")   

for x in (cpu1, mb1, ram1):
    x.move()

# Inheritance Class Polymorphism
class telephone:            # Parent Class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  

    def move(self):
        print("You can make a call")
        print("You can send a message")

class phone(telephone):     # Child Class
    def move(self):
        print("You can take a picture")
        print("You can browse any website")

telephone1 = telephone("Panasonic", "KX-TGF350")
phone1 = phone("Nokia", "C1")

for x in (telephone1, phone1):
    print(x.brand)
    print(x.model)
    x.move()

    