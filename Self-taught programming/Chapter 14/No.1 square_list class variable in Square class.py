class Square:
    square_list = []
    def __init__(self, side):
        self.side = side
        print('created!')
        self.square_list.append(self)

square1 = Square(5)
print(Square.square_list)