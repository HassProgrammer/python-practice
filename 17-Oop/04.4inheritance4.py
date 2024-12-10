class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stop...")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("FOrtune")
car2 = ToyotaCar("Prius")

print(car1.name)
print(car2.start())
print(car1.stop())
print(car2.color)
        

        