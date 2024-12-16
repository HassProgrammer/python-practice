# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

# class Electric_Car(Car):
#     def __init__(self, brand, model, battery_size ):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
    

d_Car = Car("Toyota", "G-Corolla")
print("------Car details___________")
print(f"Full name: {d_Car.full_name()},\nBrand: {d_Car.get_brand()},\nModel: {d_Car.model}\n")

# tesla = Electric_Car("Tesla", "Model S", "85kwh")
# print("------Electric car details___________")
# print(f"Full name: {tesla.full_name()},\nBrand: {tesla.brand},\nModel: {tesla.model},\nBattery size: {tesla.battery_size}")