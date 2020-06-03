'''
Class instatiation of pieces to use on a Rubik's Cube or similar object.
'''

class Piece:
    def __init__(self, sides, num_sides=1):
        self.num_sides = num_sides 
        if sides and len(sides) != self.num_sides:
                raise ValueError("Error: Wrong # of sides for that piece!")
        self.sides = {face: None for face in sides} 


class Center(Piece):
    def __init__(self, sides=None, num_sides=1):
        super().__init__(sides, num_sides)

    def __repr__(self):
        return f"Center({self.sides}, {self.num_sides})"

    def __str__(self):
        return f"Center Piece - ({self.num_sides}): {self.sides}"


class Edge(Piece):
    def __init__(self, sides=None, num_sides=2):
        super().__init__(sides, num_sides)

    def __repr__(self):
        return f"Edge({self.sides}, {self.num_sides})"

    def __str__(self):
        return f"Edge Piece - ({self.num_sides}): {self.sides}"


class Corner(Piece):
    def __init__(self, sides=None, num_sides=3):
        super().__init__(sides, num_sides)

    def __repr__(self):
        return f"Corner({self.sides}, {self.num_sides})"

    def __str__(self):
        return f"Corner Piece - ({self.num_sides}): {self.sides}"