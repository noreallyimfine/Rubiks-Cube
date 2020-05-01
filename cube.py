import random
from piece import Piece, Center, Edge, Corner

class RubiksCube:
    def __init__(self):
        self.bot_layer = {'bottom_center': Center(), 'front_middle': Edge(),
                          'front_left': Corner(), 'front_right': Corner(),
                          'back_left': Corner(), 'back_right': Corner(),
                          'back_middle': Edge(), 'left_middle': Edge(),
                          'right_middle': Edge()}
        self.mid_layer = {'front_center': Center(), 'right_center': Center(),
                          'left_center': Center(), 'back_center': Center(),
                          'front_left': Edge(), 'front_right': Edge(),
                          'back_left': Edge(), 'back_right': Edge()}
        self.top_layer = {'top_center': Center(), 'front_middle': Edge(),
                          'front_left': Corner(), 'front_right': Corner(),
                          'back_left': Corner(), 'back_right': Corner(),
                          'back_middle': Edge(), 'left_middle': Edge(),
                          'right_middle': Edge()}
        
        self.opposing_colors = []
    
    def __repr__(self):
        return f"""RubiksCube({self.top_layer}, {self.mid_layer}, {self.bot_layer})"""

    def __str__(self):
        return f"""{self.top_layer}\n\n{self.mid_layer}\n\n{self.bot_layer}"""

    def initialize_centers(self):
        # List of colors
        colors = ['w', 'y', 'o', 'b', 'r', 'g']
        # list all the center pieces
        centers = [self.bot_layer['bottom_center'],
                   self.mid_layer['right_center'],
                   self.mid_layer['left_center'],
                   self.mid_layer['front_center'],
                   self.mid_layer['back_center'],
                   self.top_layer['top_center']]

        # looping through center pieces
        for piece in centers:
            print("Colors:", colors)
            color = random.choice(colors)
            # assign it a random choice from the colors
            piece.side1 = color
            # remove that color from list
            colors.remove(color)

        self.opposing_colors.append(
            (self.bot_layer['bottom_center'].side1, self.top_layer['top_center'].side1)
            )
        self.opposing_colors.append(
            (self.mid_layer['right_center'].side1, self.mid_layer['left_center'].side1)
            )
        self.opposing_colors.append(
            (self.mid_layer['front_center'].side1, self.mid_layer['back_center'].side1)
            )

    def initialize_edges(self):
        pass

    def initialize_corners(self):
        pass

    def initialize_cube(self):
        self.initialize_centers()

        self.initialize_edges()

        self.initialize_corners()

