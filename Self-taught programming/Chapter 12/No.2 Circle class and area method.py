import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        print('Created!')

    def area(self):
        self.area = (self.radius ** 2) * math.pi
        print(self.area)

circle1 = Circle(4)
circle1.area()