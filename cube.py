import random
from piece import Piece, Center, Edge, Corner


class CubeFace:
    def __init__(self):
        self.center = None
        self.top_left = None
        self.top_center = None
        self.top_right = None
        self.mid_left = None
        self.mid_right = None
        self.bot_left = None
        self.bot_center = None
        self.bot_right = None

    def __str__(self):
        formatted_face = f"""
        {self.top_left} | {self.top_center} | {self.top_right}
        {self.mid_left} | {self.center} | {self.mid_right}
        {self.bot_left} | {self.bot_center} | {self.bot_right}
        """
        return formatted_face


class RubiksCube:
    def __init__(self):
        self.front = CubeFace()
        self.back = CubeFace()
        self.left = CubeFace()
        self.right = CubeFace()
        self.upward = CubeFace()
        self.downward = CubeFace()

        self.faces = faces = [self.front, self.back, self.left,
                              self.right, self.upward, self.downward]

        self.opposing_faces = [(self.front, self.back),
                               (self.left, self.right),
                               (self.upward, self.downward)]

    def initialize_centers(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']

        # set each faces center to a color, popping off list so to not rechoose
        for face in self.faces:
            face.center = random.choice(colors)
            colors.remove(face.center)

    def initialize_edges(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']
        color_count = {color: 0 for color in colors}
        edges = ['top_center', 'mid_left', 'mid_right', 'bot_center']
        for face in self.faces:
            for edge in edges:
                # Check if edge is None
                # if yes...
                    # Select 
            # Can probably do both sides of the edge piece in one go
            # There will be 4 of each color ultimately
            # Each color will pair with every other color except the opposing color

            pass

    def initialize_corners(self):
        pass

    def initialize_faces(self):
        # Map a color to each center
        self.initialize_centers()

        # create edges
        self.initialize_edges()

        # create corners
        self.initialize_corners()