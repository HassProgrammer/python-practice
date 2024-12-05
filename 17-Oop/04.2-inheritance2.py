class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of employee: {self.name}\nid: {self.id}")

class Programmer(Employee):
    def language(self):
        print("The default language is Python")

class Origin(Programmer):
    def nationality(self):
        print("Bangladesh")


emp = Employee("Ahshanul", 786)
emp.showDetails()
print("-------------------------------")
emp2 = Programmer("Araf", 107)
emp2.showDetails()
emp2.language()
print("-------------------------------")
emp3  = Origin("Sadman", 108)
emp3.showDetails()
emp3.language()
emp3.nationality()