# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"



car1 = Car("Toyota", "G-Corolla")
print("------Car details___________")
print(f"Full name: {car1.full_name()},\nBrand: {car1.brand},\nModel: {car1.model},\nFuel type: {car1.fuel_type()}\n")

tesla = ElectricCar("Tesla", "Model S", "85kwh")
print("------Electric car details___________")
print(f"Full name: {tesla.full_name()},\nBrand: {tesla.brand},\nModel: {tesla.model},\nBattery size: {tesla.battery_size},\nFuel type: {tesla.fuel_type()}")