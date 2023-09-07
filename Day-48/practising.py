# Here I am showing File Manager project in python

import os

class FileManager:
    def create_directory(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        else:
            print(f"Directory '{directory_name}' already exists.")

    def create_file(self, file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                print(f"File '{file_name}' created successfully.")
        else:
            print(f"File '{file_name}' already exists.")

    def list_files(self, directory):
        if os.path.exists(directory) and os.path.isdir(directory):
            files = os.listdir(directory)
            if files:
                print(f"Files in directory '{directory}':")
                for file in files:
                    print(file)
            else:
                print(f"No files found in directory '{directory}'.")
        else:
            print(f"Directory '{directory}' does not exist.")

def main():
    print("Welcome to the File Manager!")

    file_manager = FileManager()

    while True:
        print("\nMenu:")
        print("1. Create a directory")
        print("2. Create a file")
        print("3. List files in a directory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            directory_name = input("Enter directory name: ")
            file_manager.create_directory(directory_name)
        elif choice == '2':
            file_name = input("Enter file name: ")
            file_manager.create_file(file_name)
        elif choice == '3':
            directory = input("Enter directory to list files: ")
            file_manager.list_files(directory)
        elif choice == '4':
            print("Exiting the File Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
