class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = self.side * 6
        print(self.perimeter)

hexagon1 = Hexagon(4)
hexagon1.calculate_perimeter()