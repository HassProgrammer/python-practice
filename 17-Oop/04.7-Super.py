class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stop...")
    
class ToyotaCar(Car):
    def __init__(self, name, type):
        self.brand = name
        super().__init__(type)

car = ToyotaCar("Prius", "Electric")
print(car.type)