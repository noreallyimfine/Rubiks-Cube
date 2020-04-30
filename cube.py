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
        self.face1 = CubeFace()
        self.face2 = CubeFace()
        self.face3 = CubeFace()
        self.face4 = CubeFace()
        self.face5 = CubeFace()
        self.face6 = CubeFace()
        self.opposing_faces = [(self.face1, self.face2),
                               (self.face3, self.face4,
                               (self.face5, self.face6))]

    def initialize_centers(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']

        # set each faces center to a color, popping off list so to not rechoose
        # TODO: export to function
        faces = [self.face1, self.face2, self.face3,
                 self.face4, self.face5, self.face6]
        for face in faces:
            face.center = random.choice(colors)
            colors.remove(face.center)

    def initialize_edges(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']
        edges = ['top_center', 'mid_left', 'mid_right', 'bot_center']
        for edge in edges:
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