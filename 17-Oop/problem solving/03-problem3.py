# Qs. Define a Employee class with attributes role, department & salary. this class also  
# has a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional
# attributes: name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print(f"Role: {self.role}\nDept: {self.dept}\nSalary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")


e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()
print("----------------------")
eng1 = Engineer("Elon Musk", 40) 
eng1.showDetails()