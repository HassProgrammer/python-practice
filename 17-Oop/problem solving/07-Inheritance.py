# 3. Inheritance
# Problem: Create an Electric Car class that inherits from the Car class and has an additional attribute
# battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



car1 = Car("Toyota", "G-Corolla")
print("------Car details___________")
print(f"Full name: {car1.full_name()},\nBrand: {car1.brand},\nModel: {car1.model}\n")

tesla = ElectricCar("Tesla", "Model S", "85kwh")
print("------Electric car details___________")
print(f"Full name: {tesla.full_name()},\nBrand: {tesla.brand},\nModel: {tesla.model},\nBattery size: {tesla.battery_size}")