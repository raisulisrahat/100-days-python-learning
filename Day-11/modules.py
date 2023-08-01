# Here I am using myModules

# Import my create Modules
import myModules
a = myModules.Bio["Name"]
print("I am "+a)

# From My create Modules
from myModules import Bio
print("I am "+Bio["Age"]+" years old")