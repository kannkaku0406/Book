class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        self.perimeter = (self.width + self.height) * 2
        print(self.perimeter)

class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        print(self.perimeter)

rectangle1 = Rectangle(3, 4)
square1 = Square(5)
rectangle1.calculate_perimeter()
square1.calculate_perimeter()