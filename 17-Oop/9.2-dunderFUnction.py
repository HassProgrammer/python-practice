class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real}i + {self.img}j")
    def __add__(self, num2): #Using dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return  Complex(newReal, newImg)
    
    def __sub__(self, num2): #Using dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return  Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()
print("-----------")
num3 = num1 + num2 #for Using dunder function we can write num1+num2 except num1.add(num2)
num3.showNumber()
print("Sub--------------")
num4 = num1 - num2
num4.showNumber()