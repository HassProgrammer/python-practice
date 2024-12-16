# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance to check if tesla is an instance of Car and ElectricCar.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    total_car = 0
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        ElectricCar.total_car += 1

    def fuel_type(self):
        return "Electric charge"



car1 = Car("Toyota", "G-Corolla")
print("------Car details___________")
print(f"Full name: {car1.full_name()},\nBrand: {car1.brand},\nModel: {car1.model},\nFuel type: {car1.fuel_type()}\n")

car2 = Car("Tata", "Nexon")
print("------Car details___________")
print(f"Full name: {car2.full_name()},\nBrand: {car2.brand},\nModel: {car2.model},\nFuel type: {car2.fuel_type()}\n")
print(f"Total Car's: {Car.total_car}\n")

tesla = ElectricCar("Tesla", "Model S", "85kwh")
print("------Electric car details___________")
print(f"Full name: {tesla.full_name()},\nBrand: {tesla.brand},\nModel: {tesla.model},\nBattery size: {tesla.battery_size},\nFuel type: {tesla.fuel_type()}\n")

print(f"Total Car's: {ElectricCar.total_car}\n")

print(isinstance(tesla ,Car))
print(isinstance(tesla, ElectricCar))