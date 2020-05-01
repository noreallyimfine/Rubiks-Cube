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
        self.bot_layer = {'top_center': Center(), 'front_middle': Edge(),
                          'front_left': Corner(), 'front_right': Corner(),
                          'back_left': Corner(), 'back_right': Corner(),
                          'back_middle': Edge(), 'left_middle': Edge(),
                          'right_middle': Edge()}

