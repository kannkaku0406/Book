class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area = self.width * self.height / 2
        print(self.area)

triangle1 = Triangle(2, 5)
triangle1.area()