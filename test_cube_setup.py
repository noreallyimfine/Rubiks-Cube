import unittest
from cube import RubiksCube

class CubeSetupTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_color_count(self):

        # make sure there are 9 of each color
        color_dict = {'r': 0, 'o': 0, 'g': 0, 'b': 0, 'y': 0, 'w': 0}

        pieces = [
            self.cube.top_layer['front_right'],
            self.cube.top_layer['back_right'],
            self.cube.top_layer['front_left'],
            self.cube.top_layer['back_left'],
            self.cube.top_layer['back_middle'],
            self.cube.top_layer['front_middle'],
            self.cube.top_layer['right_middle'],
            self.cube.top_layer['left_middle'],
            self.cube.top_layer['top_center'],
            self.cube.mid_layer['left_center'],
            self.cube.mid_layer['right_center'],
            self.cube.mid_layer['front_center'],
            self.cube.mid_layer['back_center'],
            self.cube.mid_layer['front_left'],
            self.cube.mid_layer['back_left'],
            self.cube.mid_layer['back_right'],
            self.cube.mid_layer['front_right'],
            self.cube.bot_layer['front_right'],
            self.cube.bot_layer['front_left'],
            self.cube.bot_layer['back_left'],
            self.cube.bot_layer['back_right'],
            self.cube.bot_layer['back_middle'],
            self.cube.bot_layer['front_middle'],
            self.cube.bot_layer['right_middle'],
            self.cube.bot_layer['left_middle'],
            self.cube.bot_layer['bottom_center'],
        ]

        self.assertEqual(len(pieces), 26)


        for piece in pieces:
            for side in piece.sides:
                color = piece.sides[side]
                color_dict[color] += 1

        for color in color_dict:
            self.assertEqual(color_dict[color], 9)
    
if __name__ == "__main__":
    unittest.main()