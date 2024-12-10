class Student_marks:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem) / 3) +"%"


student1 = Student_marks(98, 99, 33)
print(student1.percentage)
student1.math = 100
print(student1.percentage)