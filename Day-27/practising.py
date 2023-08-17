# Here is am showing Practising Day 22 in python

# Math Built-In Modules
import math

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

def power(number1, number2):
    return int(math.pow(number1, number2))

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"
        "5. Power\n")

select = int(input("Select operations:"))
 
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
 
if select == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))
 
elif select == 2:
    print(num1, "-", num2, "=",
                    subtract(num1, num2))
 
elif select == 3:
    print(num1, "*", num2, "=",
                    multiply(num1, num2))
 
elif select == 4:
    print(num1, "/", num2, "=",
                    divide(num1, num2))
elif select == 5:
    print(num1, "^", num2, "=",
                    power(num1, num2))
else:
    print("Invalid input")