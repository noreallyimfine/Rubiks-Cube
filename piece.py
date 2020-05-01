class Piece:
    def __init__(self, sides):
        self.sides = sides


class Center(Piece):
    def __init__(self, side1=None):
        self.side1 = side1

    def __repr__(self):
        return f"Center({self.side1})"

    def __str__(self):
        return f"Center Piece - ({self.side1})"


class Edge(Piece):
    def __init__(self, side1=None, side2=None):
        self.side1 = side1
        self.side2 = side2

    def __repr__(self):
        return f"Edge({self.side1, self.side2})"

    def __str__(self):
        return f"Edge Piece - ({self.side1}, {self.side2})"


class Corner(Piece):
    def __init__(self, side1=None, side2=None, side3=None):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __repr__(self):
        return f"Corner({self.side1}, {self.side2}, {self.side3})"

    def __str__(self):
        return f"Corner Piece - ({self.side1}, {self.side2}, {self.side3})"