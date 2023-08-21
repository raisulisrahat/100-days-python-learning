# Here i am showing the Day 21 practice project

# Task note
import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline

def create_task():
    description = input("Enter task description: ")
    deadline_str = input("Enter task deadline (YYYY-MM-DD): ")
    year, month, day = map(int, deadline_str.split("-"))
    deadline = datetime.date(year, month, day)
    return Task(description, deadline)

def main():
    print("Welcome to the Task Manager!")

    tasks = []

    while True:
        print("\nMenu:")
        print("1. Create a new task")
        print("2. List all tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = create_task()
            tasks.append(task)
            print("Task created successfully!")
        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. Description: {task.description}, Deadline: {task.deadline}")
        elif choice == '3':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
