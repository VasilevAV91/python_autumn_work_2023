class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    def info(self):
        print(self.colour)
        self.square

a = Shape('Red', 10)
b = Shape('Blue', 20)
a.info()
b.info()

