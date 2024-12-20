# #(super) = Function used in a child class to call methods from a parent class
# (superclass) •
# Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
      def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
      def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled= True, radius= 5)
square = Square(color="blue", is_filled=False, width=36)
triangle = Triangle(color="aqua", is_filled=True, width=24, height=28)
print(f"Circle:\n------\nColor: {circle.color}\nIs Filled: {circle.is_filled}\nRadius: {circle.radius}\n")
circle.describe()
print("-----------------------------------------------")
print(f"Square:\n------\nColor: {square.color}\nIs Filled: {square.is_filled}\nWidth: {square.width}\n")
square.describe()
print("-----------------------------------------------")
print(f"Triangle:\n------\nColor: {triangle.color}\nIs Filled: {triangle.is_filled}\nWidth: {triangle.width}\nHeight: {triangle.height}")
triangle.describe()


