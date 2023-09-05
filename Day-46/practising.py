# Here I showing Day 41 Practising moduels in Python

# Task Manager

import yaml

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

def taskLoad():
    try:
        with open('Task.yaml', 'r') as file:
            return yaml.safe_load(file) or []
    except FileNotFoundError:
        return []

def taskSave(tasks):
    with open('Task.yaml', 'w') as file:
        yaml.dump(tasks, file)

def main():
    print('Welcome to the Task Manager!')
    
    tasks = taskLoad()

    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter your task description: ")
            newTask = Task(description)
            tasks.append(newTask)
            taskSave(tasks)
            print("New Task Added.")
        elif choice == '2':
            if not tasks:
                print("No Task Found.")
            else:
                print("Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    status = 'Completed' if task.completed else 'Not Completed'
                    print(f"{idx}, Description: {task.description}, Status: {status}")
        elif choice == '3':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option")

if __name__ == "__main__":
    main()
