# Dictionary
student_grades = { } 

# Add new student
def add_student(name, grade):
    student_grades[name] = grade
    print("\n..........................")
    print(f"\nAdded {name} with a garde {grade}.")

#Update student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print("\n..........................")
        print(f"Update Successful!!\n{name} mark is now {grade}.")
    else:
        print("\n..........................")
        print (f"{name} not found!!")

#delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print("\n..........................")
        print(f"{name} has been successfully deleted.")
    else:
        print("\n..........................")
        print (f"{name} not found!!")

#view all student
def display_all_students():
    if student_grades:
        for name , grade in student_grades.items():
            print("\n..........................")
            print(f"{name}: {grade}")
    else:
        print("\n..........................")
        print(f"No student found/added.")

def search_student(name, grade):
    if name in student_grades:
        print("\n..........................")
        print(f"{name} found with a grade of {student_grades[name]}.")
    else:
        print("\n..........................")
        print(f"{name} not found.")

