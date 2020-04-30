class Center(Piece):
    def __init__(self, side1):
        self.side1 = side1


class Edge(Piece):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


class Corner(Piece):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

