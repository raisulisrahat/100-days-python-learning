# Here I am using Built-In Modules

# Using Built-In Modules in platform
import platform

nodeName = platform.node()
systemName = platform.system()
print("Your node name is "+nodeName, "Your system name is "+systemName)

# Using dir() function 
x = dir(platform)
print(x)