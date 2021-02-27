class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = self.side * 4
        print(self.perimeter)

    def change_size(self, change):
        self.side += change
        print(self.side)

square1 = Square(5)
square1.change_size(1)