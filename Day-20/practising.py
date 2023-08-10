# Here I am showing Day 1 to Day 17 in python

class Employees:
    def __init__(self, id, name, title):
        self.id = id
        self.name = name
        self.title = title

    def display(self):
        print("ID: {}".format(self.id))
        print("Name: {}".format(self.name))
        print("Job Title: {}".format(self.title))

    def readEmployee(self):
        try:
            with open("employee_list.txt", "r") as file_list:
                read_list = file_list.read()
                print(read_list)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Something went wrong:", e)

    def writeEmployee(self):
        try:
            with open("employee_list.txt", "a") as file_list:
                employee_info = f"{self.id},{self.name},{self.title}\n"
                file_list.write(employee_info)
                print("Employee added successfully.")
        except Exception as e:
            print("Something went wrong:", e)

    def removeEmployee(self, target_id):
        try:
            with open("employee_list.txt", "r") as file_list:
                lines = file_list.readlines()

            with open("employee_list.txt", "w") as file_list:
                for line in lines:
                    emp_id = int(line.split(',')[0])
                    if emp_id != target_id:
                        file_list.write(line)
                print("Employee removed successfully.")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Something went wrong:", e)

while True:
    print("\nEmployee Management Menu:")
    print("1. Read Employee List")
    print("2. Add Employee")
    print("3. Remove Employee")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee = Employees(0, "", "")
        print("\nEmployee List:")
        employee.readEmployee()
    elif choice == "2":
        new_id = int(input("Enter new employee ID: "))
        new_name = input("Enter new employee name: ")
        new_title = input("Enter new employee job title: ")
        new_employee = Employees(new_id, new_name, new_title)
        new_employee.writeEmployee()
    elif choice == "3":
        target_id = int(input("Enter ID of employee to remove: "))
        employee = Employees(0, "", "")
        employee.removeEmployee(target_id)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
