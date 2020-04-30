import random
from piece import Center, Edge, Corner


class CubeFace:
    def __init__(self):
        self.center = Center()
        self.top_left = Corner()
        self.top_center = Edge()
        self.top_right = Corner()
        self.mid_left = Edge()
        self.mid_right = Edge()
        self.bot_left = Corner()
        self.bot_center = Edge()
        self.bot_right = Corner()


class RubiksCube:

    colors = random.shuffle(['w', 'y', 'o', 'r', 'b', 'g'])

    def __init__(self):
        self.face1 = CubeFace()
        self.face2 = CubeFace()
        self.face3 = CubeFace()
        self.face4 = CubeFace()
        self.face5 = CubeFace()
        self.face6 = CubeFace()



    def randomize_faces():
        pass
        # need a list of potential colors
        # mapping of rules constraining color choices (for after choosing centers)

        # set each faces center to a color, popping off list so to not rechoose