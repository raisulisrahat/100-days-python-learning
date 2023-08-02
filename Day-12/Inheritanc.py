# Here I am showing  Inheritance and Polymorphism in python

class telephone:        # Parent Class
    def call(self):
        print("You can make a call")
    def message(self):
        print("You can send a message")
class phone(telephone):     # Child Class
    def photo(self):
        print("You can take a picture")
    def web(self):
        print("You can browse any website")

# Add the __init__() and super() Function
class smartphone(phone):
    def __init__(self):
        super().__init__()

x = smartphone()
x.call()
x.message()
x.photo()
x.web()