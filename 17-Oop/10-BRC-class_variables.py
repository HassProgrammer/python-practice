# object = A "bundle" of related attributes (variables) and methods (functions)
#        Ex. phone, cup, book
#        You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object


from car10 import Car

car1 = Car("Mustang", 2024, "Red", False)
print(car1) #For print memory location

#using 'car1' object with '.' access modifier to print the value
print(f"Model: {car1.model}\nYear: {car1.year}\nColor: {car1.color}, Sale/Not: {car1.for_sale}\n")

car2 = Car("Corvette", 2025, "Blue", True)
print(f"Model: {car2.model}\nYear: {car2.year}\nColor: {car2.color}, Sale/Not: {car2.for_sale}\n")

car3 = Car("Charger", 2026, "Yellow", True)
print(f"Model: {car3.model}\nYear: {car3.year}\nColor: {car3.color}, Sale/Not: {car3.for_sale}\n")



car1.drive()
car2.drive()
car3.drive()
print("\n")
car1.stop()
car2.stop()
car3.stop()
print("\n")
car1.describe()
car2.describe()
car3.describe()