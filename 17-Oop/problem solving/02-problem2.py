# Qs. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area method of the class which calculates the area of the circle.
# Define a PerimeterO method of the class which allows you to calculate the perimeter of the
# circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())