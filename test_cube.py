import unittest
from cube import RubiksCube

class CubeTurnTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_L(self):

        # Corners
        top_back_left = self.cube.top_layer['back_left'].sides.copy()
        top_front_left = self.cube.top_layer['front_left'].sides.copy()
        bot_front_left = self.cube.bot_layer['front_left'].sides.copy()
        bot_back_left = self.cube.bot_layer['back_left'].sides.copy()

        # Edges
        mid_back_left = self.cube.mid_layer['back_left']
        top_left_middle = self.cube.top_layer['left_middle']
        mid_front_left = self.cube.mid_layer['front_left']
        bot_left_middle = self.cube.bot_layer['left_middle']

        print("Top front left before turn", top_front_left)

        self.cube._L()

        print("Top front left after turn", top_front_left)
        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], top_front_left['top'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], top_front_left['front'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], top_front_left['left'])




if __name__ == "__main__":
    unittest.main()