class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rectangle1 = Rectangle()
square1 = Square()
rectangle1.what_am_i()
square1.what_am_i()