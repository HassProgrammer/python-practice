# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class Child (Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):
    def speaking(self):
        return f"WoOF!"

class Cat(Animal):
    def speaking(self):
        return f"Meow!"

class Mouse(Animal):
    def speaking(self):
        return f"Squeek!"


dog = Dog("Scooby Doo!")
cat = Cat("Garfield")
mouse = Mouse("Mickey")
print(f"{dog.name} is {dog.speaking()}")
print(f"He is {cat.name}. {cat.sleep()} after that {cat.speaking()}")
print(f"He is {mouse.name} and {mouse.eat()} then {mouse.speaking()} after that {mouse.sleep()} oh no! is {mouse.name} {mouse.is_alive}")