# Composition = The composed object directly owns its components, which cannot exist independently
#               "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.hors_power = horse_power
class Wheel:
    def __init__(self, size):
        self.size = size
class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)                 #{Note: Our class Car own an engine  and wheel}
        self.wheel = [Wheel(wheel_size)  for wheel in range(4)]

    def display_car(self):
        return f"Maker: {self.make} | Model: {self.model} | Horse Power: {self.engine.hors_power}(hp) | Wheel size: {self.wheel[0].size}(in)"


car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=675, wheel_size=19)

print(car1.display_car(), end="\n<-------------------------------->\n")
print(car2.display_car())

