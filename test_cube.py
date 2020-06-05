import unittest
from cube import RubiksCube

class CubeTurnTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_L(self):

        # Corners
        top_back_left = self.cube.top_layer['back_left']
        top_front_left = self.cube.top_layer['front_left']
        bot_front_left = self.cube.bot_layer['front_left']
        bot_back_left = self.cube.top_layer['back_left']

        # Edges
        mid_back_left = self.cube.mid_layer['back_left']
        top_left_middle = self.cube.top_layer['left_middle']
        mid_front_left = self.cube.mid_layer['front_left']
        bot_left_middle = self.cube.bot_layer['left_middle']