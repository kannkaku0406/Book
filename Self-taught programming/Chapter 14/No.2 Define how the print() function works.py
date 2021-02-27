class Square:
    def __init__(self, side):
        self.side = side
        print('created!')

    def __repr__(self):
        s = str(self.side)
        return s + ' by ' + s + ' by ' + s + ' by ' + s

square1 = Square(6)
print(square1)