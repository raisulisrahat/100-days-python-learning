
# Here i am showing Sys module in python
import sys

for line in sys.stdin:
    line = line.rstrip()  # Remove newline character from the input line
    if 'q' == line:
        break
    sys.stdout.write(f'Input: {line}\n')  # Fix the newline character escape sequence
    sys.stdout.flush()  # Correct the function call

else:
    sys.stderr.write("Error\n")  # Correct the function call

print("Exit")