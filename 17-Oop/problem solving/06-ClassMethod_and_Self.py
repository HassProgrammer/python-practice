# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def the_full_name(self):
        return f"{self.brand} {self.model}"



car1 = Car("Toyota", "Corolla")
print(f"Brand: {car1.brand},\nModel: {car1.model}")
print("------Full name____________")
print(f"Full name: {car1.the_full_name()}")