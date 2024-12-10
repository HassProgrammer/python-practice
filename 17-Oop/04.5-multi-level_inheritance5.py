class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stop...")
    
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car2 = ToyotaCar("Toyota")

print(car1.start())
print(car1.type)
print(car2.brand)

        

        