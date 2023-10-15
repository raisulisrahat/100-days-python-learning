# Here I am showing Problem Solve Day 6

# Memory Management and Optimization:
# Build a Python script that analyzes memory usage and provides recommendations for optimizing memory consumption. You can use the psutil module to collect memory information and subprocess to execute memory-intensive tasks.    

import argparse
import shutil
import os

def copy_files(args):
    for source in args.source:
        destination = args.destination
        if args.destination_dir:
            destination = os.path.join(destination, os.path.basename(source))
        shutil.copy(source, destination)
        print(f"File copied: {source} to {destination}")

def move_files(args):
    for source in args.source:
        destination = args.destination
        if args.destination_dir:
            destination = os.path.join(destination, os.path.basename(source))
        shutil.move(source, destination)
        print(f"File moved: {source} to {destination}")

def delete_files(args):
    for source in args.source:
        os.remove(source)
        print(f"File deleted: {source}")

def main():
    parser = argparse.ArgumentParser(description="Custom File Manipulation CLI")

    subparsers = parser.add_subparsers(title="Commands", dest="command")

    copy_parser = subparsers.add_parser("copy", help="Copy files")
    copy_parser.add_argument("source", nargs="+", help="Source files to copy")
    copy_parser.add_argument("destination", help="Destination directory")
    copy_parser.add_argument("--destination-dir", action="store_true", help="Treat destination as a directory")

    move_parser = subparsers.add_parser("move", help="Move files")
    move_parser.add_argument("source", nargs="+", help="Source files to move")
    move_parser.add_argument("destination", help="Destination directory")
    move_parser.add_argument("--destination-dir", action="store_true", help="Treat destination as a directory")

    delete_parser = subparsers.add_parser("delete", help="Delete files")
    delete_parser.add_argument("source", nargs="+", help="Source files to delete")

    args = parser.parse_args()

    if args.command == "copy":
        copy_files(args)
    elif args.command == "move":
        move_files(args)
    elif args.command == "delete":
        delete_files(args)

if __name__ == "__main__":
    main()

