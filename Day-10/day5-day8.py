"""
| 5 | Loops 
| 6 | Function and Lambdas 
| 8 | Scope and Sorting
"""
Student_List = [{"Id": "01", "Name": "A", "Result": 4.06},
                {"Id": "02", "Name": "B", "Result": 4.46},
                {"Id": "03", "Name": "C", "Result": 5.0},
                {"Id": "04", "Name": "D", "Result": 3.0}]

def Add_Students(student_list, students_id, name, result):
    new_student = {"Id": students_id, "Name": name, "Result": result}
    student_list.append(new_student)
    

def Student_result():
    sort_list = sorted(Student_List, key=lambda x: x["Result"])
    for x in sort_list:
        result = float(x["Result"])

        if result > 4.50:
            print(f"{x['Name']} can get the job.")
        elif result > 4.0:
            print(f"{x['Name']} is in waiting list.")
        else:
            print(f"{x['Name']} can't get the job.")
    
Add_Students(Student_List, "05", "E", 3.80)
Add_Students(Student_List, "06", "F", 4.90)
Add_Students(Student_List, "07", "G", 4.20)

Student_result()


