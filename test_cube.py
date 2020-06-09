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
        mid_back_left = self.cube.mid_layer['back_left'].copy()
        top_left_middle = self.cube.top_layer['left_middle'].copy()
        mid_front_left = self.cube.mid_layer['front_left'].copy()
        bot_left_middle = self.cube.bot_layer['left_middle'].copy()


        self.cube._L()

        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], top_front_left['top'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], top_front_left['front'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], top_front_left['left'])

        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], bot_front_left['left'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], bot_front_left['bottom'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['top'], bot_front_left['front'])



if __name__ == "__main__":
    unittest.main()