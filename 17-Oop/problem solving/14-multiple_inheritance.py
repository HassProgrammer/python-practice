# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating
# multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is a battery 85kwh"


class Engine:
    def engine_info(self):
        return  "This is an engine 300 kW"

class ElectricCar2(Battery, Engine):
    pass


tesla = ElectricCar2()
print(tesla.battery_info())
print(tesla.engine_info())