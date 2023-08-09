# Here I am showing Day 15 to Day 17 python practise

# 15 | File Handling(Read, Write and Delete file)
# 16 | Constructor and Encapsulation
# 17 | Exception Handling 
import csv

class Student:
    def __init__(self, roll, name, sub):
        self.roll = roll
        self.name = name
        self.sub = sub

    def display(self):
        print("Roll: %s" % self.roll)
        print("Name: %s" % self.name)
        print("Subject: %s" % self.sub)
        print()

    def student_sheet():
        try:
            with open("students_sheet.csv", "r") as file_sheet:
                read_sheet = csv.reader(file_sheet)
                for row in read_sheet:
                    roll, name, sub = row
                    student = Student(roll, name, sub)
                    student.display()
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Something went wrong:", e)

Student.student_sheet()