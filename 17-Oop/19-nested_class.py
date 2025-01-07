# Nested class = A class defined within another class
#                   class Outer:
#                       class Inner:

# Benefits: Allows you to logically group classes that are
#           closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts

class Company1:
    class Employee:
        print("This is the first class.")

class Nonprofit:
    class Employee:
        print("This is the second class")

print("****************************************************")

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"
        

    def __init__(self, company_name):
        self.company_name = company_name
        self.employee  = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employee]
    
company = Company("Krab Kraby")
company2 = Company("KhanX")

company.add_employee("Khan", "Manager")
company.add_employee("Elon Musk", "Cook")
company.add_employee("Schooby Doo", "Cashier")

company2.add_employee("Sadman", "CEO")
company2.add_employee("Sakib", "Manager")

print(company.list_employees())

for employee in company.list_employees():
    print(employee, end="\n---------\n")

print("'''''''''''Company2''''''''''''")
print(company2.list_employees())
for employee in company2.list_employees():
    print(employee, end="\n---------\n")

# print(company.company_name)