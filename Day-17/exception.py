# Here i am showing Exception Handling

# Exception handling with try, except, else, and finally
# Try: This block will test the excepted error to occur
# Except:  Here you can handle the error
# Else: If there is no exception then this block will be executed
# Finally: Finally block always gets executed either exception is generated or not


# Try Except Exception
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Oops! Try again...")

# Else Exception
def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
divide(3, 2)
divide(3, 0)

# Finally Exception
def divide(x, y):
    try:

        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        print('This is always executed')  

divide(3, 2)
divide(3, 0)

# Raising Exceptions
try:
    raise NameError(input("Enter a name: "))
except NameError:
    print('An exception flew by!')
    raise

