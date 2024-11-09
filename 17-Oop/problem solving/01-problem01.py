# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            print(value)
            sum = sum + value
        print(f"Assalamualaikum {self.name}, your average score is {sum/3}  ")


student1 = Student("Hulk", [99,45,33])
student1.get_avg()
