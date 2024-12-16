# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.


class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "A car is a vehicle that has wheels, carries a small number of passengers, and is moved by an engine or a motor.\n"
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    total_car = 0
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        ElectricCar.total_car += 1

    def fuel_type(self):
        return "Electric charge"
    @staticmethod # Decorator
    def general_description():
        return "An electric car (EV) is a fully automatic vehicle that runs on an electric motor and produces zero tailpipe emissions"



car1 = Car("Toyota", "G-Corolla")
print("------Car details___________")
print(f"Full name: {car1.full_name()},\nBrand: {car1.brand},\nModel: {car1.model},\nFuel type: {car1.fuel_type()}\n")

print(car1.model) #print for decorator

car2 = Car("Tata", "Nexon")
print("------Car details___________")
print(f"Full name: {car2.full_name()},\nBrand: {car2.brand},\nModel: {car2.model},\nFuel type: {car2.fuel_type()}\n")
print(f"Total Car's: {Car.total_car}\n")
print(Car.general_description())

tesla = ElectricCar("Tesla", "Model S", "85kwh")
print("------Electric car details___________")
print(f"Full name: {tesla.full_name()},\nBrand: {tesla.brand},\nModel: {tesla.model},\nBattery size: {tesla.battery_size},\nFuel type: {tesla.fuel_type()}\n")

print(f"Total Car's: {ElectricCar.total_car}\n")

print(ElectricCar.general_description())