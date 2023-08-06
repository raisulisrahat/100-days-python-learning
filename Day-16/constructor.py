# Here I am showing constructor in python

# Constructor
class Employee:  
    def __init__(self, name, id, post):  
        self.id = id  
        self.name = name
        self.post = post
  
    def display(self):  
        print("ID: %d \nName: %s \nPost: %s" % (self.id, self.name, self.post))  
  
  
emp1 = Employee("Asif", 101, "Web Developer")  
emp2 = Employee("Sima", 102, "Android Developer")
emp3 = Employee("Sakib", 103, "Web Developer")
emp4 = Employee("Opi", 104, "Blockchain Developer")
  

emp1.display() 
emp2.display()  
emp3.display()  
emp4.display()

# Parameterized Constructor
class Emp:  
    # Constructor - parameterized  
    def __init__(self, name):  
        print("This is parametrized constructor")  
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
Employee = Emp("Sakib")  
Employee.show()    

# Non-parameterized Constructor
class Emp:                  # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
Employee = Emp()  
Employee.show("Sakib")

# Built-in Constructor
class Employee:    
    def __init__(self,name,id,post):    
        self.name = name;    
        self.id = id;    
        self.post = post    
    def display_details(self):    
        print("Name:%s, ID:%d, Post:%s"%(self.name,self.id))    

emp1 = Employee("Asif", 101, "Web Developer")  
emp2 = Employee("Sima", 102, "Android Developer")
emp3 = Employee("Sakib", 103, "Web Developer")
emp4 = Employee("Opi", 104, "Blockchain Developer")

print(emp1.__doc__)    
print(emp1.__dict__)    
print(emp1.__module__) 
print(emp2.__doc__)    
print(emp2.__dict__)    
print(emp2.__module__) 
print(emp3.__doc__)    
print(emp3.__dict__)    
print(emp3.__module__) 
print(emp4.__doc__)    
print(emp4.__dict__)    
print(emp4.__module__)