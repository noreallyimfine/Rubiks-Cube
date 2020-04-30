class Piece:
    def __init__(self, sides):
        self.sides = sides


class Center(Piece):
    def __init__(self, side1=None, sides=1):
        self.side1 = side1


class Edge(Piece):
    def __init__(self, side1=None, side2=None, sides=1):
        self.side1 = side1
        self.side2 = side2


class Corner(Piece):
    def __init__(self, side1=None, side2=None, side3=None, sides=1):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
