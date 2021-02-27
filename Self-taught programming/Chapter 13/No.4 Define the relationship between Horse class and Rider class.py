class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self, rider):
        self.rider = rider

rider1 = Rider('john')
horse1 = Horse(rider1)