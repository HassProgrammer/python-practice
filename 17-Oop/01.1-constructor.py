class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student.")

roll1 = Student("Ahshanul", 55)
print(roll1.name, roll1.marks)

roll2 = Student("Sadman", 100)
print(roll2.name, roll2.marks)
