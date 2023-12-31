# Here I write how to use print in python. Most of the common sentence are "Hello World!". So every programming language string is in text data and `Hello World` is a string 
print("Hello World!") # print a string with python 

# Here is the demo of using single and double quotation marks
print('Hello World')    # Using single qoutation
print("Hello World")    # Using Double qoutation
print("print('Hello World!')")
print('print("Hello World!")')

# I can print multiipule string in new line base. Here is the example
print("Hello World!\nHello World!\nHello World!\nHello World!") # adding muntipule new line 

# Here I am showing you a gap or non gap in string
print("Hello" "World!")    # No Gap in this sentance
print("Hello" +" "+ "World!")  # Gap in this sentance

# Error Types

# Here I am showing you SyntaxError. If miss any quotation, Showing this SyntaxError. Here is Demo: 
"""
print("Hello World!)"   # Output was: 'SyntaxError: '()' was never closed'
print("Hello World!) # Output was: 'SyntaxError: unterminated string literal'
print(Hello World!)  # Output was: 'SyntaxError: invalid syntax. Perhaps you forgot a comma or qutation?'
"""

# If I miss the print() and quotation geting SyntaxError.
# Hello World!  # Output was: 'SyntaxError: invalid syntax'

# Here I am showing you a SyntaxError with a variable. If i write a wrong variable name output will be SyntaxError: invalid syntax.
"""
My name = Rahat
print(My name)
"""