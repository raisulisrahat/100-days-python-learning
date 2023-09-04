# Here I am Showing Argparse in python

import argparse

if __name__ == "__main__":
    # Create an ArgumentParser with a program description
    parser = argparse.ArgumentParser(description="A program that does something with multiple arguments.")

    # Add the arguments
    parser.add_argument("arg1", help="Description of arg1")
    parser.add_argument("arg2", help="Description of arg2")
    # Add more arguments as needed...

    # Parse the command line arguments
    args = parser.parse_args()

    # Now you can access and use the arguments as needed
    print("arg1:", args.arg1)
    print("arg2:", args.arg2)

