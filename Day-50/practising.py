# Here I am showing CLI calculator

import argparse

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("x", type=float, help="First operand")
    parser.add_argument("y", type=float, help="Second operand")

    args = parser.parse_args()

    calculator = Calculator()

    if args.operation == "add":
        result = calculator.add(args.x, args.y)
    elif args.operation == "subtract":
        result = calculator.subtract(args.x, args.y)
    elif args.operation == "multiply":
        result = calculator.multiply(args.x, args.y)
    elif args.operation == "divide":
        try:
            result = calculator.divide(args.x, args.y)
        except ValueError as e:
            print(f"Error: {str(e)}")
            return

    print(f"Result of {args.operation}: {result}")

if __name__ == "__main__":
    main()