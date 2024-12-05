class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def running(self):
        print("This rabbit is running.")

class Fish(Animal):
    def swimming(self):
        print("This rabbit is swimming.")

class Hawk(Animal):
    def flying(self):
        print("This hawk is flying.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#using inherit methods
print(rabbit.alive)
fish.eat()
hawk.sleep()

#using own methods
rabbit.running()
fish.swimming()
hawk.flying()