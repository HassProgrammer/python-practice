class Student:
    collage_name = "Northern"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student.")
    def greeting(self):
        print(f"Assalamu Alikum {self.name}")
    def get_marks(self):
        return self.marks

student1 = Student("Ahshanul", 80)
print(Student.collage_name)
print(f"Your name {student1.name}, Your marks {student1.marks}")
student1.greeting()
print(f"You have {student1.get_marks()}")