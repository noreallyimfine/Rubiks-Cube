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
        
        self.edges = [self.top_center, self.mid_left, self.mid_right,
                      self.bot_center]

        self.corners = [self.top_left, self.top_right, self.bot_left,
                        self.bot_right]
        

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

        self.faces = [self.front, self.back, self.left,
                      self.right, self.upward, self.downward]

        self.opposing_colors = []

    def initialize_centers(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']

        # set each faces center to a color, popping off list so to not rechoose
        for face in self.faces:
            face.center = random.choice(colors)
            colors.remove(face.center)

        self.opposing_colors.append((self.front.center, self.back.center))
        self.opposing_colors.append((self.left.center, self.right.center))
        self.opposing_colors.append((self.upward.center, self.downward.center))

        print(self.opposing_colors)

    def initialize_edges(self):
        colors = ['w', 'y', 'o', 'r', 'b', 'g']
        color_count = {color: 0 for color in colors}
        # Hardercoded
        # Start from front face, top center
        # choose random color, assign it
        first_choice = random.choice(colors)
        self.front.top_center = first_choice
        # increment dict
        color_count[first_choice] += 1
        # choose another color 
        second_choice = first_choice
        # confirm its not opposing center from first color or the same color
        # assign to up face
        # increment color by one
# Locate the face-edge attached to it
                    # Choose a random color for that side
                    # Check that it's not the same color or the opposing color
                    # If it is, select again
                    # If not, assign it and increment the dict
            # Can probably do both sides of the edge piece in one go
            # There will be 4 of each color ultimately
            # Each color will pair with every other color except the opposing color

    def initialize_corners(self):
        pass

    def initialize_faces(self):
        # Map a color to each center
        self.initialize_centers()

        # create edges
        self.initialize_edges()

        # create corners
        self.initialize_corners()